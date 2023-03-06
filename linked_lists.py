class Node:

    def __init__(self, data):
        self.data = data
        self.nextval = None

class Llist:
    def __init__(self):
        self.headval = None

 
    def printList(self):
        printval = list1.headval

        list2 = []
        while printval:
            list2.append(printval.data)
            printval = printval.nextval
        return list2


        
list1 = Llist()
list1.headval = Node('Mon')
v1 = Node('Tue')
V2 = Node('Wed')

list1.headval.nextval = v1
v1.nextval = V2

print (list1.printList())