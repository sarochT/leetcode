"""
    https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        solution = []
        candidates.sort()
        
        if sum(candidates) < target:
            return []
        
        def find_sum(new_candidate, next_index):
            
            if sum(new_candidate) == target and new_candidate not in solution:
                solution.append(new_candidate)
                return
            
            if sum(new_candidate) > target:
                return
            
            for i in range(next_index, len(candidates)):
                find_sum(new_candidate + [candidates[i]], i+1)
            
        find_sum([], 0)

        return solution