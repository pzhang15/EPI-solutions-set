'''
Given a singly linked list and an integer k, write a program to remove the kth last element from the list
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def remove_kth_last(l, k):
    p1 = p2 = l
    for _ in range(k):
        p1 = p1.next
    print('kth', p1.data)
    while p1:
        p1 = p1.next
        p2 = p2.next
    p2.next = p2.next.next

    return l

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)
l1.next.next.next.next.next = Node(6)
l1.next.next.next.next.next.next = Node(7)

ret = remove_kth_last(l1, 3)
p = ret
while p:
    print(p.data)
    p = p.next