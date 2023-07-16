class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]):
        n = len(people)
        m = len(req_skills)
        skillId = {}
        for i, skill in enumerate(req_skills):
            skillId[skill] = i
        skill_mask = [0] * n
        for i in range(n):
            for skill in people[i]:
                skill_mask[i] |= 1 << skillId[skill]
        dp = [-1] * (1 << m)
        dp[0] = 0

        def f(mask):
            if dp[mask] != -1:
                return dp[mask]
            for i in range(n):
                newMask = mask & ~skill_mask[i]
                if newMask != mask:
                    peopleMask = f(newMask) | (1 << i)
                    if (dp[mask] == - 1 or peopleMask.bit_count() < dp[mask].bit_count()):
                        dp[mask] = peopleMask
            return dp[mask]
        answer = f((1 << m) - 1)
        ans = []
        for i in range(n):
            if (answer >> i) & 1:
                ans.append(i)
        return ans


x = Solution()
print(x.smallestSufficientTeam(req_skills=["java", "nodejs", "reactjs"], people=[["java"], ["nodejs"], ["nodejs", "reactjs"]]
                               ))
