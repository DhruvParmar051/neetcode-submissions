import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)        

        heap = [-count for count in freq.values()]

        heapq.heapify(heap)

        cooldown = deque()
        time = 0 

        while heap or cooldown:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1

                if count != 0:
                    cooldown.append((count,time+n))

            
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(heap, cooldown.popleft()[0])
        
        return time