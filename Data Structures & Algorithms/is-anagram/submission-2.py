class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}

        for c in s:
            if c not in mp1:
                mp1[c] = 0
            mp1[c] += 1
        
        for c in t:
            if c not in mp2:
                mp2[c] = 0
            mp2[c] += 1

        return mp1 == mp2