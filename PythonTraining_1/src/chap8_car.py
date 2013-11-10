'''
Created on Sep 26, 2013

@author: cquiroz
'''

if __name__ == '__main__':
    pass

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM    ", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(*a):
    print(a.low)
    
    
cleanup(spam)