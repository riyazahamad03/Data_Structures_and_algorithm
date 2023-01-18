class solution:
    def generateParanthesis(self,n:int):
        res,stack = [],[]

        def backTrack(openN,CloseN):
            if openN == CloseN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                backTrack(openN + 1,CloseN)
                stack.pop()
            if CloseN < openN:
                stack.append(')')
                backTrack(openN , CloseN + 1)
                stack.pop()
        backTrack(0,0)
        return res
x = solution()
print(x.generateParanthesis(10))