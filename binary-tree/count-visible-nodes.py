# https://www.geeksforgeeks.org/count-the-number-of-visible-nodes-in-binary-tree/
# microsoft codility

import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

count = 0

# recurssion
# Time Complexity: O(N) where N is a number of nodes in the BT 
# Space Complexity: O(1)
def count_visible_nodes(node, mx):
    global count
    if node.data > mx:
        count += 1
        mx = max(node.data, mx)
    if node.left: count_visible_nodes(node.left, mx)
    if node.right: count_visible_nodes(node.right, mx)
    

if __name__ == '__main__':

    """
          5
        /  \
       3   10
      / \   /
    20   21 1
    """
    # creating BT
    root = Node(5)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(20)
    root.left.right = Node(21)
    root.right.left = Node(1)
    
    # counting visible nodes
    count_visible_nodes(root, -sys.maxsize)
    print(count)