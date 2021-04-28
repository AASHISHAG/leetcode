class Trie:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.is_word = False


def insert(root, word):

    for ch in word:
        found_in_child = False
        for child in root.children:
            if ch == child.val:
                root = child
                found_in_child = True
                break
        if not found_in_child:
            node = Trie(ch)
            root.children.append(node)
            root = node

    root.is_word = True


def find_prefix(root, word):

    for ch in word:
        found = False
        for child in root.children:
            if ch == child.val:
                root = child
                found = True
                break
        if not found:
            return False
    return True



def print_prefix(root):

    while len(root.children) == 1 and not root.is_word:
        root = root.children[0]
        print(root.val)

if __name__ == '__main__':
    root = Trie('#')
    insert(root, "aashish")
    insert(root, "aankita")

    print_prefix(root)
    print(find_prefix(root, "aaszh"))