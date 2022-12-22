class solution:
    def canJump(self,lst:list[int]):
        goalPost = len(lst)-1
        for i in range(len(lst)-1,-1,-1):
            if i+lst[i] >= goalPost:
                goalPost = i
        if goalPost == 0:
            return True
        else:
            return False
x = solution()
print(x.canJump([2,3,1,1,4]))