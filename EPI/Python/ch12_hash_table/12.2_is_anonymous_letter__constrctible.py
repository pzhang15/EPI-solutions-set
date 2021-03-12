import collections
'''
given a string(letter) and a text, see if you can construrct this snippet 
by using any but not more characters in the text

LC 383. Ransom Note
'''

#pythonic
def sol(s, t):
    els = not collections.Counter(s)
    print()
    return not (collections.Counter(s) - collections.Counter(t))
s = "aa"
t = "aa"
res= sol(s, t)

print(res)