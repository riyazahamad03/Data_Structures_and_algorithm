class TrieNode:
    def __init__(self):
        self.lastChar = False
        self.children = {}
    def addWord(self , word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.lastChar = True
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)
        res , visit = [] , set()
        rows , cols = len(board) , len(board[0])
        def dfs(r , c , node , word):
            if (min(r,c) < 0 or 
                r >= rows or c >= cols or
                (r,c) in visit or
                board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.lastChar:
                res.append(word)
            dfs(r + 1 , c , node , word)
            dfs(r - 1 , c , node , word)
            dfs(r  , c + 1, node , word)
            dfs(r  , c - 1, node , word)
            visit.remove((r,c))
        for row in range(rows):
            for col in range(cols):
                dfs(row , col , root , "")
        return list(set(res))

x = Solution()
print(x.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], [
      "i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "rain", "pea", "eat", "rain", "oath"]))
