
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
    
    '''
    1. Post order traversal
    '''
    '''
    if not root: return
    if root.left: self.invertTree(root.left)
    if root.right: self.invertTree(root.right)
    root.left, root.right = root.right, root.left
    return root
    '''

    '''
    2. DFS
    '''

    '''
    if root is None: return
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
        node.left, node.right = node.right, node.left
    return root
    '''

    '''
    3. BFS / Level order traversal
    '''
        
    '''
    if root is None: return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
        node.left, node.right = node.right, node.left
    return root
    '''


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print_tree(root)


