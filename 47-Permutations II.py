class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        answers = []
        
        def find_permute(candidates, candidate_indexes):
            # stop condition
            if len(candidates) == len(nums):
                answers.append(candidates)
                return
                
            # recursive call
            for i in range(0, len(nums)):
                if i not in candidate_indexes:
                    find_permute(candidates + [nums[i]], candidate_indexes + [i])
        
        find_permute([], [])
        return answers
