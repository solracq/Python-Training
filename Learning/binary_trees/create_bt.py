#        1
#       / \
#      2   3
#     / \ / \
#    4  None None
#   /  \
# None None
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def print_ltree(self):
        temp = self.left
        while temp:
            print(temp.val, end=" ")
            temp = temp.left

    def print_rtree(self):
        temp = self.right
        while temp:
            print(temp.val, end=" ")
            temp = temp.right

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    root.print_ltree()
    print()
    root.print_rtree()