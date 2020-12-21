from typing import *
import functools
'''
spread sheet columns: A, B, C, ... X, Y, Z, AA, AB, AC... ZZ, AAA, AAB, ...
given spreadsheet columns encoding, with A corresponding to 1, convert it to to integer
e.g 4 for 'D', 27 for 'AA', 72 for 'ZZ'

'''
# brute force is  O(26^n), n the length of the string
# for every digit, you have to numerate additional 'A-Z'
def encoding_to_int(enc):
    value = 0
    for c in enc:
        num = ord(c) - ord('A') + 1
        value = value * 26 + num
    return value

def pythonic_way(enc):
    return functools.reduce(
        lambda result, c: result * 26 + (ord(c) - ord('A') + 1), enc, 0
    )

enc = 'ZZ'
res = encoding_to_int(enc)
res2 = pythonic_way(enc)
print(res, res2)


