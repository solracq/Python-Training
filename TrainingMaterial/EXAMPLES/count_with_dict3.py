#!/usr/bin/env python3

from collections import Counter
counts = Counter()

with open("../DATA/breakfast.txt") as BR: 

    for line in BR:
        breakfast_item = line[:-1]
        counts[breakfast_item] += 1

for item,count in counts.items():
    print(item,count)