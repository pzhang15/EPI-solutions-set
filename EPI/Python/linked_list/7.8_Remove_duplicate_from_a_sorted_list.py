'''
given a sorted list contains duplicated, remove all duplicates, 
LC 83
'''  
def sol(l):
    p = l
    while p:
        while p.next and p.next.data == p.data:
            p.next = p.next.next
        p = p.next
    return l
