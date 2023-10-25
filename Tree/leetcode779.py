class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n , val ,  nxtIndex):
            if n == 1:
                return nxtIndex
            tot = 2 ** (n - 1)

            if val > (tot/2):
                nxtIndex = 1 if nxtIndex == 0 else 0
                return dfs(n - 1 , val  - (tot/ 2) , nxtIndex )
            else:
                nxtIndex = 0 if nxtIndex == 0 else 1
                return dfs(n - 1 , val , nxtIndex)
        return dfs(n , k , 0)
x = Solution()
print(x.kthGrammar(n = 2, k = 2))