class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = Node(data)
                        break
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = Node(data)
                        break
                    else:
                        current = current.right


    def pre_order_traverse(self, node):
        if node is not None:
            print(node.data)
            self.pre_order_traverse(node.left)
            self.pre_order_traverse(node.right)

    def find_longest(self):
        current = self.root
        longest = current.data
        while current:
            if len(str(current.data))>len(str(longest)):
                longest = current.data
            current = self.pre_order_traverse(current.left) or self.pre_order_traverse(current.right)
        return longest

    def find_shortest(self):
        current = self.root
        shortest = current.data
        while current:
            if len(str(current.data))<len(str(shortest)):
                shortest = current.data
            current = self.pre_order_traverse(current.left) or self.pre_order_traverse(current.right)
        return shortest

tree = Tree()

tree.create(6)
tree.create(1)
tree.create(63)
tree.create(4)
tree.create(60)
tree.create(96)
tree.pre_order_traverse(tree.root)