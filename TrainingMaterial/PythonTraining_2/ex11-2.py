#!/usr/bin/env python3

import re

rx_rabbit = re.compile(r"\brabbit('?s)?\b",re.I)
replacement = 'badger'

def preserve_case(m):
    old_text = m.group()

    if old_text.isupper():
        replacement_text = replacement.upper()
    elif old_text[0].isupper():
        replacement_text = replacement.capitalize()
    else:
        replacement_text = replacement

    return replacement_text

with open('../DATA/alice.txt') as ALICE:
    with open('badger.txt','w') as BADGER:
        for line in ALICE:
            new_line = rx_rabbit.sub(preserve_case,line)
            BADGER.write(new_line)
