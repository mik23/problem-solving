class BSTree:
	def __init__(self, data: int, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right
	
	def insert(self, data):
		if self.data == data:
			return
		if self.data is None:
			self.data = data
			return
		if data < self.data:
			if self.left is None:
				self.left = BSTree(data)
			else:
				self.left.insert(data)
		else:
			if self.right is None:
				self.right = BSTree(data)
			else:
				self.right.insert(data)

	def preOrderTraversing(self):
		if self is None:
			return
		if self.data is not None:
			print(self.data)
		if self.left:
			self.left.preOrderTraversing()
		if self.right:
			self.right.preOrderTraversing()

	def search(self, data):
		if self.data == data:
			return True
		if data < self.data and self.left is not None:
			return self.left.search(data)
		elif data < self.data and self.right is not None:
			return self.right.search(data)
		return False