'''
Given tree that each node contains the number of node that node contains in its subtree
compute the kth node appearing in an inorder traversal in less than O(N) time

'''
def kth_inroder(root, k):
    while root:
        left_size = root.left.size if root.left else 0
        if left_size + 1 < k: #has to be in the right sub_tre
            k -= left_size + 1
            root = root.right
        elif left_size + 1 == k:
            return root
        else:
            tree = tree.left
    return None



