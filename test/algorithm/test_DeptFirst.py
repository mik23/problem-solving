from unittest import TestCase

from binarytrees.algorithm.DeptFirst import preOrderTraversing
from binarytrees.algorithm.DeptFirst import postOrderTraversing
from binarytrees.algorithm.DeptFirst import inOrderTraversing
from binarytrees.data.Tree import Tree

# 1
# 2      3
# 4 5   6 7
#           1


seven = Tree(7)
six = Tree(6)
three = Tree(3, six, seven)
uno = Tree(1)
four = Tree(4)
five = Tree(5)
two = Tree(2, four, five)
tree = Tree(1, two, three)


class Test(TestCase):
    def test_pre_order_traversing(self):
        result = list()
        preOrderTraversing(tree, result)
        self.assertEqual(result, [1, 2, 4, 5, 3, 6, 7])

    def test_post_order_traversing(self):
        result = list()
        postOrderTraversing(tree, result)
        self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

    def test_in_order_traversing(self):
        result = list()
        inOrderTraversing(tree, result)
        self.assertEqual(result, [4, 2, 5, 1, 6, 3, 7])

