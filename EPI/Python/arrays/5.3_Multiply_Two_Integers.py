from typing import *
'''
Certain applications require arbitrary precision arithmetic. 
One way to achieve this is to use arrays to represent integers, 
e.g., with one digit per array entry, with the most significant digit appearing first, 
and a negative leading digit denot¬ inganegativeinteger. 
For, example,(1,9,3,7,0,7,7,2,1)represents193707721and (-7,6,1,8,3,8,2,5,7,2,8,7) represents-761838257287.
Write a program that takes two arrays representing integers, and returns an integer representing their product.
For example, since 193707721 X -761838257287 = -147573952589676412927, if the inputs are  (1,9,3,7,0,7,7,2,1} and (-7,6,1,8,3,8,2,5,7,2,8,7), 
your function should return (-1,4,7,5,7,3,9,5,2,5,8,9,6,7,6,4,1,2,9,2,7).
'''
#O(nm) total bit operation
def multiply(s: int, t: int) -> int:
    # ^ to check if two condition are the same 1^ 1 = 0, 0 ^ 0 = 0, 1 ^ 0 or 0 ^ 1 = 1
    # if they are not the same, our if statement return true, so sign = -1
    sign = -1 if ((s[0] < 0) ^ (t[0] < 0)) else 1 
    s[0], t[0] = abs(s[0]), abs(t[0])
    #           9 9 9
    #         * 1 1 1
    #       ————————————
    #           9 9 9  <- 0
    #         9 9 9    <- 1
    #       9 9 9      <- 2 （m - 1次）

    # 为什么是N + M？可以想象以下我们在做乘法的时候，每一位的T会乘上所有的S，第一次的不会向左shift进位
    # 而之后的每一次都会向左shift进位一次， 所以相当于把N长度的S，向左shift了（M - 1）次
    # 但是因为第一位有可能出现进位的情况，比如 999 * 911，那么我们为了补位要给流出额外的一个位置
    # N会最终向左shift (M - 1) + 1 = M 次，顾:N + M

    res = [0] * (len(s) + len(t))

    for i in reversed(range(len(s))):
        for j in reversed(range(len(t))):
            #          idx: 0  1  2
            #            s: 1  3  8 
            #          idx:    0  1
            #            t:    4  6
            #
            # idx:    0  1  2  3  4  
            # res:               48

            #为什么是 i + j + 1呢,
            #因为我们的res长度为 N + M, s的长度为N， t的长度为M
            #但是res实际最后一位为 N + M - 1， 而S的最后一位为 N - 1, t的最后一位为M - 1
            #所以实际上 S + T = （N - 1） + (M - 1) = N + M - 2， 所以要 + 1用来补位 变为 N + M - 1而和我们的result对齐
            #  idx:     0 1
            #           1 5  
            #      *    2 1
            #--------------
            #idx:   0 1 2 3 
            # 1 + 1 + 1 = 3
            #             5              
            
            
            
            res[i + j + 1] += s[i] * t[j] # 注意是 +=,因为当前res可能存了上一次循环的进位数字
            res[i + j] += res[i + j + 1] // 10
            res[i + j + 1] %= 10

    # remove the leading zeros
    i = 0
    for i in range(len(res)):
        if res[i] != 0:
            break
    res = res[i:]

    return [res[0] * sign] + res[1:]

s = [-9, 9, 9]
t = [1, 1, 1]
res = multiply(s, t)
print(res)