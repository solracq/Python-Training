class StackNew:
    def __init__(self):
        self._items = list()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def len(self):
        return len(self._items)

    def print(self):
        print(self._items)
