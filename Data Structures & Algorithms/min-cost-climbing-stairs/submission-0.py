class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = [0] * (len(cost) + 1)
        d[0] = 0
        d[1] = 0

        for i in range(2,len(cost)+1):
            d[i] = min(d[i-1]+cost[i-1], d[i-2]+cost[i-2])
        
        return d[len(cost)]