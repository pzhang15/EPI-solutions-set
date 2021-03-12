'''
LC 94
Given a tree, return the inorder traversal result as a list
思考如何避免zig zag的情况
比如 
    1
   / \ 
  2   6
   \
    3 
     \
      4
     /
    5  
'''
def sol(root):
    res, stack = [], []
    #stack只负责存左边，
    #cur负责在第一次遍历之后储存右子树的root
    cur = root
    while cur or stack: 
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right #这招挺厉害的， 直接换cur指针的位置然后利用下一个while循环做同样的事情
    return res
