'''
@author: Solrac
'''
from random import randint

def create_matrix(size):
    matrix = [[randint(10, 90) for i in range(size)] for j in range(size)]
    return matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = ' ')
        print()

def spiral_matrix(n):
    matrix = create_matrix(4)
    start_row = 0
    end_row = n
    start_column = 0
    end_column = n
    lista = []
    while start_row < end_row and start_column < end_column:
        for i in range(start_column, end_column):
            lista.append(matrix[start_row][i])
        
        start_row += 1
        
        for i in range(start_row, end_row):
            lista.append(matrix[i][end_column-1])
            
        end_column -= 1
        
        if start_row < end_row:
            for i in range(end_column-1, start_column-1, -1):
                lista.append(matrix[end_row-1][i])
            
            end_row -= 1
            
        if start_column < end_column:
            for i in range(end_row-1, start_row-1, -1):
                lista.append(matrix[i][start_column])
                
            end_column += 1
    print()
    return lista
    
matrix = create_matrix(4)
print_matrix(matrix)
print(spiral_matrix(4))