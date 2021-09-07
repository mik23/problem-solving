from unittest import TestCase
from binarytrees.data.Tree import Tree

sub2 = Tree(2)
sub3 = Tree(3)
tree = Tree(1, sub2, sub3)
tree2 = Tree(1, sub2, sub3)

class TestTree(TestCase):
    def test_is_equal(self):
        self.assertEqual(tree, tree2)
