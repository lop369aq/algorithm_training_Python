from collections import deque

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end = " ")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end = " ")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end = " ")

def levelorder(node):
    if not node:
        return

    queue = deque([node])

    while queue:
        current = queue.popleft()
        print(current.value, end = ' ')

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)