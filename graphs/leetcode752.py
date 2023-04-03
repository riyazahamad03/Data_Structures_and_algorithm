import collections
class solution:
    def openLock(self , deadends : list[str] , target : str):
        if '0000' in deadends:
            return -1
        q = collections.deque()
        q.append(['0000' , 0]) #initial and Number of turns
        visitSet = set(deadends)
        def children(wheel):
            res = []
            for i in range(4):
                dig = str((int(wheel[i]) + 1) % 10)
                res.append(wheel[:i] + dig + wheel[i + 1:])
                dig = str((int(wheel[i]) - 1 + 10) % 10)
                res.append(wheel[:i] + dig + wheel[i + 1:])
            return res
        while q:
            lock , turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in  visitSet:
                    visitSet.add(child)
                    q.append([child , turns + 1])
        return -1
x = solution()
print(x.openLock(["0201","0101","0102","1212","2002"] , "0202"))
