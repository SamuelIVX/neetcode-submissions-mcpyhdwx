class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = left = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            right += 1
            
            length = max(length, right - left)
        
        return length