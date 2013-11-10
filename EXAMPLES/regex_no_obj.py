#!/usr/bin/env python3

import re

fs = "apple banana Artichoke cherry date enchilada APPETIZER"

print(re.findall(r'\ba.{3}',fs,re.IGNORECASE))
