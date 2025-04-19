import random
import itertools

# Delete elements in list
def confirmusers():
    unconfirmed_users = ['alice', 'brian', 'candace']
    confirmed_users = []
    count = 0
    while len(unconfirmed_users) != 0:
        print("Verifying {0}".format(unconfirmed_users[count]))
        confirmed_users.append(unconfirmed_users[count])
        del unconfirmed_users[count]
    print(unconfirmed_users)
    print(confirmed_users)

def del_list_item(lista:list):
    print(lista)
    for i in range(0, len(lista)-5):
        del lista[i+1]
    else:
        print("Finilized List: ", end="")
    print(lista)

def list_remove_item(lista:list):
    print(lista)
    for fruit in lista:
        print(fruit)
        lista.remove(fruit)
    else:
        print("Finilized List: ", end="")
    print(lista)
    lista.remove(lista[len(lista)-1])
    print(lista)

def remove_duplicates_while(lista):
    while 'cat' in lista:
        lista.remove("cat")
        print(lista)

def get_common(lista1, lista2):
    common_list = []
    for i in range(len(lista1)):
        if lista1[i] in lista2 and lista1[i] not in common_list:
            common_list.append(lista1[i])
    return common_list

def get_common2(lista1, lista2):
    common_list = []
    for item in lista1:
        if item in common_list:
            continue
        if item in lista2:
            common_list.append(item)
    return common_list

def get_unique(lista1, lista2):
    unique_list = []
    for item in list1:
        if item not in list2:
            unique_list.append(item)
    return unique_list

def get_min(lista:list):
    min = lista[0]
    for i in range(len(lista) - 1):
        if min > lista[i+1]:
            min = lista[i+1]
        else:
            pass
    return min

def get_max(lista:list):
    max = lista[0]
    for i in range(len(lista) - 1):
        if max < lista[i+1]:
            max = lista[i+1]
        else:
            pass
    return max

def linear_search(lista, k):
    for item in lista:
        if item == k:
            return lista.index(item)

def binary_search(lista, k):
    lista.sort()
    start = 0
    end = len(lista)
    middle = (start + end + 1) // 2
    found = -1
    while start < end or found == -1:
        if lista[middle] == k:
            found = middle
        if k < lista[middle]:
            end = middle - 1
        elif lista[middle] < k:
            start = middle + 1
        middle = (start + end + 1) // 2
    return found

def selection_sort(lista):
    for i in range(len(lista)):
        min = i
        for j in range(i+1, len(lista)):
            if lista[min] > lista[j]:
                min = j
        # swap(lista, i, min)
        lista[i], lista[min] = lista[min], lista[i]
    return lista

def swap(l, first, second):
    temp = l[first]
    l[first] = l[second]
    l[second] = temp

def insertion_sort(arr:list):
    for i in range(len(arr)):
        insert = arr[i]
        move_item = i
        while (move_item > 0) and (arr[move_item - 1] > insert):
            arr[move_item] = arr[move_item - 1]
            move_item -= 1
        arr[move_item] = insert
    return arr

def find_duplicate(arr):
    duplicate = []
    non_duplicate = []
    for i in range(len(arr) - 1):
        if arr[i] in duplicate:
            continue
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicate:
                duplicate.append(arr[i])
        if arr[i] not in duplicate:
            non_duplicate.append(arr[i])
    return (duplicate, non_duplicate)

def find_dup(arr):
    dup_arr = list()
    for item in arr:
        if item in dup_arr:
            continue
        if arr.count(item) >= 2:
            dup_arr.append(item)
    return dup_arr

def find_unique(arr):
    unq_arr = []
    for item in arr:
        if arr.count(item) == 1:
            unq_arr.append(item)
    return unq_arr

def create_matrix(n):
    matrix = [[random.randint(0, 90) for column in range(n)] for row in range(n)]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column], end=" ")
        print()
    print()

