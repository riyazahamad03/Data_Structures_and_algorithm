class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tot = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                tot[5] += 1
            elif bill == 10:
                if tot[5] > 0:
                    tot[5] -= 1
                    tot[10] += 1
                else:
                    return False
            elif bill == 20:
                if tot[10] > 0 and tot[5] > 0:
                    tot[10] -= 1
                    tot[5] -= 1
                    tot[20] += 1
                elif tot[5] >= 3:
                    tot[5] -= 3
                    tot[20] += 1
                else:
                    return False
        return True


x = Solution()
print(x.lemonadeChange(bills=[5, 5, 10, 10, 20]))
