#!/usr/bin/env python3

counts = {}

with open("../DATA/breakfast.txt") as BR: 

    for line in BR:
        breakfast_item = line[:-1]
        counts[breakfast_item] = counts.get(breakfast_item,0) + 1

for item,count in counts.items():
    print(item,count)