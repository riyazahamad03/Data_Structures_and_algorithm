class solution:
    def countRoutes(self, locations: list[int], start: int, finish: int, fuel: int):
        dp = {}
        mod = 10 ** 9 + 7

        def dfs(curCity, remFuel):
            if remFuel < 0:
                return 0
            if (curCity, remFuel) in dp:
                return dp[(curCity, remFuel)]

            ans = 0
            if curCity == finish:
                ans = 1

            for nxtCity in range(len(locations)):
                if nxtCity != curCity:
                    ans += dfs(nxtCity, remFuel -
                               abs(locations[curCity] - locations[nxtCity]))
            dp[(curCity, remFuel)] = ans
            return ans
        return dfs(start, fuel)


x = solution()
print(x.countRoutes(locations=[2, 3, 6, 8, 4], start=1, finish=3, fuel=5))
print(x.countRoutes(locations=[4, 3, 1], start=1, finish=0, fuel=6))
print(x.countRoutes(locations=[5, 2, 1], start=0, finish=2, fuel=3))
