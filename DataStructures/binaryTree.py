class BinaryTree:
    def __init__(self, data_val):
        self.data_val = data_val
        self.right = None
        self.left = None

    def insert(self, data_val):
        if self.data_val:
            if data_val < self.data_val:
                if self.left is not None:
                    self.left.insert(data_val)
                else:
                    self.left = BinaryTree(data_val)
            else:
                if self.right is not None:
                    self.right.insert(data_val)
                else:
                    self.right = BinaryTree(data_val)
        else:
            self.data_val = data_val

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data_val)
        if self.right:
            self.right.print_tree()

