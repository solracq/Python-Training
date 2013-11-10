#!/usr/bin/env python3

import re

# match anything BUT a letter, digit, underscore, or apostrophe
rx_wordsep = re.compile(r"[^\w']+")

s1 = 'There are 10 kinds of people in a Binary world -- "Geek talk"'

words = rx_wordsep.split(s1)
print(words)

