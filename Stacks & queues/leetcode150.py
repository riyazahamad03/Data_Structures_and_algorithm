class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        i = 0
        while i < len(tokens):
            if tokens[i] == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) + int(num2))
            elif tokens[i] == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append( int(num1) - int(num2))
            elif tokens[i] == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) * int(num2))
            elif tokens[i] == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(float(num1) / num2))
            else:
                stack.append(int(tokens[i]))
            i+=1
            # print(stack)
        return stack[-1]
x = Solution()
print(x.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
