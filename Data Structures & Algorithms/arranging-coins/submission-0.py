class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Minimum num of rows: 0
        # Maximum num of rows: n
        left, right = 0, n 

        while left<= right:
            # Now that we picked some k row(s) of i length
            # How many coins will it cost to build these k row(s)?
            k_rows = left+(right - left) // 2
            cost = k_rows*(k_rows + 1)/2

            if cost == n:
                return k_rows
            elif cost > n:
                right = k_rows - 1
            else:
                left = k_rows + 1
        
        return right
