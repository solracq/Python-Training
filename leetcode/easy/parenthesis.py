'''
@author: Solrac
'''
def parenthesis_validation(s):
    lista = list(s) 
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    stack = []
    
    for i in range(len(lista)):
        if lista[i] in op:
            stack.append(lista[i])
        elif lista[i] in cp:
            position = cp.index(lista[i])
            if len(stack) > 0 and stack[len(stack)-1] == op[position]:
                stack.pop()
            else:
                return 'UNBALNCED'
    if len(stack) == 0:
        return 'BALANCED'
    
s = '[({})[()]{[()]}]'
print(s)
print(parenthesis_validation(s))
