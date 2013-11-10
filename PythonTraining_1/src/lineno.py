'''
Created on Sep 25, 2013

@author: cquiroz
'''
import sys

if __name__ == '__main__':
    pass

text1 = str(sys.argv[1])

with open (text1) as F:
    for line in enumerate(F):
        print(line)