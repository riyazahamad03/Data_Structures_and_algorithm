class soltution:

    def binarySearch(self, arr, tar):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2

            if arr[m] <= tar:
                l = m + 1
            else:
                r = m
        return l

    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        arr2.sort()
        hashMap = {}

        def dfs(i, prev):
            if i == len(arr1):
                return 0
            if (i, prev) in hashMap:
                return hashMap[(i, prev)]

            cost = float("inf")
            if (arr1[i] > prev):
                cost = dfs(i + 1, arr1[i])

            idex = self.binarySearch(arr2, prev)
            if idex < len(arr2):
                cost = min(cost, 1 + dfs(i + 1, arr2[idex]))

            hashMap[(i, prev)] = cost
            return cost
        res = dfs(0, - 1)
        return res if res != float("inf") else -1


x = soltution()

print(x.makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]))
