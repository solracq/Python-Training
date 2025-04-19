#!/usr/bin/env python3

with open("../DATA/mystery","rb") as m:
    while True:
        bytes = m.read(2)
        if not bytes:
            break
        print(chr(bytes[0]),end='')
