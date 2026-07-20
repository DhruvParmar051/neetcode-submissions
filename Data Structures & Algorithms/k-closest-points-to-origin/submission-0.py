class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            dis = ((x-0)**2 + (y-0)**2)**0.5

            heapq.heappush(heap,(dis,x,y))

        res = []
        for _ in range(k):
            _,x,y = heapq.heappop(heap)

            res.append([x,y])
        
        return res