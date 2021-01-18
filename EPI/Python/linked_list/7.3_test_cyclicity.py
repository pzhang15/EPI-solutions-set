'''
LC141, LC142 finished
'''
class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

def detectCycle(head: Node) -> Node:
    if not head:
        return None
    slow, fast = head, head.next
    while fast and fast.next:
        if fast is slow:
            break
        fast = fast.next.next
        slow = slow.next
    
    if not fast:
        return None
    print(fast.data)
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)
l1.next.next.next.next.next = Node(6)
l1.next.next.next.next.next.next = Node(3)


res = detectCycle(l1)
