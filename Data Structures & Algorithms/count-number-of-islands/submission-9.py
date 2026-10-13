class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Depth-First Search 
        islands = 0
        # visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def findIslands(row, col):
            if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])): return
            # if (row, col) in visited: return
            if grid[row][col] == "0": return

            # visited.add((row, col))
            grid[row][col] = "0"

            for dr, dc in directions:
                findIslands(row + dr, col + dc)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if (row, col) not in visited and grid[row][col] == "1":
                if grid[row][col] == "1":
                    findIslands(row, col)
                    islands += 1

        
        return islands