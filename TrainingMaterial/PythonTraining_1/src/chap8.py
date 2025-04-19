'''
@author: cquiroz
'''

if __name__ == '__main__':
    pass

'''
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
    global spam
    for i in spam:
        print(i.lower().strip())
    
    
cleanup(spam)