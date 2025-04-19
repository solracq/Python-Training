from collections import deque
from queue_new import Queue

def queue_list(queue:list):
    queue.append('f')
    print(queue)
    queue.pop(0)
    print(queue)
    queue.pop(0)
    print(queue)
# Execution
queue = ['a', 'b', 'c', 'd', 'e']
queue_list(queue)
print()

def queue_deque(arr:list):
    queue = deque(arr)
    print(queue)
    queue.append('f')
    print(queue)
    queue.popleft()
    print(queue)
    queue.popleft()
    print(queue)
# Execution
arr = ['a', 'b', 'c', 'd', 'e']
queue_deque(arr)
print()

def queueing():
    queue = Queue(maxsize=4)
    print(f"Maxium size of the queue is : {queue.qsize()}")
    print(f"Empty? {queue.empty()}")
    queue.put('a')
    queue.put('b')
    queue.put('c')
    print(f"Full? {queue.full()}")
    print(f"size? {queue.qsize()}")
    queue.put('d')
    print(f"Empty? {queue.empty()}")
    print(f"Full? {queue.full()}")
    print(f"size? {queue.qsize()}")
    print(f"Removing item for the queue? {queue.get()}")
    print(f"Removing item for the queue? {queue.get()}")

# Execution
print(queueing())

