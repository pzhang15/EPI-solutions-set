import collections
'''
Given an array of words(paragraph), and a set of keywords. 
find minimum subarray that contains all keywords, return its indices
paragraph = ['apple', 'banana','apple','apple','dog', 'cat', 
            'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
keyword = {banana, cat}
'''
def sol(paragraph, keyword):
    
    #为什么要用Counter把原本的set转换成hashmap呢？即便是set中每个元素有且只有一个
    #如果：通过移动指针时删除set中的元素来检查我们是否有涵盖所有的key， 我们会丢失key，
    #在走到后来如果window中不包含key， 我们需要重新添加的时候却不知道当初删掉的哪些key
    #所以set只适合用来知道还未涵盖的个数，用来解答：当前 并不知道记录在什么时候删掉了具体哪个key
    #而尽管每个set中元素只有一个，我也依然可以知道具体哪个key的个数为0, 甚至为负，以及当初set含有哪些key（
    #某个key的val = 0时， key依然可以支持查询， hashmap为负的时候说明我可以有多余的可以进行省略
    #但是因为我们丢失了原本用len(set)就可以得知当前还未涵盖的个数，因为len(dic)永远等于一开始key的个数， 
    #所以我们需要额外的变量来知道还剩多少个需要进行覆盖
    keys = collections.Counter(keyword)
    remain = len(keyword)
    res = Subarray(-1, len(paragraph)) #window至多有，而且确保能进入第一次比较
    start = 0
    for end, s in enumerate(paragraph):
        if s in keys:
            keys[s] -= 1 #hashmap为负的时候说明我可以有多余的可以进行丢弃
            if keys[s] >= 0: #因为起始为1，即时keys[s] == 0说明当前window中至少含有一个当前为key的s
                remain -= 1
        while remain == 0:
            if end - start < res.end - res.start:
                res.start, res.end = start, end
            word = paragraph[start]
            if word in keys:
                keys[word] += 1
                if keys[word] > 0:
                    remain += 1
            start += 1
    return res
            
            



