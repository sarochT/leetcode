class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_minus = False
        if x < 0:
            is_minus = True
        answer = ""
        x = str(x)
        for i in range(len(x)):
            if x[len(x) - i - 1] != "-":
                answer += x[len(x) - i - 1]
        if is_minus:
            answer = "-"+answer
        
        answer = int(answer)
        
        if answer > pow(2, 31) - 1 or answer <= -1 * pow(2, 31) :
            return 0
        
        return answer