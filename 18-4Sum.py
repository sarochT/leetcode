"""
    https://leetcode.com/problems/4sum/

    Time complexity: O(n^3)
"""

class Solution:
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # initialize value
        answers = []
        nums.sort()
        num_count = {}
        for i in range(len(nums)):
            if num_count.get(nums[i]):
                num_count[nums[i]] += 1
            else:
                num_count[nums[i]] = 1

        
        # calculate
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    num4 = target - (nums[i] + nums[j] + nums[k])
                    candidate = [nums[i], nums[j], nums[k], num4]

                    if num_count.get(num4) is None:
                        continue
                    
                    # To prevent getting non-existing members
                    count = 0
                    for n in [nums[i], nums[j], nums[k]]:
                        if n == num4:
                            count += 1
                    if num_count[num4] <= count:
                        continue

                    # To prevent duplicate answers
                    candidate.sort()
                    if candidate not in answers:
                        answers.append(candidate)

        return answers