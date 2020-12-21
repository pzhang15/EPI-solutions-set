'''
Add two list based integer:
given l1 and l2 represent two integers, they might have different length

In both lists, least significant digit come first
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
def sol(l1, l2):
    dummy = itr = Node()
    carry = 0
    while l1 or l2 or carry:
        val = carry + (l1.data if l1 else 0) + (l2.data if l2 else 0)
        
        itr.next = Node(val%10)
        itr = itr.next
        carry = val //10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next

        
