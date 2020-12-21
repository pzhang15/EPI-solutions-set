import functools
'''
given two string s(search string) and t (text), find the first occurence of s in t
'''
def sol(s, t):
    if len(s) > len(t):
        return -1
    base = 26
    t_hash = functools.reduce(lambda h, c: h * base + ord(c), t[:len(s)],0)
    s_hash = functools.reduce(lambda h, c: h * base + ord(c), s, 0)

    power_s = base ** max(len(s) - 1, 0) # to access the most significant digit later
    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s): i] == s: #因为是sum， 所以有的时候会出现sum相同但实际字母不同的情况
            return i - len(s)
        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * 26 + ord(t[i])

    if t_hash == s_hash and t[i - len(s):] == s:
            return len(t) - len(s)
    return -1