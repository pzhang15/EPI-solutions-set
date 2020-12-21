import functools
import string
'''
_______________________problem statement______________________
6.1:
    Implement:
    1. a integer to string function
        def int_to_s(it):
    2. a string to integer function
        def s_to_int(it):

6.2:
    base 10: 314 denotes number 3 x 100 + 1 x 10 + 4 x 1
                                10 ^2   10^1   10 ^0

    give a string , an integer b1, integer b2, the string is in base b1, output string in b2
    assuming 2 <= b1, b2 <= 16

    def base_conversion(s, b1, b2):

6.3:
    spread sheet columns: A, B, C, ... X, Y, Z, AA, AB, AC... ZZ, AAA, AAB, ...
    given spreadsheet columns encoding, with A corresponding to 1, convert it to to integer
    e.g 4 for 'D', 27 for 'AA', 72 for 'ZZ'
'''






'''
6.4:
    given input array of characters, replace each 'a' with 2 'd's and delete each 'b'
    [a, c, d, b, b, c, a] -> [d, d, c, d, c, d, d]

6.5:
    Test if a string is a plindrome, no space
    e.g 'A man,a plan,a canal,Panama' is a palindrome
    but 'Ray a Ray' is not

6.6:
    Give a string like 'Alice likes Bob', return 'Bob likes Alice'
'''


'''
6.7:
    Look and Say, Given n, return n th 'look and say' number
    <1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211>

6.8:
    Roman to interger
    T = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        Exceptions:
            I before V and X
            X before L and C
            C before D and M
    Back to Back exception is not allowed

6.9:
    IP address is 4 decimal string separted by periods like 192.168.1.201, 3 periods total
    each decimal string is between 0-255
    given a decimal string, determine where to add periods to a decimal string so that the resulting tring is a valid IP address
'''
'''
6.10:
    e.g Give a string 'Hello World'
    1:   e              _               l   
    2: H    l       o       W       r       d
    3:          l               o               !

    return [
            [e_l],
            [hloWrd],
            [lo!]
    ]

6.11:
    RLE encoding:
    aaaabcccaa -> 4a1b3c2a
    implement both encoding and decoding

6.12:
    given two string s(search string) and t (text), find the first occurence of s in t
'''
