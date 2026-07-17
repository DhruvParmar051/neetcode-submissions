class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)

        # result = [1] * n

        # prefix = 1
        # for i in range(n):
        #     result[i] = prefix
        #     prefix *= nums[i]

        # suffix = 1
        # for i in range(n-1,-1,-1):
        #     result[i] *= suffix
        #     suffix *= nums[i]

        # return result

        n = len(nums)

        prefix = [1] * n
        suffic = [1] * n

        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for j in range(n-2,-1,-1):
            suffic[j] = suffic[j+1] * nums[j+1]

        result = [0] * n

        for i in range(n):
            result[i] = prefix[i] * suffic[i]
        
        return result
