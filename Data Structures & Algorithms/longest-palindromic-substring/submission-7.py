class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        start = 0
        maxLen = 1

        for i in range(n):
            dp[i][i] = True

        def isPalindrome(l,r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        

        for i in range(n-1,-1,-1):
            for j in range(i+1,n):

                if s[i] == s[j]:

                    if j - i <= 2:
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        dp[i][j] = True
                
                if dp[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    start = i
        
        return s[start:start + maxLen]
        