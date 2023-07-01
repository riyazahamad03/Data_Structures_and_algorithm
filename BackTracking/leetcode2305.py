class solution:
    def distributeCookies(self, cookies: list[int], k: int):
        n = len(cookies)

        children = [0] * k

        ans = float('inf')

        def distribution(index):
            nonlocal ans
            if index >= n:
                return max(children)

            if max(children) >= ans:
                return ans

            for i in range(k):

                children[i] += cookies[index]

                current_unfairness = distribution(index+1)

                ans = min(ans, current_unfairness)
                children[i] -= cookies[index]

            return ans

        return distribution(0)


x = solution()
print(x.distributeCookies(cookies=[8, 15, 10, 20, 8], k=2))
