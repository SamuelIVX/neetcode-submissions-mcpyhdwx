class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Minimum num of rows: 0
        # Maximum num of rows: n
        low, high = 0, n 

        while low<= high:
            # Now that we picked some k row(s) of i length
            # How many coins will it cost to build these k row(s)?
            mid = low+(high - low) // 2
            cost = mid * (mid + 1) // 2

            if cost == n:
                return mid
            elif cost > n:
                high = mid - 1
            else:
                low = mid + 1
        
        return high
