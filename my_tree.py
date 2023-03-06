class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data>self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = Node(data)
                
    
    def inordertraversal(self, root):
        res = []
        if root:
            res = self.inordertraversal(root.left)
            res.append(root.data)
            res = res + self.inordertraversal(root.right)
        return res

    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res =res + self.preorder(root.left)
            res =res + self.preorder(root.right)

        return res

    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left )
            res = res + self.postorder(root.right)
            res.append(root.data) 
        return res

    def longestroot(self, root):
        leftr  = []
        rightr = []
        if root:
            leftr = leftr + self.inordertraversal(root.left)
            rightr = self.inordertraversal(root.right)
            if (len(leftr) <len(rightr)):
                return f'left root is the longest with {len(leftr)}'
            else:
               return  f'right root is the longest with {len(rightr)}'
            
    

root = Node(10)
root.insert(3)
root.insert(4)
root.insert(11)
print (root.longestroot(root))
