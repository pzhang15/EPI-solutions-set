'''
<1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211>
'''
def look_and_say(n):
    def next_number(s):
        res = []
        i = 0
        while(i < len(s)):
            cnt = 1 #make up for the last one
            while(i + 1 < len(s) and s[i] == s[i + 1]):
                cnt += 1
                i += 1
            res.append(str(cnt) + s[i])
            i += 1
            
        return ''.join(res)

    s = '1'
    for i in range(n):
        s = next_number(s)
    return s
n = 6
s = look_and_say(n)
print(s)