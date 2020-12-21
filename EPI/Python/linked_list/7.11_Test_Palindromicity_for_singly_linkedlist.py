'''
Test weather a singly linkedlist is palindromic in O(N)
'''

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
        
    first_itr, sec_itr = l, reverse_list(slow)
    while first_itr and sec_itr:
        if first_itr.val != sec_itr.val:
            return False
        first_itr, sec_itr = first_itr.next, sec_itr.next
    return True      

