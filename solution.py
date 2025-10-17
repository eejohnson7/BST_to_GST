'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        cum = 0
        def rev_inorder(node):
            nonlocal cum
            if not node:
                return
            rev_inorder(node.right)
            orig = node.data
            node.data = cum
            cum += orig
            rev_inorder(node.left)
        rev_inorder(root)
        return root
