
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self, head1=None):
        if head1 is None:
            head1 = self.head
        temp = head1
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def print_list_reverse(self):
        temp = self.tail
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def find_lenght(self):
        count = 0
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
        return count

    def insert_head(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        else:
            node.next = self.head
            # self.head = node
            self.head.prev = node
        return node

    def insert_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def insert_position(self, pos, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        if pos < 1:
            return "Invalid position"
        if pos == 1:
            node.next = self.head
            self.head.prev = node
        else:
            count = 1
            curr = self.head
            while count < pos-1 and curr.next is not None:
                curr = curr.next
                count += 1
            next_node = curr.next
            node.prev = curr
            node.next = next_node
            curr.next = node

    def remove_head(self):
        if self.head is None:
            return "Nothing to remove, linked list is empty!"
        self.head = self.head.next
        self.head.next.prev = None

    def remove_tail(self):
        if self.head is None:
            return "Nothing to remove, linked list is empty!"
        last = self.head
        while last.next:
            last = last.next
        last.prev.next = None

    def remove_position(self, pos):
        if self.head is None:
            return "Nothing to remove, linked list is empty!"
        if pos < 1:
            return "Invalid position"
        if pos == 1:
            self.head = self.head.next
            self.head.next.prev = None
        else:
            count = 1
            curr = self.head
            while count < pos and curr.next is not None:
                curr = curr.next
                count += 1
            next_node = curr.next
            curr.prev.next = next_node
            next_node.prev = curr.prev


if __name__ == "__main__":
    ll = LinkedList()
    # Create nodes
    ll.head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    ll.tail = Node(5)
    # Create "next" connections btw nodes
    ll.head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = ll.tail
    ll.tail.next = None
    # Create "prev" connections btw nodes
    ll.tail.prev = node4
    node4.prev = node3
    node3.prev = node2
    node2.prev = ll.head
    # Transverse list
    ll.print_list()
    # Transverse Reverse list
    ll.print_list_reverse()
    len = ll.find_lenght()
    print(f"Linked list length is {len}")

    print("Removing node in position 3")
    ll.remove_position(3)
    ll.print_list()

    # inserting
    head = ll.insert_head(45)
    ll.print_list(head)
    ll.insert_tail(20)
    ll.print_list()
    ll.insert_position(4, 12)
    ll.print_list()
    # Removing
    ll.remove_head()
    ll.print_list()
    ll.remove_tail()
    ll.print_list()