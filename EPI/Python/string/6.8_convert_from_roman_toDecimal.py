import functools
'''
Roman to interger
T = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    Exceptions:
        I before V and X
        X before L and C
        C before D and M
Back to Back exception is not allowed
'''
#trick to Roman integer is to iterate from right to left and subtract 
def sol(s):
    T = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]]
    )

s = 'LIX'
it = sol(s)
print(it)