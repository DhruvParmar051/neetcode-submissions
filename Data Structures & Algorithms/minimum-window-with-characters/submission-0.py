from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        count = Counter(t)
        window = defaultdict(int)

        have = 0
        need = len(count)

        res = [-1,-1]
        resLen = float('inf')

        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in count and window[c] == count[c]:
                have += 1
            
            while have == need:
                if right-left+1  < resLen:
                    res = [left,right]
                    resLen = right-left+1
                
                window[s[left]] -= 1

                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1
            
                left += 1

        l,r = res
        return s[l:r+1] if resLen != float('inf') else "" 