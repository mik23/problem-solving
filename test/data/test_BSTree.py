from unittest import TestCase
from binarytrees.data.BSTree import BSTree

class Test(TestCase):
    def setUp(self):
        #     4
        # 1			5
        #   3 
        self.tree = BSTree(4)
        self.tree.insert(1)
        self.tree.insert(3)
        self.tree.insert(5)

    def test_insertBSTree(self):
        self.assertEqual(self.tree.left.right.data, 3)

    def test_searchFoundBSTree(self):
        self.assertTrue(self.tree.search(1))

    def test_searchNotFoundBSTree(self):
        self.assertFalse(self.tree.search(23))