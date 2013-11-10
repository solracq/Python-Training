'''
Created on Sep 25, 2013

@author: cquiroz
'''

if __name__ == '__main__':
    pass

ctemps = [100.0, 34.0, 23.0, 56.0, 45.0]
fruts = ["apple", "mango", "watermelon", "stawberry", "guava"]
#f = [ctemps*9/5+32 for c in ctemps]

# Excersise 5-2
for c in ctemps:
    f = ( ( c * 9 ) / 5) + 32
    print( "{0:.1f}\u00B0 Celsius corresponds to {1:.1f}\u00B0 Fahrenheit".format(c,f))
    
