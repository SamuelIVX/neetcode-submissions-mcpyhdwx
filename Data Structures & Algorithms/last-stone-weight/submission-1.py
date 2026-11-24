import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heaps are min-heaps by default.
        # For max-heaps, multiply valeus by -1 and push
        # them to the heap as they get sorted by smallest values
        # by default anyway. When popping them, multiply
        # them by -1 once more to get their original values.
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) >= 2:
            # Since first is being popped first from the max-heap
            # first >= second is always true.
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first - second))          
        
        return -heap[0] if heap else 0