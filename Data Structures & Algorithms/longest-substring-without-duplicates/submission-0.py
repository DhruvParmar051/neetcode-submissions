from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = deque()
        length = 0

        for ch in s:
            while ch in window:
                window.popleft()
            
            window.append(ch)
            length = max(length, len(window))
        
        return length