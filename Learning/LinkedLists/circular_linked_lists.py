
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(last):
    if last is None:
        return "List is empty!"

    head = last.next
    while head:
        print(head.data, end=" ")
        head = head.next
        if head == last.next:
            break
    print()

if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    last = Node(4)

    first.next = second
    second.next = third
    third.next = last
    last.next = first

    print_list(last)