class solution:
    def mergeTriplets(self , triplets : list[list[int]] , target : list[int]):
        goodSet = set()
        for triples in triplets:
            if triples[0] > target[0] or triples[1] > target[1] or triples[2] > target[2]:
                continue
            for idex , e in enumerate(triples):
                if e == target[idex]:
                    goodSet.add(idex)
        return len(goodSet) == 3
x = solution()
print(x.mergeTriplets([[2,5,3],[1,8,4],[1,7,5]] , [2,7,5]))