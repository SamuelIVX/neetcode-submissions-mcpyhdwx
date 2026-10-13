from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Breadth-First Search
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        pacific_q = deque()
        atlantic_q = deque()
        
        pacific_visited = set()
        atlantic_visited = set()

        def BFS(q, visited):
            while q:
                row, col = q.popleft()

                for direction in directions:
                    new_row = row + direction[0]
                    new_col = col + direction[1] 
                    
                    if (new_row >= 0 and new_row < len(heights)) and (new_col >= 0 and new_col < len(heights[0])) and heights[new_row][new_col] >= heights[row][col] and (new_row, new_col) not in visited:
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for row in range(len(heights)):
            # Left Column            
            pacific_q.append((row, 0))
            pacific_visited.add((row, 0))

            # Right Column
            atlantic_q.append((row, (len(heights[0]) - 1)))
            atlantic_visited.add((row, (len(heights[0]) - 1)))
 
        for col in range(len(heights[0])):
            # Bottom Row
            atlantic_q.append((len(heights) - 1, col))
            atlantic_visited.add((len(heights) - 1, col))
            
            # Top Row
            pacific_q.append((0, col))
            pacific_visited.add((0, col))

        BFS(atlantic_q, atlantic_visited)
        BFS(pacific_q, pacific_visited)

        return [[row, col] for row, col in pacific_visited if (row, col) in atlantic_visited]