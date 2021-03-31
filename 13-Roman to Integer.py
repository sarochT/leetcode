class Solution:

    def romanToInt(self, s: str) -> int:
        value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if len(s) == 1:
            return value[s[0]]
        
        count = 0
        partition = []
        for i in range(0, len(s)):
            if count > len(s) - 1:
                break
            if count == len(s) - 1:
                partition.append(value[s[count]])
                break
            if value[s[count]] < value[s[count+1]]:
                partition.append(value[s[count+1]]-value[s[count]])
                count += 2
            else:
                partition.append(value[s[count]])
                count += 1

        return sum(partition)