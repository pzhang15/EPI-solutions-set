'''
Test weather a singly linkedlist is palindromic in O(N)
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
#LC 234
def reverse(l, prev_given):
    prev = prev_given
    curr = l
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

def sol(l):
    def reverse_list(l):
        prev = None
        curr = l
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        
    slow = fast = l
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    print(slow.data)
    first_itr, sec_itr = l, reverse_list(slow)
    print(sec_itr.data)
    while l:
        print(l.data)
        l = l.next
    while first_itr and sec_itr:
        if first_itr.val != sec_itr.val:
            return False
        first_itr, sec_itr = first_itr.next, sec_itr.next
    return True    

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)
l1.next.next.next.next.next = Node(6)
l1.next.next.next.next.next.next = Node(7)
  

sol(l1)