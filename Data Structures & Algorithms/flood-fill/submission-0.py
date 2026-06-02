class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.starting_color = image[sr][sc]
        self.rows = len(image)
        self.columns = len(image[0])
        visited = set()
        def dfs(grid, r, c, visited):
            if (min(r, c) < 0) or r == self.rows or c == self.columns or grid[r][c] != self.starting_color or (r, c) in visited:
                return
            
            visited.add((r,c))
            grid[r][c] = color
            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r, c - 1, visited)
            return
        
        dfs(image, sr, sc, visited)
        return image