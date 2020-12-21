'''
Given a refernce to a single node, delete it in O(1)
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
#seems impossible right? cause the previous node's next pointer needs to be updates
#but we can do this:

def deletion_from_list(node):
    node.data = node.next.data
    node.next = node.next.next