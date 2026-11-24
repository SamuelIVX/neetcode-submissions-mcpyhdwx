import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapq.heapify_max(gifts)

        while k:
            maximum = heapq.heappop_max(gifts)

            heapq.heappush_max(gifts, (int(sqrt(maximum))))

            k -= 1
        
        return sum(gifts)