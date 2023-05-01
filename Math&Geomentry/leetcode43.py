class solution:
    def multiply(self, str1: str, str2: str):
        if str1 == "0" or str2 == "0":
            return "0"
        res = [0] * (len(str1) + len(str2))
        str1,str2 = str1[::-1],str2[::-1]
        for idx in range(len(str1)):
            for jdx in range(len(str2)):
                dig = int(str1[idx]) * int(str2[jdx])
                res[idx + jdx] += dig
                res[idx + jdx + 1] += res[idx + jdx] // 10
                res[idx + jdx] = res[idx + jdx]%10
        res , ptr = res[::-1] , 0
        while ptr < len(res) and res[ptr] == 0:
            ptr += 1
        res = map(str , res[ptr::])
        return "".join(res)
x = solution()
print(x.multiply('123' , '456'))
