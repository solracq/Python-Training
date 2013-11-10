#!/usr/bin/env python3

import re

rx_num = re.compile(r"\b\d{3}-\d{4}\b")

with open('../DATA/custinfo.dat') as CUST:
    for line in CUST:
        if rx_num.search(line):
            print(line, end=' ')

