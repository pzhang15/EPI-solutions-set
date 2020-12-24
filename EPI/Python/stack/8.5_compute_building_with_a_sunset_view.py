'''
Give a list of building, sunlight come from right, return all building that can view the sunlight

[2, 3, 4, 2, 1] -> [4, 2, 1] 
'''
def sol(l):
    stack = []
    for e in l:
        while stack and stack[-1] <= e:
            stack.pop()
        stack.append(e)
    return stack

buildings = [2, 3, 4, 2, 1]
print(sol(buildings))


 