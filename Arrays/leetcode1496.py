class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        x, y = 0, 0

        for i in path:
            if i == "E":
                x += 1
            elif i == "S":
                y -= 1
            elif i == "N":
                y += 1
            elif i == "W":
                x -= 1

            current_position = (x, y)

            if current_position in visited:
                return True

            visited.add(current_position)

        return False


x = Solution()
print(x.isPathCrossing("NESWW"))
