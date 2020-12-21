'''
LC 92
take a sinlgly linkedlist L and two integer s and f as arguemtns 
and reverse the order of the node from s to f, includisve, the number begin at 1
'''
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def reverse(l ,s , t):
    dummy = sub_head = Node(-1, l)
    for _ in range(s):
       sub_head = sub_head.next
    
    itr = sub_head.next
    for _ in range(s, t):
        temp = itr.next
        print(sub_head.data, itr.data, temp.data)
        itr.next, temp.next, sub_head.next = (temp.next, sub_head.next, temp)
    return dummy.next

l1 = Node(1)
l1.next = Node(2)
l1.next.next = Node(3)
l1.next.next.next = Node(4)
l1.next.next.next.next = Node(5)
l1.next.next.next.next.next = Node(6)
l1.next.next.next.next.next.next = Node(7)

p = l1
while(p):
    print(p.data, end='->')
    p = p.next
print()

ret = reverse(l1 ,2 , 5)
p = ret
while(p):
    print(p.data,end='->')
    p = p.next
print()

        
