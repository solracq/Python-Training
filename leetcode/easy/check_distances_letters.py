'''
Check Distances Between Same Letters
You are given a 0-indexed string s consisting of only lowercase English letters, where each letter in s appears exactly
twice. You are also given a 0-indexed integer array distance of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, ... , 'z' -> 25).

In a well-spaced string, the number of letters between the two occurrences of the ith letter is distance[i].
If the ith letter does not appear in s, then distance[i] can be ignored.


Return true if s is a well-spaced string, otherwise return false.
Excample:
Input: s = "abaccb", distance = [1,3,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Output: true

Explanation:
- 'a' appears at indices 0 and 2 so it satisfies distance[0] = 1.
- 'b' appears at indices 1 and 5 so it satisfies distance[1] = 3.
- 'c' appears at indices 3 and 4 so it satisfies distance[2] = 0.
Note that distance[3] = 5, but since 'd' does not appear in s, it can be ignored.
Return true because s is a well-spaced string.
'''
def check_distance(s:str, distance:list) -> bool:
    # Vars
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    dictionary = {}
    duplicates = []
    arr = ['flower', 'flowless', 'flat']
    L = min([len(i) for i in arr])
    print(f"L = {L}")
    matches = []
    for i in range(L, 1, -1):
        subs = [substring[0:L] for substring in arr]
        print(f"subs= {subs}")
        all_equal = list(set(subs))
        print(f"all_equal= {all_equal}")
        if len(all_equal) == 1:
            return str(all_equal)
        else:
            pass

s = ""
distance = []
check_distance(s, distance)