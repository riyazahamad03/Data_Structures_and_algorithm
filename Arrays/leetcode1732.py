class solution:
    def largestAltitude(self, gain: list[int]):
        maxAlt, alt = 0, 0
        for i in range(len(gain)):
            alt += gain[i]
            maxAlt = max(maxAlt, alt)
        return maxAlt


x = solution()
print(x.largestAltitude([-5, 1, 5, 0, -7]))
