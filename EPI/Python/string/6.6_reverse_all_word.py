'''
Give a string like 'Alice likes Bob', return 'Bob likes Alice'

'''

def reverse_all_word(s):
    def reverse_range(s, l, r):
        print(l , r)
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
    reverse_range(s, 0, len(s) - 1)
    start = 0
    while(start < len(s)):
        finish = start
        while finish < len(s) and s[finish] != ' ':
            print(s[finish])
            finish += 1
        reverse_range(s, start, finish - 1)
        start = finish + 1
    
s = list('Alice likes Bob')
print(len(s))
reverse_all_word(s)
print(str(s))
         
