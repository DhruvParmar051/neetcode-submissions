class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0,n-1
        water = 0
        left_max, right_max = heights[left], heights[right]

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, heights[left])
                water += left_max - heights[left]
            else:
                right -= 1
                right_max = max(right_max, heights[right])
                water += right_max - heights[right]
        
        return water 


