from unittest import TestCase

from binarytrees.data.Tree import Tree
from binarytrees.algorithm.BreadthFirst import breadthFirst
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
    def test_breadth_first(self):
        result = list()
        breadthFirst(tree, result)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])