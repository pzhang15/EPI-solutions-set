'''
e.g Give a string 'Hello World'
1:   e              _               l   
2: H    l       o       W       r       d
3:          l               o               !

return [
        [e_l],
        [hloWrd],
        [lo!]
]
'''
def sol(s):
    result = []
    n = len(s)
    for i in range(1, n, 4):
        result.append(s[i])
    for i in range(0, n, 2):
        result.append(s[i])
    for i in range(3, n, 4):
        result.append(s[i])
    return result
s = 'Hello World!'
res = sol(s)
print(res)
    