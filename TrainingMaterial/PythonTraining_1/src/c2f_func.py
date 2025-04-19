'''
@author: cquiroz
'''

if __name__ == '__main__':
    pass

def c2f(ctemp):
    print("Converting Celsius to Fahrenheit: ")
    celsius=float(ctemp)
    fahrenheit = (9*celsius)/5 +32
    print(celsius,"\u00B0 Celsius corresponds to ", fahrenheit, "\u00B0 Fahrenheit")
    
c2f(100)
c2f(0)
c2f(37)
c2f(-40)
