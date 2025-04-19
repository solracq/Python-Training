from collections import deque

def deque_list(arr:list):
    queue = deque(arr)
    print(queue)
    queue.append(8)
    print(f"Add item to the right: {queue}")
    queue.appendleft(0)
    print(f"Add item to the left: {queue}")
    queue.pop()
    print(f"Remove item from the right: {queue}")
    queue.popleft()
    print(f"Remove item from the left: {queue}")
    queue.insert(2, 9)
    print(f"Add new item at a specified index: {queue}")
    queue.rotate(3)
    print(f"Rotating the queue to the right: {queue}")
    queue.rotate(-3)
    print(f"Rotating the queue to the left: {queue}")
    arr = list(queue)
    print(arr)
# Execution
arr = [1, 2, 3, 4, 5, 6, 7]
deque_list(arr)
