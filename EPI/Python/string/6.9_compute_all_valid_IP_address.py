'''
IP address is 4 decimal string separted by periods like 192.168.1.201, 3 periods total
each decimal string is between 0-255
given a decimal string, determine where to add periods to a decimal string so that the resulting tring is a valid IP address
'''
# enumerate all possible three periods location, roll back whenver we see an invalid number
def sol(s):
    def is_valid(s):
        # '00', '001' are not valid, 0 is valid
        print(s)
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)  #no leading zero, but '0' is fine
    result = []
    n = len(s)
    parts = [''] * 4 
    for i in range(1, min(4, n)):
        parts[0] = s[:i]
        if is_valid(parts[0]):
            for j in range(1, min(4, n - i)):
                parts[1] = s[i:i + j]
                if is_valid(parts[1]):
                    for k in range(1, min(4, n - i - j)):
                        parts[2], parts[3] = s[i + j:i + j + k], s[i + j + k:]
                        if is_valid(parts[2]) and is_valid(parts[3]):
                            result.append('.'.join(parts))
    return result

s = '19216811'
result = sol(s)

print(result)