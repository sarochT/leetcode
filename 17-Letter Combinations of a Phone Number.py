"""
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/
    Time complexity: O(m^n)
"""

class Solution:
    
    answers = []
    
    def generateLetterCombinations(self, answer, i: int):
        if i == len(self.digits):
            self.answers.append(answer)
            return
        
        for c in self.digit_chars[self.digits[i]]:
            self.generateLetterCombinations(answer+c, i+1)

    
    def letterCombinations(self, digits: str) -> List[str]:
        # reset to default
        self.answers = []
        # initial value
        self.digits = digits
        self.digit_chars = {
            '2': "abc", 
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        if len(digits) == 0:
            return []
        else:
            self.generateLetterCombinations("", 0)
            return self.answers