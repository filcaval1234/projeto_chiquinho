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

    def busca(self, key, root = -1):
        if root == -1:
            root = self.root
        if root is not None:
            if key == root.key:
                return root.data
            esq = self.busca(key, root.left)
            dir = self.busca(key, root.right)
            if esq is not None:
                return esq
            elif dir is not None:
                return dir
        return None

    def remove(self, key, root=-1):
        if root == -1:
            self.root = self.remove(key, self.root)
            return
        if root is not None:
            if key > root.key:
                root.right = self.remove(key, root.right)
            elif key < root.key:
                root.left = self.remove(key, root.left)

            if root.key == key:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    root.key, root.data = self.menorSucessor(root.key, root.data, root.right)
                    root.right = self.remove(key, root.right)
            return root

    def menorSucessor(self, key, data, root=-1):
        if root == -1:
            return self.menorSucessor(key, root=self.root)
        if root is not None:
            if root.left is not None:
                return self.menorSucessor(key, root.left)
            else:
                key1 = root.key
                data1 = root.data
                root.key = key
                root.data = data
                return key1, data1

    def imprimir(self, lista, root = -1):
        if root == -1:
            root = self.root
        if root is not None:
            self.imprimir(lista, root.left)
            lista.append(root.data)
            self.imprimir(lista, root.right)

class TreeNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None