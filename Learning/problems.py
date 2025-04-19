import sys
import random
import math

def count_substring_in_string(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] != sub_string[0]:
            continue
        else:
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
    return count
# Execution
string = "TestCaseTestCase"
sub_string = "CaseT"
print(f"The number of times '{sub_string}' is contained in '{string}' is: {count_substring_in_string(string, sub_string)}\n")

def parenthesis_validation(s):
    op = ['{', '[', '(']
    cp = ['}', ']', ')']
    s_list = list(s)
    stack = []
    for i in range(len(s)):
        if s_list[i] in op:
            stack.append(s_list[i])
        elif s_list[i] in cp:
            location = cp.index(s_list[i])
            if len(stack) > 0 and op[location] == stack[len(stack)-1]:
                stack.pop()
            else:
                return "UNBALANCED"
    if len(stack) == 0:
        return "BALANCED"
# Execution
s = "{[()[]{}]}"
print(f"Is '{s}' balanced? {parenthesis_validation(s)}\n")

def reverse_string_chunk(s, chunk):
    output = []
    for i in range(0, len(s), chunk):
        output.append(s[i:i+chunk][::-1])
    return "".join(output)

# Execution
s = "abcdefghijkl"
chunk = 3
print(f"Reversing '{s}' in chunks of {chunk} is: {reverse_string_chunk(s, chunk)}\n")

def linear_search(arr:list, k:int):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

# Execution
arr = [34, 56, 2, 10, 77, 51, 93, 30, 5, 52]
k = 77
print(f"Find {k} in {arr} = {linear_search(arr, k)}\n")

def binary_search(arr:list, k:int):
    s = 0
    e = len(arr) - 1
    middle = (s + e + 1) // 2
    found = -1
    arr.sort()
    while s < e and found == -1:
        if arr[middle] == k:
            found = middle
        elif arr[middle] < k:
            s = middle + 1
        else:
            e = middle - 1
        middle = (s + e + 1) // 2
    return found

# Execution
k = 30
arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(arr)
print(sorted(arr))
print(f"Binary Search: {k} is located in {binary_search(arr, k)}\n")

def find_min(arr:list):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min
# Execution
arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"The minimum number in {arr} is {find_min(arr)}\n")

def find_max(arr:list):
    max = arr[0]
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
# Execution
arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"The maximum number in {arr} is {find_max(arr)}\n")

def sorting(arr:list):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
# Execution
arr = [34, 67, 89, 12, 21, 45, 88, 56, 73, 11, 48, 67, 5, 30, 32]
print(f"Original array: {arr}")
sorting(arr)
print(f"Sorted array: {arr}\n")

def insert_sort(arr:list):
    for i in range(len(arr)):
        insert = arr[i]
        move_item = i
        while (move_item > 0) and (arr[move_item-1] > insert):
            arr[move_item]= arr[move_item-1]
            move_item -= 1
        arr[move_item] = insert

# Execution
print("Insert Sort")
lista = [80, 35, 75, 11, 7, 38, 34, 45, 35, 67, 17, 14, 83, 94, 88, 56, 2, 10, 77, 51, 93, 30, 5, 52, 70, 1, 99, 84, 22,
         11, 4, 76, 69]
print(lista)
insert_sort(lista)
print(lista)
print()

def find_sum_two_num(arr:list, x):
    arr.sort()
    res = tuple()
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == x:
                return res + (i, j)
            if arr[i] + arr[j] > x:
                break
# Execution
arr = [50, 20, 10, 80, 75, 35]
x = 70
print(arr)
print(sorted(arr))
print(find_sum_two_num(arr, x))
print()

def two_point_approach(arr:list, x):
    arr.sort()
    start = 0
    end = len(arr) - 1
    while (start < end):
        if arr[start] + arr[end] == x:
            return (start, end)
        if arr[start] + arr[end] < x:
            start += 1
        else:
            end -= 1
    return False
# Execution
x = 70
arr = [50, 20, 10, 80, 75, 35]
arr.sort()
print(arr)
print(f"The sum {x} of two nums using Two Point Approach: {two_point_approach(arr, x)}\n")

