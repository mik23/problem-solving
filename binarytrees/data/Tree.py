class Tree:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def isEqual(self, T):

        if self.data is None and T.data is not None:
            return False

        if self is None and T is None:
            return True

        if self.isEqual(self.left, T.left) and self.isEqual(self.right, T.right):
            return True







