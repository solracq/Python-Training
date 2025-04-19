class QueueNew:
    def __init__(self):
        self._items = list()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if len(self._items) != 0:
            return self._items.pop(0)

    def size(self):
        if len(self._items) != 0:
            return len(self._items)
        else:
            return 0

    def print(self):
        print(self._items)

queue = QueueNew()
queue.push(1)
queue.push(2)
queue.push(3)
queue.print()
for i in range(queue.size()):
    queue.pop()
    queue.print()