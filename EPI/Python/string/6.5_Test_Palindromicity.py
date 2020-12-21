'''
Test if a string is a plindrome, no space
e.g 'A man,a plan,a canal,Panama' is a palindrome
but 'Ray a Ray' is not
'''

def first_attempt(s):
    i, j = 0, len(s) - 1
    while(i < j):
        if not s[i].isalnum():
            i += 1
        if not s[j].isalnum():
            j -=1
        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
        
        
    return True
s = 'A man,a plan,a canal,Panama'
res = first_attempt(s)
print(res)