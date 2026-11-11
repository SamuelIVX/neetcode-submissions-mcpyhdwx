class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = left = right = 0

        while right <= len(s) - 1:
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            right += 1
            
            length = max(length, right - left)
        
        return length