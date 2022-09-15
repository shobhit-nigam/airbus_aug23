import pandas as pd
import os
import numpy as np
from datetime import datetime
import os
import sys
import time
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# fixed values
slot_upper_limit = 140
data_file = "test_data.csv"
count = 0
slot_overflow = ""
cached_time_stamp = os.stat(data_file).st_mtime
frequency = 1
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_id = "trainer.nigam@gmail.com"
password = "iwqxwpojganikbbl"
email_line = "please check the attached text file for details"
critical_msg = ""
critical = ""


def check_slots(df):
    global count
    global slot_overflow
    global critical_msg
    global critical
    dfa = pd.read_csv(df)
    slot_based = dfa['test_slot'].value_counts()
    dfb = dfa.drop_duplicates(subset=['email'], keep='last')

    line1 = "total registrations with duplicates " + str(dfa.shape[0]) + "\n"
    line2 = "total registrations without duplicates " + str(dfb.shape[0]) + "\n"
    line3 = "total slots filled (with duplicates) : " + "\n"
    total_slots = len(dfb['test_slot'].value_counts())
    counts = str(slot_based)
    line4 = counts[0:counts.rfind('\n')] + "\n"

    now = datetime.now()
    line0 = now.strftime("on %a, %d %b at %I:%M:%p\n")
    current_time = now.strftime("%d_%b_%I_%M_%p")
    file_name = "status_" + current_time + ".txt"

    with open(file_name, "w") as fa:
        fa.write(line0)
        fa.write(line1)
        fa.write(line2)
        fa.write(line3)
        fa.write(line4)

    slot_dict = dict(slot_based)

    for k, v in slot_dict.items():
        if v > slot_upper_limit:
            count = count + 1
            slot_overflow = slot_overflow + "\n" + k + " has reached " + str(v) + " bookings "

    if count > 0:
        critical = "needs attention, slots are filling up\n"
        critical_msg = "Report : needs attention"
        slot_overflow = f"The following slots have crossed {slot_upper_limit}" + slot_overflow
    else:
        critical = f"no slots above {slot_upper_limit} yet\n"
        critical_msg = "Report: all good"

    print("intiating email")
    message = MIMEMultipart('mixed')
    message['From'] = 'Report'.format(sender_id)
    message['To'] = 'mr.nigam@gmail.com'
    message['CC'] = 'sukhb9119@gmail.com'
    message['Subject'] = critical_msg

    msg_content = critical + line2 + slot_overflow + email_line
    body = MIMEText(msg_content, 'plain')
    message.attach(body)

    fa = open(file_name)
    attachment = MIMEText(fa.read())
    attachment.add_header('Content-disposition', 'attachment', filename=file_name)
    message.attach(attachment)
    msg_full = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_id, password)
        server.sendmail(message["From"], message["To"].split(","), message["Cc"].split(","), msg_full)
        server.quit()
    print("send the email successfully")


def check_time_stamp(df):
    global cached_time_stamp
    stamp = os.stat(df).st_mtime
    if stamp != cached_time_stamp:
        cached_time_stamp = stamp
        print("file has changed, intiating check_slots function")
        check_slots(data_file)

def watch(df):
    while True:
        try:
            time.sleep(frequency)
            check_time_stamp(df)
        except FileNotFoundError:
            pass
        except KeyboardInterrupt:
            print("user has shut down the process")
            os._exit(0)

def send_email():
    message = MIMEMultipart('mixed')
    message['From'] = 'Report'.format(sender_id)
    message['To'] = 'mr.nigam@gmail.com'
    message['CC'] = 'sukhb9119@gmail.com'
    message['Subject'] = critical_msg

    msg_content = critical + line2 + slot_overflow + email_line
    body = MIMEText(msg_content, 'plain')
    message.attach(body)

    fa = open(file_name)
    attachment = MIMEText(fa.read())
    attachment.add_header('Content-disposition', 'attachment', filename=file_name)
    message.attach(attachment)
    msg_full = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_id, password)
        server.sendmail(message["From"], message["To"].split(","), message["Cc"].split(","), msg_full)
        server.quit()
    print("send the email successfully")

watch(data_file)
