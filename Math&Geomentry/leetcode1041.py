class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        xDir, yDir = 0, 1
        x, y = 0, 0

        for d in instructions:
            if d == "G":
                x, y = x + xDir, y + yDir
            elif d == "L":
                xDir, yDir = -1 * yDir, xDir
            else:
                xDir, yDir = yDir, -1 * xDir
        return (x, y) == (0, 0) or (xDir, yDir) != (0, 1)


x = Solution()
print(x.isRobotBounded("GGLLGG"))
