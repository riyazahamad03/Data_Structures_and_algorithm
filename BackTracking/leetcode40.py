class solution:
    def combinationSum2(self, candidates : list[int] , target : int):
        res = []
        candidates.sort()
        def backTrackdfs(curr , idex , tar):
            if tar == 0:
                res.append(curr[::])
                return
            if idex >= len(candidates) or tar <= 0:
                return
            curr.append(candidates[idex])
            backTrackdfs(curr , idex + 1 , tar - candidates[idex])
            curr.pop()
            while idex + 1 < len(candidates) and candidates[idex] == candidates[idex + 1]:
                idex += 1
            backTrackdfs(curr , idex + 1 , tar)
        backTrackdfs([] , 0 , target)
        return res
x = solution()
print(x.combinationSum2([10,1,2,7,6,1,5] , 8))
