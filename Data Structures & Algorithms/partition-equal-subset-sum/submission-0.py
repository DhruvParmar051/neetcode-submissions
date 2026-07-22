class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False
        
        target = total // 2
        position = {0}

        for num in nums:
            new = set()
            for s in position:
                if s + num == target:
                    return True
                new.add(s+num)
            position |= new
        
        return target in position
