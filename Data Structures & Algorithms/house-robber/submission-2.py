class Solution:
    def rob(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [0] * n
        # dp[0] = nums[0]        

        # for i in range(1,n):
        #     dp[i] = max(dp[i-1], dp[i-2] +  nums[i])
        
        # return dp[-1]


        n = len(nums)
        prev2, prev1 = 0,0

        for num in nums:
            prev2, prev1 = prev1, max(prev1,prev2+num)
        
        return prev1
