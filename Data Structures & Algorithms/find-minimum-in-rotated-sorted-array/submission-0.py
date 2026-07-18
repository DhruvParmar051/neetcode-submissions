class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = float('inf')
        for num in nums:
            mini = min(num, mini)
        return mini