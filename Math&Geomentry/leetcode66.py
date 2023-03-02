class solution:
    def plusOne(self,dig:list[int]):
        dig = dig[::-1]
        f = True
        i = 0
        while f:
            if i < len(dig):
                if dig[i] == 9:
                    dig[i] = 0
                else:
                    dig[i] += 1
                    f = False
            else:
                dig.append(1)
                f = False
        return dig[::-1]
x = solution()
print(x.plusOne([1,2,3]))