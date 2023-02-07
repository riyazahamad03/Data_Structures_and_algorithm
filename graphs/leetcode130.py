class solution:
    def solve(self,board:list[list[int]]):
        ROWS,COLS = len(board),len(board[0])
        def capture(r , c):
            if r == ROWS or c == COLS or r < 0 or c < 0 or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r , c + 1)
            capture(r , c - 1)
        # capture the border elements
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or r == ROWS -1 or c == 0 or c == COLS - 1 or board[r][c] != 'O':
                    capture(r, c)

        # mark the elements which are 'O' as 'X' since the elements in which does 
        # not satisfy the condition are marked as 'T' 
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
        
        # uncapture the captured elements
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        return board
x = solution()
print(x.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))