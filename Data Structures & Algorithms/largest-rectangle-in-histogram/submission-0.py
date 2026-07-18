class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        pse = [-1] * n
        nse = [n] * n

        # previous smallest element
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1]
            
            stack.append(i)

        # next smallest elements 
        stack = []
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            
            stack.append(i)
        
        ans = 0

        for i in range(n):
            width = nse[i] - pse[i] - 1
            ans = max(ans, width * heights[i])
        
        return ans
