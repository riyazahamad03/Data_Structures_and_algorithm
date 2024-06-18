class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        vals = [[i, j] for i, j in zip(difficulty, profit)]
        worker.sort()
        vals.sort()

        net_profit, max_profit, idx = 0, 0, 0
        for ability in worker:
            while idx < len(difficulty) and ability >= vals[idx][0]:
                max_profit = max(max_profit, vals[idx][1])
                idx += 1
            net_profit += max_profit
        return net_profit


x = Solution()
print(
    x.maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[4, 5, 6, 7]
    )
)
