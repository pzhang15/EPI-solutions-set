'''
Given a path name: 'src/./../tc/aws/././', return the shortest absolute path:
src/tc/awk
'''

def sol(s):
    tokens = s.split('/')