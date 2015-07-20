def lengthOfLongestSubstring(s):
    result = 0
    temp = []
    temp_new = []
    for i in xrange(0,len(s)):        
        if s[i] not in temp:            
            temp.append(s[i])
            if i == len(s)-1:
                if result < len(temp):
                    result = len(temp)
        else:
            if result < len(temp):
                result = len(temp)
            temp_new = temp[temp.index(s[i])+1:]
            temp_new.append(s[i])
            temp = temp_new
    return result 

print lengthOfLongestSubstring('nfpdmpi')
