class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        children = {}
        lcp = ""

        for word in strs:
            temp = children
            for char in word:

                if char not in temp:
                    temp[char] = {}

                temp = temp[char]

            temp["1"] = 1

        print(children)

        for char in strs[0]:
            if len(children) > 1:
                break

            lcp += char
            children = children[char]

        return lcp