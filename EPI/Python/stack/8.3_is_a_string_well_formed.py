'''
valid parentheses:
well-formed:
    ([]){()} is well-formed
    [()[]{()}] is well-formed
    {abc}()
Not well-formed:
    {(})
    [


'''
def sol(s):
    T = {')': '(' , ']':'[' ,'}' :'{'}
    stack = []
    for c in s:
        if c in T:
            if len(stack) == 0 or stack.pop() != T[c]:
                return False
        elif c in['([{']:
            stack.push(c)
    return len(stack) == 0

    