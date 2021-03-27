# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        nums = []
        def dfs(node, path):
            # stop condition
            if node.left is None and node.right is None:
                nums.append(path + str(node.val))
                return
            
            # recursive call
            if node.left is not None:
                dfs(node.left, path + str(node.val))
            if node.right is not None:
                dfs(node.right, path + str(node.val))
                    
        dfs(root, "")
        return sum([int(num) for num in nums])