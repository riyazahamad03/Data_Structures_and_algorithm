from collections import Counter, defaultdict
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        row,col = len(board),len(board[0])
        resultSet = set()
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if (r < 0 or r>= row or c<0 or c>=col or word[i] != board[r][c] or (r,c) in resultSet ):
                return False
            
            resultSet.add((r,c))
            
            res = ( dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1)
                    )
            resultSet.remove((r,c))
            return res
        # to prevent TLE
        count = defaultdict(int,sum(map(Counter,board),Counter()))
        if count[word[0]] > count[word[-1]]:
            word=word[::-1]
            
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
x = Solution()
print(x.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"ABCCED"))