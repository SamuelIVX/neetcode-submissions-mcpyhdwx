class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        k = len(set(s))
        length = left = 0

        for right in range(len(s)):

            while s[right] in substring:
                substring.remove(s[left])
                left += 1

            substring.add(s[right])
            
            if right - left + 1 > length:
                length = right - left + 1
            if length == k:
                break
        
        return length