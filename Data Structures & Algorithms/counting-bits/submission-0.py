class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            curr = i
            count = 0
            while curr:
                count  += curr & 1
                curr >>= 1
            
            ans.append(count)
        
        return ans