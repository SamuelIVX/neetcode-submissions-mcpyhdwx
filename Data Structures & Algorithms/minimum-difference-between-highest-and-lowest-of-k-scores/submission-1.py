class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        left, right = 0, k - 1
        mpd = float('inf')

        while right < len(nums):

            mpd = min(mpd, nums[right] - nums[left])

            left += 1
            right += 1            
        
        return mpd