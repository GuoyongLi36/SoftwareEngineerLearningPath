import random

class TreeNode:
	def __init__(self, x, parent = None):
		self.val = x
		self.left = None
		self.right = None
		self.leftNodes = 0
		self.rightNodes = 0
		self.height = 0
		self.parent = parent

class AVLtree:
	def __init__(self):
		self.root = None
	
	def insertValue(self, x):
		if self.root == None:
			self.root = TreeNode(x)
		else: self.insertIntoTree(x, self.root)
	
	def insertIntoTree(self, x, node):
		if node.val > x:
			if node.left != None:
				self.insertIntoTree(x, node.left)
			else:
				node.left = TreeNode(x, node)
		else:
			if node.right !=None:
				self.insertIntoTree(x, node.right)
			else:
				node.right = TreeNode(x, node) 
		self.balance(node)

	def balance(self, node):
		if node == None:
			return
		heightDiff = self.height(node.left) - self.height(node.right)
		if  heightDiff>= 2:
			if (self.height(node.left.left) > self.height(node.left.right)):
				self.rotateLeftNode(node)
			else:
				self.rotateRightLeftNode(node)
		elif heightDiff <=-2:
			if (self.height(node.right.right) > self.height(node.right.left)):
				self.rotateRightNode(node)
			else:
				self.rotateLeftRightNode(node)
		node.height = max(self.height(node.left), self.height(node.right)) + 1


	def rotateLeftNode(self, k1):
		k2 = k1.left
		k1.left = k2.right
		if k2.right != None:
			k2.right.parent = k1
		k1.left = k2.right
		k2.right = k1
		root = k1.parent
		k1.parent = k2
		k2.parent = root
		if root == None:
			self.root = k2
		else:
			if root.val >k2.val:
				root.left = k2
			else:
				root.right = k2
		k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
		k2.height = max(self.height(k2.left), self.height(k2.right)) + 1

	def rotateRightNode(self, k1):
		k2 = k1.right
		k1.right = k2.left
		if k2.left != None:
			k2.left.parent = k1
		k1.right = k2.left
		k2.left = k1
		root = k1.parent
		k1.parent = k2
		k2.parent = root
		if root == None:
			self.root = k2
		else:
			if root.val >k2.val:
				root.left = k2
			else:
				root.right = k2
		
		k1.height = max(self.height(k1.left), self.height(k1.right)) + 1
		k2.height = max(self.height(k2.left), self.height(k2.right)) + 1		

	def rotateRightLeftNode(self, k1):
		self.rotateRightNode(k1.left)
		self.rotateLeftNode(k1)

	def rotateLeftRightNode(self, k1):
		self.rotateLeftNode(k1.right)
		self.rotateRightNode(k1)

	def height(self, node):
		if node == None:
			return -1
		else:
			return node.height

	def show(self, node):
		if node == "root":
			node = self.root
		if node == None:
			print("[]", end = '')
			return
		print(node.val, "(", node.height, ")", ":[", end = "")
		self.show(node.left)
		self.show(node.right)
		print ("]", end = "")

def certifyAVLtree(node):
	if node == None:
		return True, -1
	result, leftHeight = certifyAVLtree(node.left)
	if result == False:
		return False, 0
	result, rightHeight = certifyAVLtree(node.right)
	if result == False:
		return False, 0
	if abs(leftHeight - rightHeight) <2:
		return True, max(leftHeight + 1, rightHeight + 1)
	else:
		return False, -1

	



if __name__ == '__main__':
	items = [x for x in range(0,100)]
	print(items)
	random.shuffle(items)
	a = AVLtree()
	for i in items:
		a.insertValue(i)
	a.show("root")
	result, height = certifyAVLtree(a.root)
	print(result, height)














