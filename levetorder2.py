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
    root.right = Node(5)
    root.left.right = Node(4)
    root.left.left = Node(3)
    root.left.right.left = Node(9)
    root.left.right.left.right = Node(10)
    root.left.right.left.right.left= Node(14)
    root.right.right=Node(6)
    root.right.right.left=Node(7)
    root.right.right.right=Node(8)
    root.right.right.left.right=Node(11)
    root.right.right.left.right.left=Node(12)
    root.right.right.left.right.left.right=Node(13)
    
    
    
    
    levelorder(root)
