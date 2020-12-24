'''
Given a path name: 'src/./../tc/aws/././', return the shortest absolute path:
src/tc/awk
'''
#LC 71
def sol(path):
    stack = []
    elemts = path.split('/')
    for e in elemts:
        if e == '..':
            if stack:
                stack.pop()
        elif e in ['.', '']:
            continue
        else:
            stack.append(e)
    print(stack)
    
    return '/' + '/'.join(stack)
l = ['a']
print('/'.join(l))