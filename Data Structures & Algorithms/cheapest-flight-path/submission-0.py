import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u,v, price in flights:
            graph[u].append((v,price))

        minHeap = [(0,src,0)]
        best = {}
        visited = set()

        while minHeap:
            cost, node, flight = heapq.heappop(minHeap)

            if node == dst:
                return cost
            
            if flight == k+1:
                continue
            
            for nei, price in graph[node]:
                newCost = cost + price

                if best.get((nei,flight+1),float('inf')) <= newCost:
                    continue

                best[(nei,flight + 1)] = newCost
                heapq.heappush(minHeap, (newCost,nei,flight+1))

        return -1