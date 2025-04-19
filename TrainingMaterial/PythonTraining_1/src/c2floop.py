'''
@author: cquiroz
'''

if __name__ == '__main__':
    pass


c=input("Type the number of Celsius to convert to Fahrenheit: ")

celsius=float(c)

fahrenheit = (9*celsius)/5 +32

print(celsius,"\u00B0 Celsius corresponds to ", fahrenheit, "\u00B0 Fahrenheit")

r = input("Do you want to try again (y) or quit (q)? : ")
resp = str(r)  
while True:
    if resp.lower() == "q":
        print("Goodbye!")
        break
    else :
        c=input("Type the number of Celsius to convert to Fahrenheit: ")
        celsius=int(c)
        fahrenheit = (9*celsius)/5 +32
        print(celsius,"\u00B0 Celsius corresponds to ", fahrenheit, "\u00B0 Fahrenheit")
        r = input("Do you want to try again (y) or quit (q)? : ")
        resp = str(r)  
     
