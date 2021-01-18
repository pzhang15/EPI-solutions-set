from typing import *
'''
LC 110
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


        
def isBalanced(self, root: TreeNode) -> bool:
    #return (balancedStatus, height)
    def check_balance(root) -> (bool, int):
        if not root:
            return True, -1
        
        left_balance, left_height = check_balance(root.left)
        if not left_balance:
            return False, 0
        
        right_balance, right_height = check_balance(root.right)
        if not right_balance:
            return False, 0
        
        return (abs(right_height - left_height) <= 1), max(left_height, right_height) + 1

    return check_balance(root)[0]