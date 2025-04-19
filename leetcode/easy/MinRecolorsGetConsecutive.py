# Minimum Recolors to Get K Consecutive Black Blocks
# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the
# ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
# You are also given an integer k, which is the desired number of consecutive black blocks.
# In one operation, you can recolor a white block such that it becomes a black block.
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
# Example:
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Example:
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
def min_consecutive(s, k):
    b = []
    w = []
    count = 1
    # Creating lists for the Black and White positions
    for i in range(len(s)):
        if s[i] == "B":
            b.append(i)
        else:
            w.append(i)
    print(f"b = {b}")
    print(f"w = {w}")
    # If the size of s is one W
    if len(w) == 1 and b == []:
        return 1
    # Checking if the number of k continue numbers already exists
    for i in range(len(b) - 1):
        if abs(b[i] - b[i + 1]) == 1:
            count += 1
            if count >= k:
                return 0
        else:
            count = 1
    # Switching Wites to Blacks to meet the minimum K continue numbers
    count = 0
    arr = []
    for i in range(len(s)):
        if i not in b:
            b.append(i)
            b.sort()
            if len(arr) < k-1: # The previous condition before adding the last continues number
                count += 1
            print(f"Appended {i} to {b} so count = {count} and arr = {arr}")
        print(f"b = {b}")
        j = 0
        print(f"{j} {b[j]} {b[j+1]}")
        while abs(b[j] - b[j+1]) == 1:
            print(f"b[j] - b[j+1] = {b[j]} - {b[j+1]}")
            arr.append(b[j])
            arr = set(arr)
            arr = list(arr)
            print(f"arr = {arr}")
            j += 1
            print(f"j = {j}")
            print(f"{b[j]} == {len(b)-1}")
            if b[j] == len(b)-1:
                arr.append(b[j])
            if len(arr) == k:
                return count

blocks1 = "WBBWWBBWBW"
k1 = 7
blocks2 = "WBWBBBW"
k2 = 2
blocks3 = "BWWWBB"
k3 = 6
blocks4 = "W"
k4 =1
blocks5 = "WBB"
k5 = 1
blocks6 = "WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW"
k6 = 15
print(min_consecutive(blocks6, k6))

def min_consecutive2(blocks, k):
    count_w = 0
    count_b = 0
    res = []
    queue = list(blocks)
    count = 0
    while len(queue) > 0:
        previous = queue.pop(0)
        if previous == "W":
            count_w += 1
        if previous == "B":
            count_b += 1
            if count_b < k:
                count = count_w + count_b
                print(count)
                if count == k:
                    res.append(count_w)
                    count = 0
                    count_w = 0
                    count_b = 0
    return res