# assume no duplicated val inserted into tree
import random

class TreeNode:
	def __init__(self, val, parent = None):
		self.val = val
		self.left = None
		self.right = None
		self.parent = parent


class BuildSplayTree:
	def __init__(self):
		self.root = None

	def insertValue(self, val):
		if self.root == None:
			self.root = TreeNode(val)
		else:
			root = TreeNode(val)
			if self.root.val > val:
				root.right = self.root
			else:
				root.left = self.root
			self.root.parent = root
			self.root = root

	def access(self, val):
		if val == self.root.val:
			return True
		node = self.root
		while node != None:
			if node.val > val:
				node = node.left
			elif node.val < val:
				node = node.right
			else:
				while node != self.root:
					self.balance(node)
				break
		if self.root.val != val:
			return False
		return True

	def balance(self, Node):
		self.show("root")
		print("doing balance Node = ", Node.val)
		if Node.parent == self.root:
			self.leftRotate(self.root)
			return
		parent = Node.parent
		grandparent = parent.parent
		if grandparent.val > parent.val:
			print("seea")
			if parent.val > Node.val:
				print("seea1")
				print(Node.val, parent.val)
				self.leftRotate(parent)
				print("seea3")
				self.leftRotate(grandparent)
			else:
				print("seea2")
				self.leftRotate(parent)
				self.rightRotate(grandparent)
		else:
			print("seeb")
			if parent.val < Node.val:
				self.rightRotate(parent)
				self.rightRotate(grandparent)
			else:
				self.rightRotate(parent)
				self.leftRotate(grandparent)

	def leftRotate(self, Node):
		child = Node.left
		if child.right != None:
			child.right.parent = Node
			Node.left = child.right
		parent = Node.parent
		child.right = Node
		Node.parent = child
		child.parent = parent
		if parent != None:
			if parent.val > child.val:
				parent.left = child
			else:
				parent.right = child

	def rightRotate(self, Node):
		print("Node value is ", Node.val)
		print("Node left val is", Node.left.val)
		child = Node.right

		if child.left != None:
			child.left.parent = Node
			Node.left = child.right
		parent = Node.parent
		child.left = Node
		Node.parent = child
		child.parent = parent
		if parent != None:
			if parent.val > child.val:
				parent.left = child
			else:
				parent.right = child

	def show(self, node):
		if node == "root":
			node = self.root
		if node == None:
			print("[]", end = '')
			return
		print(node.val, ":[", end = "")
		self.show(node.left)
		self.show(node.right)

if __name__ == '__main__':
	items = [68, 90, 23, 30, 9, 32, 4, 72, 38, 64, 97, 25, 35, 26, 87, 16, 84, 61, 18, 11, 44, 27, 65, 52, 13, 28, 59, 15, 55, 53, 60, 67, 62, 92, 0, 33, 99, 63, 29, 40, 6, 46, 12, 58, 5, 79, 83, 74, 49, 88, 66, 37, 8, 24, 57, 96, 91, 81, 56, 7, 85, 2, 17, 31, 93, 73, 69, 89, 42, 1, 78, 82, 77, 39, 41, 80, 19, 21, 20, 3, 76, 95, 43, 47, 54, 22, 71, 14, 86, 98, 36, 70, 45, 75, 10, 48, 94, 34, 50, 51]
	#random.shuffle(items)
	print(items)
	a = BuildSplayTree()
	for i in items:
		a.insertValue(i)

	a.show("root")
	for i in range(0, 100):
		print()
		print("trying to find", i)
		a.access(i)
		a.show("root")






