'''
Given an integer and a binary tree with integeter node weights, 
and check if there exists a leaf whose path weight equal the given integer
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sol(target, root):
    if not root:
        return False
    if not root.left or root.right:
        return root.val == target
    return sol(root.left, target - root.val) or sol(root.right, target - root.val)
    
