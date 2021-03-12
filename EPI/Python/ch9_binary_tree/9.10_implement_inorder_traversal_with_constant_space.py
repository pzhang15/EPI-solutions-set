'''
given a binary tree with parent pointers, implement in order traversal with constant space
'''
def sol(root):
    prev = None
    res = []
    while root:
        if prev is root.parent:
            if root.left:
                next = root.left
            elif root.right:
                res.append(root.val)
                next = root.right or root.parent
                
        elif prev is root.left: #如果我们走完了左边
            next = root.right or root.parent
        else:
            next = root.parent #左右两边都走完
        prev = root
        root = next
    return res
    
        
            
            

        