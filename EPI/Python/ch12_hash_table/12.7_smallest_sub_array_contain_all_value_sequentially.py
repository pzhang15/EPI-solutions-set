import collections
'''
paragraph = ['apple', 'banana','apple','apple','dog', 'cat', 
            'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keywords :=   {banana, cat, dog}
same as 12.6, but keys has to be contains sequentially 
'''

#想要了解最优解必须从暴力解法开始，很多hashmap其实是优化暴力解法
#Bruteforce O(N^3): with O(N^2) repeated work
def sol(paragraph, keywords):
    min_dist = float('-inf')
    n = len(paragraph)
    #枚举每个subarray
    for i in range(n):
        for j in range(i + 1, n):
            prev = i #last keyword index
            for keyword in keywords:
                curr_idx = paragraph[i:j].index(keyword)
                if curr_idx < prev:
                    break
                prev = curr_idx
            else:
                min_dist = min(j-i, min_dist)
    return min_dist

#BruteForce O(n^2)：with O(N) repeated work
def sol2(paragraph, keywords): 
    n = len(paragraph)
    for i in range(n):
        for j in range(i + 1, n):
            curr_key = 0
            #mark off each words sequentially and move forward and try to find the next ones
            if paragraph[j] == keywords[curr_key]:
                curr_key += 1 
            if curr_key > len(keywords):
                min_dist = min(min_dist, j - i)
                break
    return min_dist

# O(N) optimal soluion:
Subarray = collections.namedtuple('Subarray', ('start', 'end'))
def sol3(paragraph, keywords):
    #Maps each keyword to its index int he keywords array
    #This will help us determin the sequentiality of each key
    keys_to_idx = {k : i for i, k in enumerate(keywords)}
    latest_occur = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)
    shortest_dist = float('inf')
    res = Subarray(-1, -1)

    for i, p in enumerate(paragraph):
        if p in keys_to_idx:
            key_idx = keys_to_idx[p] #update to the lastest occurence
            if key_idx == 0: #first keyword
                shortest_subarray_length[key_idx] = 1
            # can only be executed when key_idx -1 has been filled
            # 思考一下错位的情况：
            # paragraph = ['a', 'c', 'b']
            # keywords =  ['a', 'b', 'c']
            # 思考为什么我们要for loop去enumerate paragraph而不是keywords？
            #shortest subarray是记载成功链接起来的subarray，
            elif shortest_subarray_length[key_idx - 1] != float('inf'):
                distance_to_previous_keyword = (i - latest_occur[key_idx - 1])
                shortest_subarray_length[key_idx] = (distance_to_previous_keyword + shortest_subarray_length[key_idx - 1])
            #不懂为什么要这么设计。。。
            latest_occur[key_idx] = i

            if key_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_dist:
                shortest_dist =  shortest_subarray_length[-1]
                res = Subarray(i - shortest_dist + 1, i)
    return res

paragraph = ['apple', 'banana','apple','apple','dog', 'cat', 
            'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keywords = ['banana', 'cat', 'dog']
res = sol3(paragraph, keywords)
print(res)