'''
Given a singly linkedlist, and a nonnegative integer k, 
and returns the list cyclically to the right by k

''' 
#LC 61
def sol(head, k):
    if not head:
        return head
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head
    for _ in range(n - k):
        tail = tail.next
    new_head = tail.next
    tail.next = None
    return new_head


    