'''
Assuming each node has a reference to its parent, 

return a node's successor in an inorder traversal
'''

def sol(node):
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    while node.parent and node == node.parent.right:
        node = node.parent
    return node.parent
        
