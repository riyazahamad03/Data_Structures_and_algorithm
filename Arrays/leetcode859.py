class solution:
    def buddyStrings(self, s: str, goal: str):
        if len(s) != len(goal):
            return False

        if s == goal:
            freq = {}
            for i in range(len(s)):
                freq[s[i]] = 1 + freq.get(s[i], 0)

                if freq[s[i]] == 2:
                    return True
            return False
        fIdex, sIdex = -1, -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if fIdex == -1:
                    fIdex = i
                elif sIdex == -1:
                    sIdex = i
                else:
                    return False
        if sIdex == -1:
            return False

        return s[fIdex] == goal[sIdex] and s[sIdex] == goal[fIdex]


x = solution()
print(x.buddyStrings(s="ab", goal="ba"))
print(x.buddyStrings(s="ab", goal="ab"))
print(x.buddyStrings(s="aa", goal="aa"))
