"""
    https://leetcode.com/problems/3sum-closest/
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # initial value
        diff = abs(target - sum(nums[0:3]))
        ans = sum(nums[0:3])
        
        nums.sort()
        
        for i in range(len(nums)):
            lo = i+1
            hi = len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                tmp_diff = abs(target - s)
                if tmp_diff < diff:
                    diff = tmp_diff
                    ans = s

                if s < target:
                    lo += 1
                else:
                    hi -=1
        
        return ans
        