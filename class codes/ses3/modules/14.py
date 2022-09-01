display = print

display("hello")

print = 10

display("hello")
display(print)

# 1. print = display
# 2. print = __builtins__.print
# 3. del print

del print

print("howdy")
