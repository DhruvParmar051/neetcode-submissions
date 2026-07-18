class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = float('inf')
        max_profit = float('-inf')

        for price in prices:
            best_buy = min(best_buy,price)
            max_profit = max(max_profit, price-best_buy)
        
        return max_profit