from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #BFS Solution
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        pacific_visited = set()
        atlantic_visited = set()
        pacific_q = deque()
        atlantic_q = deque()

        def BFS(q, visited):
            while q:
                curr_row, curr_col = q.popleft()

                for dr,dc in directions:
                    new_row = curr_row + dr
                    new_col = curr_col + dc

                    if (new_row >= 0 and new_row < len(heights)) and (new_col >= 0 and new_col < len(heights[0])) and heights[new_row][new_col] >= heights[curr_row][curr_col] and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        

        for row in range(len(heights)):
            # Left Column
            pacific_visited.add((row, 0))
            pacific_q.append((row, 0))

            # Right Column
            atlantic_visited.add((row, len(heights[0]) - 1))
            atlantic_q.append((row, len(heights[0]) - 1))

        for col in range(len(heights[0])):
            # Top Row
            pacific_visited.add((0, col))
            pacific_q.append((0, col))

            # Bottom Row
            atlantic_visited.add((len(heights) - 1, col))
            atlantic_q.append((len(heights) - 1, col))

        BFS(pacific_q, pacific_visited)
        BFS(atlantic_q, atlantic_visited)

        return [[row, col] for row,col in pacific_visited if (row, col) in atlantic_visited]