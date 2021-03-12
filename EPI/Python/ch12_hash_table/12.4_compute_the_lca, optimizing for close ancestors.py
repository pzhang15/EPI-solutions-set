'''
Given two node in a binary tree, each node has a reference to their parent, 
design an algorithm that compute their LCA
Optimize it with hashmap
'''
def lca(node0, node1):
    p1, p2 = node0, node1
    visited = set()
    while p1 or p2:
        if p1:
            p1 = p1.parent
            if p1 in visited:
                return p2
            visited.add(p1)
        if p2:
            p2 = p2.parent
            if p2 in visited:
                return p2
            visited.add(p2)



