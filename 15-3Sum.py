"""
    https://leetcode.com/problems/3sum/
    
    Solution:
        a + b + c = 0
        case 1:
            a = b = c = 0
        case 2:
            c = -(a+b), a != b

        Time complexity: O(n^2)
"""

class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3 or max(nums) < 0:
            return []
            
        # initial value
        answers = []
        num_count = {}
        
        for n in nums:
            if num_count.get(n):
                num_count[n] += 1
            else:
                num_count[n] = 1
                
        if len(num_count) == 1 and num_count.get(0):
            return [[0, 0, 0]]
        if num_count.get(0) and num_count.get(0) >= 3:
            answers.append([0, 0, 0])
                
        nums = list(set(nums))
        nums.sort()
                
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num3 = -1 * (nums[i] + nums[j])
                candidate = [nums[i], nums[j], num3]
                candidate.sort()
                if num_count.get(num3):
                    if num3 != nums[i] and num3 != nums[j] \
                        or num3 == nums[i] and num_count.get(num3) > 1 \
                            or num3 == nums[j] and num_count.get(num3) > 1:
                        if candidate not in answers:
                            answers.append(candidate)
                
        return answers
                    