class ABB:
    def __init__(self):
        self.root = None

    def insert(self, data, key, root = -1):
        if root == -1:
            self.root = self.insert(data, key, self.root)
            return
        if root is None:
            root = TreeNode(key, data)
        if root is not None:
            if key < root.key:
                root.left = self.insert(data, key, root.left)
            elif key > root.key:
                root.right = self.insert(data, key, root.right)
            return root

    def imprimir(self, root = -1):
        if root == -1:
            root = self.root
        if root is not None:
            self.imprimir(root.left)

class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
