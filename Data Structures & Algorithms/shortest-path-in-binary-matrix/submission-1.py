from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (
            grid[0][0] == 1 
            or grid[len(grid) - 1][len(grid) - 1] == 1
        ): return -1

        directions = [
            (0,1),(1,0),(-1,0),(0,-1),
            (1,1),(-1,-1),(-1,1),(1,-1)
        ]
        q = deque()
        path_length = 1

        q.append((0,0))
        grid[0][0] = "1"

        while q:
            level_size = len(q)
            for _ in range(level_size):
                row, col = q.popleft()
                if (row, col) == (len(grid) - 1, len(grid) - 1): return path_length

                for dr,dc in directions:
                    new_row, new_col = row+dr, col+dc

                    if (
                        new_row >= 0 and new_row < len(grid)
                        and new_col >= 0 and new_col < len(grid[0])
                        and grid[new_row][new_col] == 0
                    ):
                        grid[new_row][new_col] = "1"
                        q.append((new_row,new_col))
            path_length += 1
        
        return -1