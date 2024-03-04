class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        res = score = 0
        l, r = 0, len(tokens) - 1
        while l < r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
                res = max(res, score)
            elif score >= 1:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break

        return res


x = Solution()
print(x.bagOfTokensScore(tokens=[100, 200, 300, 400], power=200))
