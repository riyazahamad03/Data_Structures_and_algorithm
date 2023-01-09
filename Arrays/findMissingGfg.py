class solution:
    def findMissing(self,A,B,N,M):
        d,res = {},[]
        for i in range(N):
            d[A[i]] = 1 + d.get(A[i],0)
        for j in range(M):
            d[B[j]] = 0
        for i in range(N):
            if d[A[i]] >= 1:
                res.append(A[i])
        return res
x = solution()
print(x.findMissing([1, 2, 3, 4, 5, 10],[2, 3, 1, 0, 5],6,5))