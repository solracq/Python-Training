'''
@author: Solrac
'''
def longest_prefix(lista):
    mainlist = []
    for i in range(len(lista) - 1):
        result = []
        for j in range(len(lista[i]) - 1):
            if lista[i][j:j+1] == lista[i+1][j:j+1]:
                result.append(lista[i][j:j+1])
            else:
                break
        if result != []:
            mainlist.append("".join(result))
        else:
            return ""
    
    return min(mainlist)

lista = ['flower', 'flowless', 'flat']
print(lista)
print(longest_prefix(lista))
        