def closest_sum_zero_sim(arr, x):
    diff = sys.maxsize
    start = 0
    end = len(arr) - 1
    res_s = 0
    res_e = 0
    while start < end:
        if abs(arr[start] + arr[end] - x) < diff:
            res_s = start
            res_e = end
            diff = abs(arr[start] + arr[end] - x)
        elif arr[start] + arr[end] < x:
            start += 1
        else:
            end -= 1
    return (res_s, res_e)
# Execution
nums = [1, 3, 4, 7, 10]
x = 15
print(f"O(nlog(n)) : {closest_sum_zero_sim(nums, x)}\n")
arr = [-1, 3, 2, -5, 4]
x = 0
print(f"O(nlog(n)) : {closest_sum_zero_sim(arr, x)}\n")

def closest_sum_zero(arr):
    min_sum = sys.maxsize
    for i in range(len(arr)):
        curr_sum = arr[i]
        if min_sum > abs(curr_sum):
            min_sum = abs(curr_sum)
            start = i
            end = i
        for j in range(i+1, len(arr)):
            curr_sum = curr_sum + arr[j]
            if min_sum > abs(curr_sum):
                min_sum = abs(curr_sum)
                start = i
                end = j
    return [start, end]
# Execution
arr = [-1, 3, 2, -5, 4]
print(f"O(n)^2 : {closest_sum_zero(arr)}")

def three_sum_zero(arr):
    arr.sort()
    res = []
    found = False
    for i in range(0, len(arr) - 1):
        s = i + 1
        e = len(arr) - 1
        while s < e:
            if arr[s] + arr[e] + arr[i] == 0:
                # res.append((s, e, i))
                print(f"indexes: {s}, {e}, {i}")
                print(f"Nums: {arr[s]}, {arr[e]}, {arr[i]}")
                found = True
                s += 1
                e -= 1
            elif arr[s] + arr[e] + arr[i] < 0:
                s += 1
            else:
                e -= 1
    # print(res)
    return found

def three_sum_zero_no_efficient(arr):
    res = []
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            for k in range(j+1, len(arr)):
                if arr[i]+arr[j]+arr[k] == 0:
                    res.append((i, j, k))
    return res

# Execution
arr = [-1, 0, 1, 2, -1, -4]
print(sorted(arr))
print(f"3sumzero found : {three_sum_zero(arr)}\n")

