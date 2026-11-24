import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for point in points:
            distance = sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            
            heapq.heappush(heap, (distance, point[0], point[1]))

        while k:
            point = heapq.heappop(heap)
            res.append([point[1], point[2]])
            k -= 1
        
        return res