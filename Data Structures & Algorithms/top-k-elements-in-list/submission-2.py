import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)
        res = []
        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        