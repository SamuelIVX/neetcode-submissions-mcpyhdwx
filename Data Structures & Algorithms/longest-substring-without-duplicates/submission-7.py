class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set() # Constant look-up times
        k = len(set(s)) # This will hold the longest substring length
        length = left = 0

        for right in range(len(s)):

            # If the current char at the right pointer is a duplicates
            # Keep removing the char at the left pointer
            # Iterate left pointer
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            # Add the new char at right pointer
            substring.add(s[right])
            
            # Update length to hold the longest substring so far
            if right - left + 1 > length:
                length = right - left + 1
            
            # If our length matches longest substring possible
            # which was calculated at the beginning
            # we can end immediately since there is no reason to continue
            if length == k:
                break
        
        return length