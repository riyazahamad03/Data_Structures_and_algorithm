class solution:
    def removeStars(self , s : str):
        stack = []
        for i in range(len(s)):
            if s[i] == "*" and stack:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)
x = solution()
print(x.removeStars("leet**cod*e"))