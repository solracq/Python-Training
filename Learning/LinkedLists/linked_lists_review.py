#ref: https://www.geeksforgeeks.org/singly-linked-list-tutorial/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def transverse(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse_transverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.previous
        print()

    def print_list(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()

    def reverse_list(self, head):
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Store next
            curr.next = prev  # Reverse current node's next pointer
            prev = curr  # Movie pointers one position ahead
            curr = next_node
        return prev  # Return the head of reversed linked list

    def push(self, data): # Pushed a new node to the beginning of a linked list
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert(self, data, previous): # Insert new node to any point of the linked list when previous node is known
        if not previous:
            print(f"{previous} node doesn't exist in the linked list")
        node = Node(data)
        node.next = previous.next
        previous.next = node
        #node.next = None

    def insert_position(self, pos, data): # Insert new node to the specified position
        node = Node(data)

        if self.head is None:
            print("Linked list is empty!")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            node.next = self.head
            self.head = node
        else:
            count = 1
            prev = self.head
            while count < pos-1 and prev is not None:
                prev = prev.next
                count += 1
            node.next = prev.next
            prev.next = node

    def add(self, data): # Add a new node to the end of the linked list when no previous node is known
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        node.next = None

    def remove_left(self):
        if self.head:
            self.head = self.head.next
            self.head.next = self.head.next.next
        else:
            print("linked list is empty, no node to be removed!")

    def remove_right(self):
        if self.head is None:
            print("linked list is empty, no node to be removed!")
            return
        last = self.head
        prev = None
        while last.next:
            prev = last
            last = last.next
        prev.next = None

    def remove_middle(self, data):
        if self.head is None:
            print("Linked list is empty!")
            return
        middle = self.head
        while middle.next:
            prev = middle
            middle = middle.next
            if middle.data == data:
                prev.next = middle.next

    def remove_at_position(self, pos):
        if self.head is None:
            print("Linked list is empty")
            return
        if pos == 1:
            self.head = self.head.next
            self.head.next = self.head.next.next
        else:
            count = 1
            prev = self.head
            while count < pos-1 and prev is not None:
                prev = prev.next
                count += 1
            prev = prev.next
            prev.next = prev.next.next

    def find_node(self, data):
        if self.head is None:
            print("Linked list is empty!")
            return
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next

    def size(self):
        if self.head is None:
            print("Linked list is empty!")
            return
        size = 0
        temp = self.head
        while temp.next:
            size += 1
            temp = temp.next
        return size


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    linked_list.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    linked_list.transverse()

    linked_list.tail = node5
    node5.previous = node4
    node4.previous = node3
    node3.previous = node2
    node2.previous = linked_list.head
    linked_list.reverse_transverse() # print linked list from tail
    reversed_head = linked_list.reverse_list(linked_list.head) # Actually reversing the list
    linked_list.print_list(reversed_head)  # Printing linked list using the head

    # Reverse Linked lists
    ll = LinkedList()
    ll.head = Node(6)
    ll.head.next = Node(7)
    ll.head.next.next = Node(8)
    ll.head.next.next.next = Node(9)
    ll.head.next.next.next.next = Node(10)
    ll.transverse()
    reversed_head = ll.reverse_list(ll.head)
    ll.print_list(reversed_head)

    # Push and Insert
    ll2 = LinkedList()
    ll2.head = Node(11)
    node2 = Node(12)
    node3 = Node(13)
    node4 = Node(14)
    node5 = Node(15)
    ll2.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    ll2.print_list(ll2.head)
    ll2.push(10)
    ll2.print_list(ll2.head)
    ll2.insert(16, node5)
    ll2.print_list(ll2.head)
    ll2.insert(3, node3)
    ll2.print_list(ll2.head)
    ll2.add(20)
    ll2.print_list(ll2.head)
    ll2.remove_left()
    ll2.print_list(ll2.head)
    ll2.remove_right()
    ll2.print_list(ll2.head)
    ll2.remove_middle(3)
    ll2.print_list(ll2.head)
    data = 15
    found = ll2.find_node(data)
    print(f"is {data} in linked list? {found}")
    data = 1
    found = ll2.find_node(data)
    print(f"is {data} in linked list? {found}")
    size = ll2.size()
    print(f"The size is the linked list is {size}")
    ll2.insert_position(1, 45)
    ll2.print_list(ll2.head)
    ll2.insert_position(3, 33)
    ll2.print_list(ll2.head)
    ll2.remove_at_position(1)
    ll2.print_list(ll2.head)
    ll2.remove_at_position(2)
    ll2.print_list(ll2.head)