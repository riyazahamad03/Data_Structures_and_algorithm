class solution:
    def minFlips(self , a : int , b : int , c : int):
        flips = 0
        while a > 0 or b > 0 or c > 0:
            bitA = a & 1
            bitB = b & 1
            bitC = c & 1

            if not bitC:
                flips += bitA + bitB
            else:
                if not bitA and not bitB:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1
        return flips
x = solution()
print(x.minFlips(a = 2, b = 6, c = 5))