# Two approach
class Solution:
    def maxArea(self, height) -> int:
        m = 0
        count_left = 0
        count_right = 0
        while True:
            left = count_left
            right = len(height) - count_right - 1
            width = right-left
            # print(height[left], height[right], width)
            if left >= right:
                break
            if m < min(height[left], height[right]) * width:
                m = min(height[left], height[right]) * width
            if height[left] > height[right]:
                count_right += 1
            else:
                count_left += 1
        return m