# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
# Input: s = "abccbaacz"
# Output: "c
#
# Constraints:
# 2 <= s.length <= 100
# s consists of lowercase English letters.
# s has at least one repeated letter

def first_letter_twice(s: str) -> str:
    if len(s) < 2 or len(s) > 100:
        return "Invalid Input!"

    queue = list(s.lower())
    while len(queue) > 1:
        first_char = queue.pop(0)
        if first_char == queue[0]:
            return first_char
    queue = list(s.lower())
    while len(queue) > 1:
        first_char = queue.pop(0)
        if s.count(first_char) >= 2:
            return first_char
    return "No repeated chars!"

# Execution
s = "abccbaacz"
s1 = "tslwn"
s2 = "nwcn"
s3 = "x"
s4 = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm"
s5 = "regzueqr"
print(first_letter_twice(s5))

# Second approach, the above won't work if we want to find the letter that repeats with the lowest index, eg) "regzueqr"
# the answer is "e" because the duplicate has lower index than "r"

def first_letter_twice_better(s: str) -> str:
    duplicate = []
    dictionary = {}
    for i in range(len(s) - 1):
        if s[i] in duplicate:
            continue
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                dictionary[j] = s[j]
                duplicate.append(s[j])
    if dictionary != {}:
        return dictionary[min(dictionary.keys())]
    else:
        return -1

# Execution
s = "abccbaacz"
s1 = "tslwn"
s2 = "nwcn"
s3 = "x"
s4 = "qwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnmqwertyuioplkjhgfdsazxcvbnm"
s5 = "regzueqr"
print(first_letter_twice_better(s5))

def first_letter_twice_best(s):
    duplicates = []
    dictionary = {}
    for i in range(len(s) - 1):
        if s[i] in duplicates:
            continue
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                rep_index = j
                dictionary[rep_index] = s[i]
                duplicates.append(s[i])
                break
    if len(duplicates) == 0:
        return "NO REPETITIONS!"
    return dictionary[min(list(dictionary.keys()))]

print(first_letter_twice_best(s5))