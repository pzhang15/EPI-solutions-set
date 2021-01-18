'''
9.15
LC 116
'''




def connect(self, root: 'Node') -> 'Node':
#making level order connection, left to right
    def helper(cur):
        while cur and cur.left:
            cur.left.next = cur.right
            cur.right.next = cur.next and cur.next.left
            cur = cur.next
    #traverse each level 
    p = root
    while p and p.left:
        helper(p)
        p = p.left
    return root