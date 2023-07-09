class solution:
    def largestVariance(self, s: str):
        pairs = [(l1, l2) for l1 in set(s) for l2 in set(s) if l1 != l2]
        res = float("-inf")
        for _ in range(2):
            for pair in pairs:
                c1 = c2 = 0
                for letter in s:
                    if letter not in pair:
                        continue
                    if letter == pair[0]:
                        c1 += 1
                    elif letter == pair[1]:
                        c2 += 1

                    if c1 < c2:
                        c1 = c2 = 0
                    elif c1 > 0 and c2 > 0:
                        res = max(res, c1 - c2)
            s = s[::-1]
        return res if res != float("-inf") else 0


x = solution()
print(x.largestVariance("aababbb"))
