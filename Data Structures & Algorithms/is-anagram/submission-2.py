from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countT= Counter(t)

        for c in s:
            if countT[c] <=0:
                return False
            countT[c] -= 1

        return True 