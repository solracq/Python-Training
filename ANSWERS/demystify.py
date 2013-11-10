#!/usr/bin/env python3

with open("../DATA/mystery","rb") as m:
    mystery_bytes = m.read()

print(''.join(chr(c) for c in mystery_bytes[::2]))
