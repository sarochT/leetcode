class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        new_num = ""
        if x < 0:
            return False
        for i in range(len(num)):
            new_num += num[len(num)-i-1]
        return int(new_num) == x