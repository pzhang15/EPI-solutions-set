'''
Test Collatz conjecture for the first n positive intergers
'''
def sol(N):
    verified_number = set()
    # 1 is trivial, 2 is halved to 1
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        #if test_i < i, then it has already been computed
        while test_i >= i:
            if test_i in sequence:
                # loop happened
                return False
            sequence.add(test_i)
            if test_i in verified_number:
                return True
            if test_i % 2 :# odd number
                test_i = test_i * 3 + 1
            else:
                test_i //= 2