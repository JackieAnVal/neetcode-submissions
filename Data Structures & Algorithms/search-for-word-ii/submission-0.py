class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

    def addWord(self, word, node):
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w, root)

        rows, cols = len(board), len(board[0])
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        visited, res = set(), set()

        def dfs(r, c, node, word):
            if r == rows or r < 0 or c == cols or c < 0 or (r, c) in visited or board[r][c] not in node.children:
                return
            
            visited.add((r,c))
            letter = board[r][c]
            node = node.children[letter]
            word += letter
            if node.word:
                res.add(word)
            
            for dr, dc in directions:
                dfs(dr + r, dc + c, node, word)
            visited.remove((r,c))
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] in root.children:
                    dfs(i, j, root, "")
        
        return list(res)