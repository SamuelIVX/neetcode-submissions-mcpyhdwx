class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 1. Quick Length Check
        if len(word) > len(board) * len(board[0]): return False

        # 2. Character Pruning
        board_count = Counter()
        for row in range(len(board)):
            for col in range(len(board[0])):
                board_count[board[row][col]] += 1

        word_count = Counter(word)
        for char, count in word_count.items():
            if board_count[char] < count: return False

        # 3. Reverse Search
        if board_count[word[0]] > board_count[word[-1]]: word = word[::-1]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def findWord(row, col, index):
            if index == len(word): return True
            if (
                (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])) 
                or board[row][col] != word[index] 
            ): return False

            temp = board[row][col]
            board[row][col] = "1"

            for dr,dc in directions:
                if findWord(row+dr, col+dc, index + 1): return True

            board[row][col] = temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if findWord(row, col, 0):
                        return True

        return False