if __name__ == "__main__":
    int_list = [random.randint(0, 90) for i in range(10)]
    str_list = ['banana', 'strawberry', 'berry', 'apple', 'pear', 'peach', 'mango']
    pet = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
    list1 = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
    list2 = ["THREE", "SEVEN", "EIGHT", "FOUR", "THREE"]
    confirmusers()
    del_list_item(int_list)
    list_remove_item(str_list)
    print(pet)
    remove_duplicates_while(pet)
    print(get_common(list1, list2))
    print(get_common2(list1, list2))
    print(get_unique(list1, list2))

    lista = [1, 2, 3, 4, 5]
    print(lista)
    del lista[1:4]
    print(lista)
    lista = [1, 2, 3, 4, 5]
    lista.pop()
    print(lista)
    lista.pop(2)
    print(lista)
    lista.remove(4)
    print(lista)
    lista2 = [8, 9]
    lista.extend(lista2)
    print(lista)
    lista3 = [6, 7]
    print(lista2 + lista3)
    lista.extend(lista3)
    print(lista)
    print(f"sorted {sorted(lista)}")
    print(lista)
    lista.sort()
    print(lista)
    lista4 = [4, 5]
    lista.append(lista4)
    print(lista)
    lista.extend(lista4)
    lista.append(4)
    print(lista)
    print(f"ocurrences of 4 in list: {lista.count(4)}")
    print(lista.index(9))
    lista = [1, 2, 3, 4, 5]
    lista.sort(reverse=True)
    print(f"reversed lista = {lista}")
    lista.reverse()
    print(lista)

    lista = [5, 3, 7, 9, 3, 8, 2]
    print(lista)
    print(f"min = {get_min(lista)}")
    print(min(lista))
    print(f"max = {get_max(lista)}")
    print(max(lista))
    k = 9
    print(f"{k} in '{lista}' at the position (linear search) {linear_search(lista, k)}")
    lista = [5, 3, 7, 9, 3, 8, 2]
    print(lista[1:len(lista)-1])
    print(f"{k} in '{lista}' at the position (binary search) {binary_search(lista, 8)}")
    listb = [5, 3, 7, 9, 3, 8, 2]
    print(f"Unordered list: {listb}")
    print(f"Ordered list: {selection_sort(listb)}")
    lista = [5, 6]
    print(f"original = {lista}")
    swap(lista, 0, 1)
    print(f"swaped = {lista}")
    lista[0], lista[1] = lista[1], lista[0]
    print(f"swaped again = {lista}")
    listb = [5, 3, 7, 9, 3, 8, 2]
    print(insertion_sort(listb))
    lista = [5, 3, 7, 9, 3, 8, 2, 3]
    dup, non_dup = find_duplicate(lista)
    print(f"{lista} duplicate -> {dup} ... just in case non-duplicate -> {non_dup}")

    mythical = ["Unicorn", "Balrog", "Vampire", "Dragon", "Minotaur"]
    non_mythincal = ["dog", "cat", "horse", "cow"]
    print(mythical)
    mythical.extend(non_mythincal)
    print(mythical)
    mythical.insert(5, "lion")
    print(mythical)
    mythical.remove('cow')
    print(mythical)
    mythical.insert(6, "tiger")
    print(mythical)
    del mythical[len(mythical)-1]
    print(mythical)
    print(mythical[::-1])
    mythical.pop(1)
    print(mythical)
    mythical.sort(reverse=True)
    print(mythical)
    mythical.insert(8, "Medusa")
    print(mythical)
    new_lista = list()
    new_lista = non_mythincal[:]
    print(new_lista)
    new_lista.clear()
    print(new_lista)
    mythical.pop(mythical.index("cat"))
    print(mythical)
    mythical.insert(2, "Dragon")
    print(mythical)
    print(mythical.count("Dragon"))
    new_lista = non_mythincal.copy()
    print(new_lista)
    arr = [3, 5, 6, 8, 3, 9, 7]
    print(f"lista = {arr}")
    print(f"First max = {max(arr)}")
    arr.remove(max(arr))
    print(f"Second max = {max(arr)}")
    print(arr)
    mythical.insert(len(mythical)-1, "Dragon")
    print(mythical)
    print(find_dup(mythical))
    print(find_unique(mythical))
    seto = set(mythical)
    print(seto)
    seto.add("cocodrile")
    print(seto)
    seto.discard("dog")
    print(seto)
    print("{8}".format(*mythical))
    even_list = [i for i in range(0, 11, 2)]
    print(even_list)
    odd_list = [i for i in range(1, 11, 2)]
    print(odd_list)
    sqr_list = [i**2 for i in range(10)]
    print(sqr_list)
    data = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'g', 'f', 'c']
    print(data)
    sorted_arr = sorted(data)
    unique_keys = []
    groups = []
    for key, group in itertools.groupby(sorted_arr):
        unique_keys.append(key)
        groups.append(group)
    print(unique_keys)
    print(groups)
    create_matrix(4)
 ######## STACK ##########
stack = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'g', 'f', 'c']
print(stack)
print(stack.pop())
print(stack)
stack2 = []
try:
    print(stack2.pop())
except IndexError:
    print("Empty Stack!")
else:
    # stack2.append('b')
    print(stack2)