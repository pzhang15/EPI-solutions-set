'''
9.13
Given a binary tree, return the leaves of the binary tree, the leaves hould appear in left to right order
'''

def sol(root):
    res = []
    def recur(root):
        if not root:
            return
        recur(root.left)
        if not root.left and not root.right:
            res.append(root.val)
        recur(root.right)
    recur(root)
    return res