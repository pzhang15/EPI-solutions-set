'''
As title, level order traversal LC 102
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def sol(root):
    result = []
    if not root:
        return result
    q = [root]
    while q:
        result.append([node.val for node in q])
        q = [
            child 
            for node in q
            for child in (node.left, node.right) if child
        ]
    return result