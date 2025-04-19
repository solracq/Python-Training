#!/usr/bin/env python3

counts = {}

with open("../DATA/breakfast.txt") as BR: 

    for line in BR:
        breakfast_item = line[:-1]
        if breakfast_item in counts:
            counts[breakfast_item] += 1
        else:
            counts[breakfast_item] = 1

for item,count in counts.items():
    print(item,count)