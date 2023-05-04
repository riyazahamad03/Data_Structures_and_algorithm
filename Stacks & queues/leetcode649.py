import collections


class solution:
    def predictPartyWinner(self, senate: str):
        senate = list(senate)
        D, R = collections.deque(), collections.deque()
        off = len(senate)
        for idex in range(len(senate)):
            if senate[idex] == "R":
                R.append(idex)
            else:
                D.append(idex)
                
        while D and R:
            Dq1, Rq1 = D.popleft(), R.popleft()
            if Dq1 < Rq1:
                D.append(Dq1 + off)
            else:
                R.append(Rq1 + off)
        return 'Radiant' if R else "Dire"


x = solution()
print(x.predictPartyWinner("RD"))
print(x.predictPartyWinner("RDD"))
