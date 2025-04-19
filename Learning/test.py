def find_goodtest(generated_tests, test_ids):
    for dictionary in generated_tests:
        if dictionary['test_id'] in test_ids:
            return dictionary

test_ids = ['cat', 'dog', 'log']
generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]
print(find_goodtest(generated_tests, test_ids))


def rotatetoleft(s, n):
    return s[n:] + s[:n]


def rotatetoright(s, n):
    return s[-n:] + s[:-n]

import random
def matrix(n:int):
    matrix = [[random.randint(10,90) for i in range(n)] for j in range(n)]
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print()
    print()
    return matrix

def spiral_matrix(matrix):
    arr = []
    for i in range(len(matrix)):
        if i % 2 != 0:
            for k in range(len(matrix[i])-1, -1, -1):
                arr.append(matrix[i][k])
        else:
            for l in range(len(matrix[i])):
                arr.append(matrix[i][l])
    return arr
# Execution
m = matrix(4)
print(spiral_matrix(m))
print()

import itertools
array = list(range(1,10))
permuted = []
permuted_lists = []
count = 0
for i in range(1, 10):
    permuted += list(itertools.permutations(array, i))
for item in permuted:
    item_sorted = sorted(item)
    if item_sorted in permuted_lists:
        continue
    else:
        permuted_lists.append(item_sorted)
print(permuted_lists)
print(len(permuted_lists)) # 986409 vs 511

