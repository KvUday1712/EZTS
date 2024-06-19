class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

def levelorder(root):
    if not root:
        return
    q = [root]
    while q:
        curr = q.pop(0)
        print(curr.value, end=' ')
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
    print()

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    root.right.left = Node(6)
    root.right.left.right = Node(9)
    
    levelorder(root)
