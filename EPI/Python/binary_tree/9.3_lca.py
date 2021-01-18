'''
LC 236
'''
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        Status = collections.namedtuple('Status', ('num', 'ancestor'))
        def recur(root, p, q):
            if not root:
                return Status(num=0, ancestor=None)
            left_result = recur(root.left, q, p)
            if left_result.num == 2:
                return left_result
            
            right_result = recur(root.right, q, p)
            if right_result.num == 2:
                return right_result
            
            num_target = left_result.num + right_result.num + (p, q).count(root)
            
            return Status(num_target, root if num_target == 2 else None)
        return recur(root, p, q).ancestor