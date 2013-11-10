#!/usr/bin/env python3

x = 5
def spam():
    x = 22 # does not set global x
    print("spam(1)",x)
    y = "wolverine"
    print("spam(2)",y)

def eggs():
    global x
    print("eggs(1)",x)
    x = "wolverine"
    print("eggs(2)",x)

spam()
print("after spam(): x is ",x)
eggs()
print("after eggs(): x is ",x)