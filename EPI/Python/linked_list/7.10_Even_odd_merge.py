'''
l0 -> l1 -> l2 -> l3 -> l4 -> None
re-order it to:
l0 -> l2 -> l4 -> l1 -> l3 -> None
Even nodes come first, then odd 
'''
#LC 328
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def sol(head):
    if not head:
        return head
    even, odd = ListNode(-1), ListNode(-1)
    tail, turn = [even, odd], 0
    while head:
        tail[turn].next = head
        head = head.next
        tail[turn] = tail[turn].next
        turn ^= 1
    tail[1].next = None
    tail[0].next = odd.next
    
    return even.next

    

