#!/usr/bin/env python3

import re

fs = "apple banana artichoke cherry date enchilada appetizer"
fruits = fs.split()

r1 = re.compile(r"c.")
for f in fruits:
    if r1.search(f):
        print(f, end=' ')
print()

for f in fruits:
    m = r1.search(f)
    if m:
        print(f, end=' ')
        print(m.group(), end=' ')
        print(m.start(), end=' ')
        print(m.end())
print()

r2 = re.compile(r"a([a-z]{3})(.)")
print(r2.findall(fs))
print()

for m in r2.finditer(fs):
    print(m,m.group(),m.start(),m.end(),m.group(1))

print(re.findall(r'\ba.{3}',fs,re.IGNORECASE))
