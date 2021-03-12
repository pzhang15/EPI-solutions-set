'''
LC101

'''

def sol(root):
    def check_symm(sub_tree1, sub_tree2):
            if not sub_tree1 and not sub_tree2:
                return True
            if sub_tree1 and sub_tree2:
                return (sub_tree1.val == sub_tree2.val 
                        and check_symm(sub_tree1.right, sub_tree2.left) 
                        and check_symm(sub_tree1.left, sub_tree2.right) 
                       )
            return False
    return not root or check_symm(root.left, root.right)