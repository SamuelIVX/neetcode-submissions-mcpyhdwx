class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #DFS Solution
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        pacific_visited = set()
        atlantic_visited = set()

        def findCells(row, col, visited, prev_height):
            if (row < 0 or row >= len(heights)) or (col < 0 or col >= len(heights[0])): return
            if (row, col) in visited: return
            if heights[row][col] < prev_height: return

            visited.add((row, col))

            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                findCells(new_row, new_col, visited, heights[row][col])

        for row in range(len(heights)):
            # Left Column
            findCells(row, 0, pacific_visited, float('-inf'))

            # Right Column
            findCells(row, len(heights[0]) - 1, atlantic_visited, float('-inf'))

        for col in range(len(heights[0])):
            # Top Row
            findCells(0, col, pacific_visited, float('-inf'))

            # Bottom Row
            findCells(len(heights) - 1, col, atlantic_visited, float('-inf'))

        return [[row, col] for row, col in pacific_visited if (row,col) in atlantic_visited]