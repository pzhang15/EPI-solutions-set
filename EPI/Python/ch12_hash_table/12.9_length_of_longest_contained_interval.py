'''
A = [3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8]

return [-2, -1, 0, 1, 2, 3] as a continued longestd interval
'''
def sol(A):
    s = set(A)
    max_size = 0
    while s:
        a = s.pop()
        lower = a - 1
        while lower in s:
            s.remove(lower)
            lower -= 1
        upper = a + 1
        while upper in s:
            s.remove(upper)
            upper -= 1
        #仔细思考为什么要是upper - lower - 1
        #    lower               uppper
        #------3------4------5------6-------
        # 这是个 点vs段 的问题
        # upper - lower， 6 - 3 = 3 代表的是中间隔过了3段
        # 但是因为lower 和 upper都是在最后因为查询失败所弹出while loop
        # 所以我们实际上应该不包含lower 和 upper当前所指向的数字
        # 实际上应该是(upper - 1) - (lower - 1) 
        # 也就是 5 - 4 = 1我们可以获得实际合法interval之间数字隔了多少段
        # 题里问的是一共有多少个数字， 也就是点。但通过减法我们只能得到段， 所以 + 1补上
        # (upper - 1) - (lower - 1) + 1 = upper - lower - 1
        max_size = max(max_size, upper - lower - 1)
    return max_size

