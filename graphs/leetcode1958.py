from typing import List


class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        board[rMove][cMove] = color

        def isLegalMove(color, row, col, dr, dc):
            length = 1
            row, col = row + dr, col + dc
            while (0 <= row < 8 and 0 <= col < 8):
                length += 1
                if board[row][col] == '.':
                    return False
                if board[row][col] == color:
                    return length >= 3
                row, col = row + dr, col + dc
            return False
        for dr, dc in directions:
            if isLegalMove(board[rMove][cMove], rMove, cMove, dr, dc):
                return True
        return False


x = Solution()
print(x.checkMove(board=[[".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."], [
      "W", "B", "B", ".", "W", "W", "W", "B"], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."], [".", ".", ".", "W", ".", ".", ".", "."]], rMove=4, cMove=3, color="B"))
