#!/usr/bin/env python3

import re

fs = "apple banana artichoke cherry date enchilada appetizer"
r = re.compile(r"\b(a[a-z]+)(\s*)") # match words that start with 'a'

def replace_it(m):
    # group 1 is the 'a' word, group 2 is space after it
    return "'" + m.group(1) + "'" + m.group(2)

print(r.sub(replace_it,fs))  # replace with callback

