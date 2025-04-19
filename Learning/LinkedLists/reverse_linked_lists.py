class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data, previous_node):
        node = Node(data)
        previous_node.next = node
        node.next = None

    def reverse_list(self, head): # https://www.geeksforgeeks.org/reverse-a-linked-list/
        prev = None
        curr = head
        while curr is not None:
            next_node = curr.next  # Store next
            curr.next = prev  # Reverse current node's next pointer
            prev = curr  # Movie pointers one position ahead
            curr = next_node
        return prev  # Return the head of reversed linked list

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def print_list2(self, node):
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    linked_list.head.next = node2
    node2.next = node3
    node3.next = None
    linked_list.print_list()

    reversed_head = linked_list.reverse_list(linked_list.head)
    linked_list.print_list2(reversed_head)

    # Push data to the head
    linked_list.push(5)
    linked_list.print_list()
    # Insert data to the tail
    linked_list.insert(4, node3)
    linked_list.print_list()

