'''
given two linkedlist, there is a shared node, find that node
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def overlapping(l1, l2):
    def length(l):
        cnt = 0
        while l:
            cnt += 1
            l = l.next
        return cnt
    l1_len = length(l1)
    l2_len = length(l2)
    #make sure l1 is the longer one
    if l2_len > l1_len:
        l1, l2 = l2, l1
    
    for _ in range(abs(l2_len - l1_len)):
        l1 = l1.next

    while l1 and l2 and l1 is not l2:
        l1 = l1.next
        l2 = l2.next
    return l1

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
common = Node(4)
l1.next.next.next = common
l1.next.next.next.next = Node(5)
l1.next.next.next.next.next = Node(6)
l1.next.next.next.next.next.next = Node(7)


l2 = Node(-1)
l2.next = Node(-2)
l2.next.next = Node(-3, common)

ret =overlapping(l1, l2)
print(ret.data)

    