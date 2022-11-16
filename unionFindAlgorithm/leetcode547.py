
'''
Leetcode : 547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.

'''

'''

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

'''

class numberOfProvinces:
    def Union(self,x,y,lst):
        parentX = self.findParent(x,lst)
        parentY = self.findParent(y,lst) 
        if parentX == parentY:
            return False
        lst[parentX] = parentY
        return True
    
    def findParent(self,x,lst):
        if x != lst[x]:
            lst[x] = self.findParent(lst[x],lst)
        return lst[x]

    
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        dsu = numberOfProvinces()
        n = len(isConnected)
        lst = [i for i in range(n)]
        res = n
        for i in range(n):
            for j in range(i,n):
                if isConnected[i][j] == 1 and  dsu.Union(i,j,lst) :
                    res-=1
        return res
X = numberOfProvinces()

print(X.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))


