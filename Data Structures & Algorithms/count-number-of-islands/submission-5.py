from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Breadth-First Search
        islands = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        q = deque()        

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    q.append((row, col))
                    grid[row][col] = "0"
                    islands += 1

                while q:
                    curr_row, curr_col = q.popleft()

                    for direction in directions:
                        new_row = curr_row + direction[0]
                        new_col = curr_col + direction[1]

                        if ((new_row >= 0 and new_row < len(grid)) and (new_col >= 0 and new_col < len(grid[0]))) and grid[new_row][new_col] == "1":
                            q.append((new_row, new_col))
                            grid[new_row][new_col] = "0"

        return islands
                    
