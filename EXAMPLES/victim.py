#!/usr/bin/env python3

import sys

for f in sys.argv[1:]:
    print("Processing",f)
    F = open(f, "r")
    c=0
    for l in F:
        c=c+1
        print(l)