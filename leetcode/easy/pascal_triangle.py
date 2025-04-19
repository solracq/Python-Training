'''
@author: Solrac
'''
def pascals_triangle(numRows):
    mainlist = []
    for i in range(numRows):
        lista = []
        for j in range(0, i+1):
            if j == 0:
                lista.append(1)
            elif j == i:
                lista.append(1)
            else:
                for k in range(0, 1):
                    lista.append(sum(mainlist[i-1][k:k+2]))
        mainlist.append(lista)
    return mainlist
    
lista = [[1],[1,1],[1,2,1], [1,3,3,1], [1,4,6,4,1]]
print(pascals_triangle(5))
