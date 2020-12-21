'''
Implement:
 1. a integer to string function
 2. a string to integer function

'''
def int_to_string(x: int) -> str:
    is_negative = False 
    if x < 0:
        is_negative = True
        x = -x
    
    s = []
    while x  > 0:
        s.append(chr(ord('0') + x %10))
        x //= 10
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s: str) -> int:
    sign = -1 if s[0] == '-' else 1
    s = s[s[0] in '+-':]
    running_sum = 0
    #True = 1, so we can just slice the sign character off
    for c in s:
        running_sum = running_sum * 10 + (ord(c) - ord('0'))

    return sign * running_sum

x = -456
s  = int_to_string(x)
x = string_to_int(s)
print(x)

