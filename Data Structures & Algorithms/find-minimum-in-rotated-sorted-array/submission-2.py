class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left+(right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Mid itself could be the lowest element, so keep it in the window
                right = mid
        
        return nums[right]