class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        abcbbabcd
        dvdf
        aabcade -> bcade
        
        abc
        """
        
        def removeDuplicate(text, alpha):
            for i in range(len(text)):
                if text[i] == alpha:
                    return text[i+1:]
            return text
        
        if len(s) == 0:
            return 0
        
        tmp = ""
        sub = []
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp += s[i]
            else:
                sub.append(tmp)
                tmp += s[i]
                tmp = removeDuplicate(tmp, s[i])
        sub.append(tmp)
        
        m = 0
        for i in range(len(sub)):
            if m < len(sub[i]):
                m = len(sub[i])
        
        print(sub)
        return m