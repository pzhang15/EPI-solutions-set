import collections
'''
sentence:'amanaplanacanal'
words: {'can', 'apl', 'ana'}, each words has same length
find the substring of the sentence which are the concatenation of all the words
the above should return 'aplanacan', each string in words appear exactly once and order is immaterial 
'''

def sol(sentence, words):
    #先简化成一整个string，去给你一个words set
    #你如何判定是否当前setence是否能够满足出现一次切全部出现
    n = len(sentence)
    unit_length = len(words[0])
    words_to_freq = collections.Counter(words)
    def match_all_words_once(start):
        #记载我们当前window里有每个words的出现频率
        map = collections.Counter()
        # should stop immediately after exhaust our words 
        for i in range(start, start + len(words) * unit_length, unit_length):
            curr_words = sentence[i:i + unit_length]
            it = words_to_freq[curr_words]
            if it == 0: # will also return 0 if key does not exist
                return False

            map[curr_words] += 1
            if map[curr_words] > it:
                #if our window frequency > previous words set dictionary frequency
                return False
        return True

    return [
        #only try in the range of 'excessive' starting positions
        #so all substring are guaranteed in range of n after exhaustion
        i for i in range(n - len(words) * unit_length)
        if match_all_words_once(i)
    ]



sentence = 'amanaplanacanal' 
words = {'can', 'apl', 'ana'}
words_to_freq = collections.Counter(words)
it = words_to_freq['abc']        
print(it)


