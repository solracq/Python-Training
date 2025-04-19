#!/usr/bin/env python3

import re

fs = "apple banana artichoke cherry date enchilada appetizer"
r = re.compile(r"\b(a[a-z]+)(\s*)") # match words that start with 'a'

print(r.sub('',fs))       # delete matched text
print(r.subn('XXX',fs))   # replace matched text with 'XXX'