def four_sum_zero(arr):
    arr.sort()
    found = False
    for i in range(0, len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            s = j + 1
            e = len(arr) - 1
            while s < e:
                if arr[s] + arr[e] + arr[i] + arr[j] == 0:
                    print(f"indexes: {s}, {e}, {i}, {j}")
                    print(f"Nums: {arr[s]}, {arr[e]}, {arr[i]}, {arr[j]}")
                    found = True
                    s += 1
                    e -= 1
                elif arr[s] + arr[e] + arr[i] + arr[j] < 0:
                    s += 1
                else:
                    e -= 1
    return found
# Execution
arr = [-1, 0, 1, 2, -1, -4]
print(sorted(arr))
print(f"4sumzero found : {four_sum_zero(arr)}\n")

def compression(string:str):
    s_list = list(string)
    arr = []
    arr_sol = []
    current_char = s_list[0]
    i = 0
    while i < len(string)-1:
        s_rotated = s_list[1:] + s_list[:1]
        s_list = s_rotated
        s_rotated.pop()
        # s_list = s_list.pop(0)
        if current_char == s[i]:
            arr.append(s[i])
        else:
            arr_sol.append(str(len(arr)) + current_char)
            arr.clear()
            current_char = s[i]
            arr.append(s[i])
        i += 1
    arr_sol.append(str(len(arr)) + current_char)
    return "".join(arr_sol)

def compression_groupby(string:str) -> str:
    from itertools import groupby
    arr = list(s)
    res = []
    for key, groups in groupby(arr):
        res.append(str(len(list(groups)))+key)
    return "".join(res)

# Execution
s = "AAAABBBCCCCCC"
print(f"Compressing {s} = {compression(s)}\n")

import random
def matrix(n:int):
    matrix = [[random.randint(10,90) for i in range(n)] for j in range(n)]
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

def spiral_matrix_efficient(m:list)->list:
    res = []
    for i in range(0, len(m)):
        if i % 2 == 0:
            res.append(m[i])
        else:
            res.append(m[i][::-1])
    return res

# Execution
m = matrix(4)
print(spiral_matrix(m))
print()

def get_contents_file(file):
    with open(file) as text_file:
        contents = text_file.read()
    print(contents.rstrip())
# Execution
get_contents_file('file.txt')

def get_linebyline_file(file):
    with open(file) as text_file:
        for line in text_file:
            print(line)
# Execution
get_contents_file('file.txt')

def store_list_file_contents(file):
    with open(file) as text_file:
        arr = text_file.readlines()
    print(arr[0])
    for i in range(len(arr)):
        print(arr[i].rstrip())
# Execution
store_list_file_contents('file.txt')

def append_lines_file(file):
    with open(file) as text_file:
        lines = text_file.readlines()
    s = ''
    for line in lines:
        line = line.strip()
        s += line
    print(s)
# Execution
append_lines_file('file.txt')

def write_content_file(file):
    with open(file, 'w') as new_text_file:
        new_text_file.write("I love programming!\n")
# Execution
write_content_file("programming.txt")

def append_contents_file(file):
    with open(file, 'a') as file_obj:
        file_obj.write('Programming is fun!\n')
# Execution
append_contents_file("programming.txt")

def excepts(num:int):
    answ = 0
    try:
        answ = 5 / num
    except ZeroDivisionError:
        print(f'{num} cannot be zero!')
    else:
        print(answ)
# Execution
excepts(5)

def store_list_file_json(file):
    import json
    arr = [1, 2, 3, 4, 5]
    with open(file, 'w') as file_obj:
        json.dump(arr, file_obj)
# Execution
store_list_file_json('numbers.json')

def get_json_contents(file):
    import json
    with open(file) as file_obj:
        numbers = json.load(file_obj)
    print(numbers)
# Execution
get_json_contents('numbers.json')

def manipulate_json(s):
    import json
    # Generate dict
    dictionary = {s[i]:s.count(s[i]) for i in range(len(s))}
    # Convert dict to json
    json_fmt = json.dumps(dictionary, indent=4, sort_keys=True)
    print(json_fmt)
    for key, value in sorted(dictionary.items(), key=lambda x: x[1]):
        print(f"{key}: {value}")
# Execution
s = "Testing is very dupper fun"
manipulate_json(s)

def find_duplicates(arrs:list):
    duplicates = []
    for arr in arrs:
        if arr in duplicates:
            continue
        if arrs.count(arr) == 2:
            duplicates.append(arr)
    return duplicates
# Execution
arrs = [1,3,2,6,7,8,8,5,4,2,1,5,4,6,9]
print(f"List with duplicates: {arrs}")
print(f"Found duplicates: {find_duplicates(arrs)}\n")

def find_uniques(arrs:list):
    uniques = []
    for arr in arrs:
        if arrs.count(arr) == 1:
            uniques.append(arr)
    return uniques
# Execution
arrs = [1,3,2,6,7,8,8,5,4,2,1,5,4,6,9]
print(f"List with uniques: {arrs}")
print(f"Found unique items: {find_uniques(arrs)}\n")

def find_first_nonduplicate(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
s = "google"
print(f"first non-duplicate in '{s}' is: {find_first_nonduplicate(s)}")

def list_left_append_pop(arr:list):
    print(arr)
    arr.append(6)
    print(f"add item to the right: {arr}")
    arr.pop()
    print(f"remove item to the right: {arr}")
# Execute
arr = [1, 2, 3, 4, 5]
list_left_append_pop(arr)

def compression2(s):
    queue = list(s)
    previous = ""
    res = []
    arr = []
    while len(queue) > 1:
        previous = queue.pop(0)
        if previous == queue[0]:
            arr.append(previous)
        else:
            arr.append(previous)
            res.append(str(len(arr))+previous)
            arr.clear()
    res.append(str(len(arr)+1)+previous)
    return "".join(res)
# Execution
s = "AAAABBBCCCCCC"
print(f"Compressing {s} = {compression2(s)}\n")

def compression3(s):
    queue = list(s)
    res = []
    compressed = []
    count = 1
    while len(queue) > 1:
        previous = queue.pop(0) # A  AAABBBCCCCCC # A  AABBBCCCCC    # A  ABBBCCCCC  # A BBBCCCCCC
        if previous == queue[0]: # A == A         # A == A           # A == A        # A != B and A == A
            count += 1           # 2              # 3                # 4             # compressed = [4A]
            res.append(previous) # B  BBCCCCCC   # B == B count=2
        elif previous != queue[0] and previous == res[len(res)-1]:
            compressed.append(str(count)+res[len(res)-1])
            count = 1
            res.clear()
    compressed.append(str(count) + res[len(res) - 1])
    return "".join(compressed)
# Execution
s = "AAAABBBCCCCCC"
print(f"Compressing {s} = {compression3(s)}\n")

def compression_imporved(s):
    from itertools import groupby
    arr = list(s)
    groups = []
    res = []
    for key, group in groupby(arr):
        groups.append(list(group))
    for group in groups:
        res.append(str(len(group)) + group[0])
    return "".join(res)

# Execution
s = "AAAABBBCCCCCC"
# output = 4A3B6C
print(f"Compressing {s} = {compression_imporved(s)}")

def multiply_except_itself(arr):
    result = []
    for i in range(len(arr)):
        multiplication = 1
        for j in range(len(arr)):
            if i == j:
                continue
            multiplication *= arr[j]
        result.append(multiplication)
    return result
# Execution
arr = [-10, 5, 2, 8]
# output = [5*2*8, -10*2*8, -10*5*8, -10*5*2*8]
print(arr)
print(f"Multiply all items except itself: {multiply_except_itself(arr)}")

def find_first_second_maxs(arr):
    res = []
    count = 0
    while count < 2:
        max = arr[0]
        for i in range(len(arr)):
            if max < arr[i]:
                max = arr[i]
        res.append(max)
        arr.remove(max)
        count += 1
    print(f"First maximum: {res[0]} \nSecond maximum: {res[1]}")

# Execution
arr = [5, 17, 19, 23, 34, 45, 52, 53, 58, 62, 65, 77, 88, 90, 65, 5]
print(arr)
find_first_second_maxs(arr)

def find_max_sum(arr):
    sums = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            sum = arr[i] + arr[j]
            sums.append(sum)
    return max(sums)
# Execution
arr = [-1, -2, -3, -4]
print(arr)
print("Maximum sum from list above: ", find_max_sum(arr)) #-3

def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = []
    for i in range(len(s)):
        if s[i] in vowels:
            continue
        res.append(s[i])
    return "".join(res)
s = "ca"
print(s)
print(remove_vowels(s))

def urlify(s):
    s = s.strip()
    return s.replace(" ", "%")
s = "  Mr. John Smith "
print(s)
print(urlify(s))

def sort_min(arr:list):
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

def sort_occurrences(arr): # TBD
    occur = []
    sort_min(arr)
    for i in range(len(arr) - 1):
        min_ocurr = i
        for j in range(i + 1, len(arr)):
            if arr.count(arr[min_ocurr]) > arr.count(arr[j]):
                min_ocurr = j
        arr[i], arr[min_ocurr] = arr[min_ocurr], arr[i]
    return arr
# Execuiton
arr = [3, 1, 2, 2, 4]
print(f"Not sorted arr = {arr}")
print(f"Sorted by value= {sort_min(arr)}")
print(f"SORT OCCURENCES: {sort_occurrences(arr)}")

def print_sum_matrix(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum
matrix = [[random.randint(10, 90) for i in range(4)] for j in range(4)]
print(print_sum_matrix(matrix))
matrix2 = [[3, 2, 5], [8, 7, 1], [9, 3, 4]]
total = print_sum_matrix(matrix2)
print(total)

def find_diff_btw_nums(arr):
    res = []
    size = len(arr)
    for i in range(size-1):
        previous = arr.pop(0)
        res.append(abs(previous - arr[0]))
    return res
# Execution
arr = [3, 4, 5, 2, 1]
print("FIND DIFFERENCE BTW NUMBERS")
print(arr)
print(find_diff_btw_nums(arr))

def find_min_btw_nums(arr):
    res = []
    size = len(arr)
    for i in range(size-1):
        previous = arr.pop(0)
        if previous > arr[0]:
            res.append(arr[0])
        else:
            res.append(previous)
    return res
# Execution
arr = [3, 4, 5, 2, 1]
print("FIND MINIMUM BTW NUMBERS")
print(arr)
print(find_min_btw_nums(arr))

def is_palindrome(x):
    string = str(x)
    if string == string[::-1]:
        return "IS PALINDROME"
    else:
        return "IS NOT PALINDROME"

def is_palindrome_num(x):
    size = round(math.log10(x))
    s = 0
    incr = 1
    decr = 100000
    while s < size:
        decr /= 10
        f = math.trunc(x // decr)
        incr *= 10
        b = x % incr
        print(f"f= {f}")
        print(f"b= {b}")
        if f != b:
            return "is NOT palindrome"
        s += 1
        size -= 1
    return "is palindrome"

def is_palindrome_num2(x):
    import math
    size = round(math.log10(x)+1)
    incr = 10
    decr = 10000
    count = 0
    for i in range(size):
        if (x % incr) == int(str(math.trunc(x / decr))[::-1]):
            count += 1
        incr *= 10
        decr /= 10
    # i0 = math.trunc(x / 10000)
    # i1 = math.trunc(x / 1000)
    # i2 = math.trunc(x / 100)
    # i3 = math.trunc(x / 10)
    # i4 = x
    # x % 10 = 1  == reversed(x/10000)
    # x % 100 = 21 == reversed(x/1000)
    # x % 1000 = 521 == revesed (x/100)
    # x % 10000 = 2521 == reversed (x/10)
    # x % 100000 == revesed (x/1)
    if count == size:
        return "Is palindrome"
    else:
        return "Is NOT palindrome"

# Execution
x=12521
# Lenght of an integer
print(round(math.log10(x)+1))
print(x)
print(is_palindrome(x))
print(is_palindrome_num(x))

def making_anagrams(a, b):
    sorteda = sorted(a)
    sortedb = sorted(b)
    resa = []
    resb = []
    for itema in sorteda:
        if itema not in sortedb:
            resa.append(itema)
    for itemb in sortedb:
        if itemb not in sorteda:
            resb.append(itemb)
    extra_items = len(resa) + len(resb)
    return extra_items
# Execution
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print("MAKING ANAGRAM")
print(making_anagrams(a, b))

def making_anagrams2(a, b):
    res_a = []
    res_b = []
    counta = 0
    countb = 0
    for i in range(len(a)):
        if a[i] in res_a:
            continue
        if a[i] in b:
            res_a.append(a[i])
        else:
            counta += 1
    for i in range(len(b)):
        if b[i] in res_b:
            continue
        if b[i] in a:
            res_b.append(b[i])
        else:
            countb += 1
    # Checking if both are anagrams
    if sorted(res_a) == sorted(res_b):
        print("IS ANAGRAM")
    else:
        print("IS NOT ANAGRAM")
    print(f"Removed items = {counta + countb}")
    return ("".join(res_a), "".join(res_b))
# Execution
a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
print("MAKING ANAGRAM")
print((a, b))
print(making_anagrams2(a, b))

def wrap(string, max_width):
    arr = []
    for i in range(0, len(string), max_width):
        arr.append(string[i:i+max_width]+"\n")
    return "".join(arr)
# Execution
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
print(string)
print(wrap(string, max_width))

def lengthOfLongestSubstring(s):
    duplicates = []
    sub_strings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    res = []
    for i in range(len(sub_strings)):
        if sub_strings[i] in duplicates:
            continue
        if sub_strings.count(sub_strings[i]) >= 2:
            duplicates.append(sub_strings[i])
        res.append(sub_strings[i])
    return len(res)
# Execution
s = "poder total"
print(s)
print('longest substring:', lengthOfLongestSubstring(s))
print()

def find_phone_address(s, dictionary):
    for key, value in dictionary.items():
        if key == s:
            return (f"{key}: {value}")
    return f"Phone number info for the user not found!"
# Execute
print("find phone address")
dict_ = {'sam': '99912222', 'tom': '11122222', 'harry': '12299933'}
s = "harry"
print(find_phone_address(s, dict_))

def separate_nums(num):
    res = []
    for i in range(math.trunc(math.log10(num)+1)):
        if i == 0:
            div = num // 10
            mod = num % 10
        else:
            mod = div % 10
            div = div // 10
        res.append(mod)
    return res[::-1]
# Execute
num = 12345
print("Numbers", num)
print("Separate numbers", separate_nums(num))
print()

def minwindowsubs(s, t):
    sub_strings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    valid_sub_strings = []
    for i in range(len(sub_strings)):
        if len(sub_strings[i]) >= len(t):
            t_list = list(t)
            count = 0
            while len(t_list) > 0:
                previous = t_list.pop(0)
                if previous in sub_strings[i]:
                    count += 1
                else:
                    break
            if count == len(t):
                valid_sub_strings.append(sub_strings[i])
    dictionary = {}
    for valid_substring in sorted(valid_sub_strings, key=lambda x: x[1]):
        dictionary[valid_substring] = len(valid_substring)
    dict_list = list(dictionary)
    return dict_list[0]

def minwindowsubs2(s, t):
    substr = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
    res = []
    for i in range(len(substr)):
        queue = list(t)
        count = 0
        while len(queue) > 0:
            previous = queue.pop(0)
            if previous in substr[i]:
                count += 1
            else:
                break
        if count == len(t):
            res.append(substr[i])
    dictionary = {}
    for i in range(len(res)):
        dictionary[len(res[i])] = res[i]
    return dictionary[min(list(dictionary.keys()))]

# Execute
s = "ADOBECODEBANC"
t = "ABC"
print("MINIMUM WINDOW")
print(f"String: {s}")
print(f"Sub-string: {t}")
print(minwindowsubs(s, t))

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# Execution
print(fibonacci(30))

def prime(n):
    for i in range(1, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i, end=", ")
                    break
# Execution
prime(100)
print()

def find_goodtest(generated_tests, test_ids):
    for i in range(len(generated_tests)):
        for test_id in test_ids:
            if generated_tests[i]['test_id'] in test_ids:
                return generated_tests[i]['test_id']

def find_good_test_improved(generated_tests_list, test_ids_list):
    for generated_test_dict in generated_tests_list:
        if generated_test_dict['test_id'] in test_ids_list:
            return generated_test_dict
# Execution
test_ids = ['cat', 'dog', 'log']
generated_tests = [{'test_id': 'dogz', 'number': 12}, {'test_id': 'log', 'number':15}]
print(find_goodtest(generated_tests, test_ids))
print(find_good_test_improved(generated_tests, test_ids))

def compare_two_dictionaries(dictionary1, dictionary2):
    if dictionary1 == dictionary2:
        return True
    else:
        return False
# Execution
dictionary1 = {'test_id': 'dogz', 'number': 12}
dictionary2 = {'test_id': 'log', 'number':15}
print(compare_two_dictionaries(dictionary1, dictionary2))
print(compare_two_dictionaries(dictionary2, dictionary2))

def grouping_data(data):
    from itertools import groupby
    unique_keys = []
    groups = []
    data = sorted(data)
    for key, group in groupby(data):
        unique_keys.append(key)
        groups.append(list(group))
    print(unique_keys)
    print(groups)

def grouping_data_long(arr):
    groups = []
    duplicates = []
    for i in range(len(arr)):
        if arr[i] in duplicates:
            continue
        group = []
        for j in range(i, len(arr)):
            if arr[i] == arr[j]:
                group.append(arr[i])
            duplicates.append(arr[i])
        groups.append(group)
    return groups

# Execution
data = ['a', 'b', 'a', 'a', 'c', 'd', 'b', 'g', 'f', 'c']
print("Grouping Data")
grouping_data(data)
# output: [['a', 'a', 'a'], ['b', 'b'], ['c', 'c'], ['d'], ['f'], ['g']]

def approximate_sum_two_lists(arr1, arr2, x):
    s = 0
    e = len(arr2) - 1
    res_s = 0
    res_e = 0
    diff = sys.maxsize
    while s < len(arr1) and e >= 0:
        if abs(arr1[s] + arr2[e] - x) < diff:
            res_s = s
            res_e = e
            diff = abs(arr1[s] + arr2[e] - x)
        elif arr1[s] + arr2[e] < x:
            s += 1
        else:
            e -= 1
    print(arr1[res_s], arr2[res_e], 'Difference =', diff)

# Execution
print("APPROXIMATE SUM TWO LISTS")
arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 38
approximate_sum_two_lists(arr1, arr2, x)

def closest_num(arr, k):
    dictionary = {}
    arr.sort()
    for num in arr:
        dictionary[abs(num-k)] = num
    return dictionary[min(dictionary.keys())]

# Execution
arr = [9, 11, 5, 3, 25, 18]
k= 6
# output : 5
print(f"The closest element in the list {arr} for {k} is: {closest_num(arr, k)}")

def adding_plusone_to_listToDigit(nums):
    # string = ""
    # for i in range(len(nums)):
    #     string += str(nums[i])
    res = []
    for i in range(len(nums)):
        if i != len(nums) - 1:
            res.append(nums[i])
        else:
            res.append(nums[i] + 1)
    return res
# Execution
nums = [1, 2, 3]
print(nums)
print(adding_plusone_to_listToDigit(nums))

def minwindows(s, subst):
    sl = list(subst)
    res = []
    indexes = []
    for i in range(len(s)):
        if s[i] in sl and sl != []:
            indexes.append(i)
            sl.remove(s[i])
            if sl == []:
                sl = list(subst)
                res.append(indexes)
                indexes = []
    for item in res:
        src = item[0]
        end = item[len(item)-1]+1
        indexes.append(s[src:end])
    return indexes

string = "ADOBECODEBANC"
sub_string = "ABC"
print(f"MINWIN = {minwindows(string, sub_string)}")

def longest_prefix(arr):
    min_element = min(arr)
    queue = list(min_element)
    res = []
    for i in range(len(queue)):
        previous = queue.pop(0)
        for element in arr:
            if element == min_element:
                continue
            if previous == element[i]:
                if previous in res:
                    continue
                res.append(previous)
            else:
                return "".join(res)

def longest_prefix2(arr):
    dictionary = {}
    for item in sorted(arr, key=lambda x: x[1]):
        dictionary[len(item)] = item
    min_item = dictionary[min(list(dictionary.keys()))]
    result = []
    for i in range(len(arr)):
        queue = list(min_item)
        count = 0
        res = []
        while len(queue) > 0:
            previous = queue.pop(0)
            if previous == arr[i][count]:
                res.append(previous)
                count += 1
            else:
                break
        result.append("".join(res))
    return min(result)

# Execution
lista = ['flower', 'flowless', 'flat']
print(lista)
print(longest_prefix(lista))

def find_majority_num(nums):
    dictionary = {}
    for i in range(len(nums)):
        dictionary[nums.count(nums[i])] = nums[i]
    return dictionary[max(dictionary.keys())]
# Execution
nums = [2,2,1,1,1,2,2]
print(nums)
print(find_majority_num(nums))

def largest_consecutive_sum(arr):
    sub_str = [arr[i:j] for i in range(len(arr)) for j in range(i+1, len(arr)+1)]
    res = []
    for i in range(len(sub_str)):
        sum = 0
        for j in range(len(sub_str[i])):
            sum += sub_str[i][j]
        res.append(sum)
    return max(res)

# Execution
print("LARGEST CONSECUTIVE SUM")
arr = [1]
print(largest_consecutive_sum(arr))
arr = [-2, 1]
print(largest_consecutive_sum(arr))
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(largest_consecutive_sum(arr))

def merger(arr1, m, arr2, n):
    if m > n:
        for i in range(m):
            if arr1[i] == 0:
                previous = arr2.pop(0)
                arr1[i] = previous
    return arr1
# Execution
print("MERGER")
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [4, 5, 6]
print(merger(nums1, len(nums1), nums2, len(nums2)))

def is_anagram_list(arr):
    sorted_elem = sorted(arr[0])
    count = 0
    for i in range(1, len(arr)):
        if sorted_elem == sorted(arr[i]):
            count += 1
    if count == len(arr) -1:
        return True
    else:
        return False
# Execution
arr = ['ice', 'eci', 'cei']
print(is_anagram_list(arr))

def pascals_triangle(num_rows):
    res = []
    for i in range(num_rows):
        arr = []
        for j in range(0, i+1):
            if j == 0:
                arr.append(1)
            elif j == i:
                arr.append(1)
            else:
                for k in range(0, 1):
                    arr.append(sum(res[i-1][k:k+2]))
        res.append(arr)
    return res
# Execution
# output: [[1],[1,1],[1,2,1], [1,3,3,1], [1,4,6,4,1]]
print(pascals_triangle(5))

