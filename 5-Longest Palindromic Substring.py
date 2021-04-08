class Solution:
    def __init__(self):
        self.mem = {}
    
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        
        if len(s) == 1:
            return s
            
        even = False
        for i in range(1,len(s)+1):
            head = i
            tail = i+1
            
            for j in range(0,len(s)+1):
                if head < 0 or tail > len(s):
                    break
                if self.IsParindrome(s[head:tail]):
                    if len(longest_palindrome) < len(s[head:tail]):
                        longest_palindrome = s[head:tail]
                else:
                    break
                head -= 1
                tail += 1
                
            head = i-1
            tail = i+1
            for j in range(0,len(s)+1):
                if head < 0 or tail > len(s):
                    break
                if self.IsParindrome(s[head:tail]):
                    if len(longest_palindrome) < len(s[head:tail]):
                        longest_palindrome = s[head:tail]
                else:
                    break
                head -= 1
                tail += 1
        return longest_palindrome
            
    def IsParindrome(self, s: str) -> bool:
        swap = ""
        if self.mem.get(s):
            return True
        for i in range(len(s)):
            swap += s[len(s)-i-1]
        if swap == s:
            self.mem[s] = True
            return True
        return False