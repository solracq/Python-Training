'''
Created on Sep 25, 2013

@author: Doug
'''

with open("alt.txt") as alt, open("a.txt", "w") as a, open("b.txt", "w") as b:
 for line in alt:
   if line.startswith("a"):
     a.write(line)
   elif line.startswith("b"):
     b.write(line)
