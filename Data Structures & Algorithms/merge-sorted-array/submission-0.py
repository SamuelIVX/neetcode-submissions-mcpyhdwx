class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        R = 0

        while R < n:
            nums1[m] = nums2[R]

            m += 1
            R += 1
            
        return nums1.sort()