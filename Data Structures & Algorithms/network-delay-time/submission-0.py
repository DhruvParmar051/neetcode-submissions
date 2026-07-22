import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        minHeap = [(0,k)]
        visited = set()
        maxTime = 0

        while minHeap:
            time,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)    
            maxTime = max(maxTime,time)

            for nei, wt in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, ((time+wt,nei)))
        
        return maxTime if len(visited) == n else -1