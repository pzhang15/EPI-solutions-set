# return how many bit of ones are in a number
def countbits(x):
    cnt = 0
    while x:
        bit = x & 1
        print("x: ", "{0:b}".format(x), "bit: ", bit)
        cnt += bit
        x >>= 1
    return cnt

print("result: ", countbits(4))

