class solution:
    def romanToInt(self, s: str):
        hashMap = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and hashMap[s[i]] < hashMap[s[i + 1]]:
                res -= hashMap[s[i]]
            else:
                res += hashMap[s[i]]
        return res
x = solution()
print(x.romanToInt('III'))
