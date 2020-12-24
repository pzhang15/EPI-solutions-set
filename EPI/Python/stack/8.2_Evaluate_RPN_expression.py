'''
Polish Notation:
(3 + 5) * (7 - 2)
Reverse Polish Notation:
3 5 + 7 2 - *
which is always can be reduce to:  A B o, 
whereas 'o' is used as a operator that applied to previous two numbers

Given a Reverse Plish Notation string, output the results

'''

def sol(s):
    elemts = s.split(',')
    stack  = []
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)
    }
    for e in elemts:
        if e in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[e](a, b))
        else:
            stack.append(int(e))
    return stack.pop()

s = "3,5,+,7,2,-,*"
res = sol(s)
print(res)

print(6/-132, 6 // -132)