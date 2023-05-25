from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def bfs(root):
    if root is None:
        return
    q = Queue()
    q.put(root)
    while not q.empty():
        currNode = q.get()
        print("\t", currNode.data, end="")
        if currNode.left:
            q.put(currNode.left)
        if currNode.right:
            q.put(currNode.right)

root = None
ans = 'y'
while ans == 'y' or ans == 'Y':
    data = int(input("\n enter data=>"))
    root = insert(root, data)
    ans = input("do you want insert one more node?")
bfs(root)
