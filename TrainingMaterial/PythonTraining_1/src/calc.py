'''
@author: cquiroz
'''

if __name__ == '__main__':
    pass

def add(a,b):
    c = a + b
    print("{0} + {1} = {2}".format(a,b,c))

def substract(a,b):
    if a>b:
        c = a - b
        print("{0} - {1} = {2}".format(a,b,c))
    else:
        c= b - a
        print("{0} - {1} = {2}".format(b,a,c))
        
def request_val(a,op,b):
    op = str(op)
    if (type(a)==str):
        a=float(a)
    if(type(b)==str):
        b=float(b)
    
    if op == "+":
        add(a,b)
    elif op == "-":
        substract(a,b)
    else:
        print("Wrong operation!")
        
print("Type two numbers and the desired operation, eg) 3+5 means 3,+,5: ")
a = input("Give me the first number: ")
b = input("Give me the second number: ")
c = input("Give me the operand (+,-): ")
request_val(a,c,b)