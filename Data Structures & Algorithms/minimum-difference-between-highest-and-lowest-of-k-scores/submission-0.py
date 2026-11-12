class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        window = nums[:k]
        mpd = max(window) - min(window)

        for i in range(1, len(nums) - k + 1):
            window = nums[i:i+k]
            
            mpd = min(mpd, max(window) - min(window))
        
        return mpd