'''
RLE encoding:
aaaabcccaa -> 4a1b3c2a
implement both encoding and decoding
'''
def decoding(s):
    res = []
    i,n = 0,len(s)
    cnt = 0
    for c in s:
        if c.isdigit():
            cnt = cnt * 10 + int(c)
        else:
            res.append(cnt * c)
            cnt = 0
    return ''.join(res)

def encoding(s):
    res = []
    n = len(s)
    cnt = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            cnt += 1
        else:
            res.append(str(cnt))
            res.append(s[i])
            cnt = 1
    
    res.append(str(cnt) + s[n - 1])
    return ''.join(res)

s = 'aaaabcccab'
enc = encoding(s)
dec = decoding(enc)
print(enc)
print(dec)
