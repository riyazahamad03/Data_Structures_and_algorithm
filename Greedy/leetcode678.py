class solution:
    def checkValidString(self , s : str):
        lMin , lMax = 0, 0
        for char in s:
            if char == "(":
                lMin , lMax = lMin + 1 , lMax + 1
            elif char == ")":
                lMin , lMax = lMin - 1 , lMax - 1
            else: # "*" char can have two possible of '(' and ')'
                lMin , lMax = lMin - 1 , lMax + 1
            if lMax < 0:
                return False
            if lMin < 0: #possibly that Asterisk could be on possible way in greedy approach
                lMin = 0
        return lMin == 0
x = solution()
print(x.checkValidString("()"))
