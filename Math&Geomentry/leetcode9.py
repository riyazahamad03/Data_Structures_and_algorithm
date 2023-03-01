class solution:
    def isPalindrome(self,x:int):
        if x<0:
            return False
        divider = 1
        while x >= divider*10:
            divider = divider * 10
        
        while x:
            l = x%10
            r = x//divider
            if l!=r:
                return False
            x = (x%divider)//10
            divider//=100
        return True
x = solution()
print(x.isPalindrome(121))