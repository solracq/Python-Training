#!/usr/bin/python3

numpairs = [(5,1),(1,5),(5,0),(0,5)]

total = 0

for x,y in numpairs:
    try:
        quotient = x/y
    except Exception as e:
    	print("uh-oh, when y = {0}, {1}".format(y,e))
    else: 
        total += quotient
print(total)