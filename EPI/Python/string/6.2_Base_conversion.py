from typing import *
import string
'''
base 10: 314 denotes number 3 x 100 + 1 x 10 + 4 x 1
                                10 ^2   10^1   10 ^0

give a string , an integer b1, integer b2, the string is in base b1, output string in b2
assuming 2 <= b1, b2 <= 16

'''

def base_conversion(s, b1, b2):
    def construct_from_int(num, base):
        if num == 0:
            return ''
        else:
            return construct_from_int(num // base, base) + string.hexdigits[num % base]
    print(string.hexdigits)
    # convert the string from any base to integer
    # leveraging base 10 method:  string.hexdigits.index(c.lower())
    is_negative = s[0] == '-' #return 1 if it's negative 0 if it's not
    num_as_int = 0
    for c in s[is_negative:]:
        num_as_int = num_as_int * b1 + string.hexdigits.index(c.lower())
    
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_int(num_as_int, b2))

s = '61a'
b1 = 7
b2 = 13

res = base_conversion(s, b1, b2)

print(res)
