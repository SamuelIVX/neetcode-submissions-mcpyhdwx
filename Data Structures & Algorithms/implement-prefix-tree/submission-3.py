class PrefixTree:

    def __init__(self):
        self.children = {}        

    def insert(self, word: str) -> None:
        curr = self.children

        for char in word:
            if char not in curr:
                curr[char] = {}
            
            curr = curr[char]

        curr["1"] = 1

    def search(self, word: str) -> bool:
        curr = self.children

        for char in word:
            if char not in curr:
                return False
            
            curr = curr[char]
        
        return "1" in curr
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.children

        for char in prefix:
            if char not in curr:
                return False
            
            curr = curr[char]
        
        return True