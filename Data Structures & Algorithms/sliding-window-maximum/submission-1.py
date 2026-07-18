class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # res = []

        # for i in range(len(nums)-k+1):
        #     res.append(max(nums[i:i+k]))
        
        # return res

        q = deque()
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] <= r - k:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])

        return res
