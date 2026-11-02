class Solution:
    def mySqrt(self, x: int) -> int:
        # Minimum bound is: 0 (non-negative int includes 0)
        # Maximum bound is: x

        left, right = 0, x
        res = 0

        while left<=right:
            mid = left+(right - left) // 2
            square = mid*mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return int(right)