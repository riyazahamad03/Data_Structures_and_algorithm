class solution:
    def myPow(self , x : float , n : int):
        def powX(x , n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            resVal = powX(x , n//2)
            resVal = resVal * resVal
            return x * resVal if n%2 else resVal
        res = powX(x , n)
        return res if n>=0 else 1/res
x = solution()
print(x.myPow(2.00000 , 10))