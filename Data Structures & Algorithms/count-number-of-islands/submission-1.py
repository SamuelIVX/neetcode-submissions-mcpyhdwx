class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        # visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def findIslands(row, col):
            if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])): return
            # if (row, col) in visited: return
            if grid[row][col] == "0": return

            # visited.add((row, col))
            grid[row][col] = "0"

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                findIslands(new_row, new_col)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if (row, col) not in visited and grid[row][col] == "1":
                if grid[row][col] == "1":
                    findIslands(row, col)
                    islands += 1

        
        return islands