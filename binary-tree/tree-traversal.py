
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_tree(node):
    # print(node.data) # - preorder (1,2,4,5,3,6,7)
    if node.left: print_tree(node.left)
    # print(node.data) # - inorder (4,2,5,1,6,3,7)
    if node.right: print_tree(node.right)
    print(node.data) # - postorder (4,5,2,6,7,3,1)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print_tree(root)


