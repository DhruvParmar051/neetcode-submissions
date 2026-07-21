class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None
        
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        time = 0

        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()           
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            
            time += 1

        return time if not fresh else - 1
