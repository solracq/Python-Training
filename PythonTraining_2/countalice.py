#!/usr/bin/env python3

count = 0
with open("../DATA/alice.txt") as al:
    for line in al:
        if 'Alice' in line:
            count += 1

print("Alice occurred on {0} lines in alice.txt".format(count))
