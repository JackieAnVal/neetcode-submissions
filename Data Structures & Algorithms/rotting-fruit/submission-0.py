class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])

        visited = set()
        q = deque()

        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    fresh+=1
        
        while q and fresh > 0: 
            minutes +=1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or (nr,nc) in visited or nr == rows or nc == cols or grid[nr][nc] != 1:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    fresh -=1
        return minutes if fresh == 0 else -1