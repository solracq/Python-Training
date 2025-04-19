
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def push(self, data):
        node = Node(data)
        # temp = self.head
        # self.head = node
        # node.next = temp
        node.next = self.head
        self.head = node

    def insert(self, prev_node, data):
        if prev_node:
            node = Node(data)
            node.next = prev_node.next
            prev_node.next = node
        else:
            print(f"{prev_node} doesn't exist in the linked list")

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node

    def remove_left(self):
        if self.head is None:
            print("Nothing to remove!")
            return
        first = self.head
        while first.next:
            second = first.next
            self.head = second
            break

    def remove_right(self):
        if self.head is None:
            print("Nothing to remove!")
            return
        last = self.head
        while last.next:
            previous_last = last
            last = last.next
            if last.next is None:
                previous_last.next = None

    def remove_middle(self, data):
        if self.head is None:
            print("Nothing to remove!")
            return
        middle = self.head
        while middle.next:
            previous_node = middle
            middle = middle.next
            if middle.data == data:
                previous_node.next = middle.next

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node(2)

    node2 = Node(3)
    node3 = Node(4)

    linked_list.head.next = node2
    node2.next = node3
    linked_list.print_list()
    print()
    linked_list.push(1)
    linked_list.print_list()
    print()
    linked_list.insert(node2, 8)
    linked_list.print_list()
    print()
    linked_list.add(9)
    linked_list.print_list()
    print()
    linked_list.remove_left()
    linked_list.print_list()
    print()
    linked_list.remove_right()
    linked_list.print_list()
    print()
    linked_list.remove_middle(8)
    linked_list.print_list()
    print()
