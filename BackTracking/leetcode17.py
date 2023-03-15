class solution:
    def letterCombination(self , digits : str):
        res = []
        digToChar = {
            "2" : 'abc',
            "3" : 'def',
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }
        def backTrack(idex , currStr):
            if len(digits) == len(currStr):
                res.append(currStr[::])
                return
            for c in digToChar[digits[idex]]:
                backTrack(idex + 1 , currStr + c)
        if digits:
            backTrack(0 , "")
        return res
x = solution()
print(x.letterCombination("23"))