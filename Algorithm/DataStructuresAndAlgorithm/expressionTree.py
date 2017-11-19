# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def creation(str):
    List=[]
    for i in str:
        if i.isalpha():
            node = TreeNode(i)
            List.append(node)
        else:
            node = TreeNode(i)
            print(List[-1].val)
            print(List[-2].val)
            node.left = List[-2]
            node.right = List[-1]
            List.pop(-1)
            List.pop(-1)
            List.append(node)
    return List[0]
