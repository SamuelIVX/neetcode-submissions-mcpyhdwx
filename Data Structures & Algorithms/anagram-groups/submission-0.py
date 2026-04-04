class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}
        for str in strs:
            k = "".join(sorted(str))
            if k not in res:
                res[k] = []
            res[k].append(str)
        
        return [x for x in res.values()]