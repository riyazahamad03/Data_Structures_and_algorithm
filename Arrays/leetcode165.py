class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_split, v2_split = version1.split("."), version2.split(".")
        v1, v2 = 0, 0
        v1_length, v2_length = len(v1_split), len(v2_split)
        v1_val, v2_val = 0, 0
        while v1 < v1_length or v2 < v2_length:
            if v1 < v1_length:
                v1_val = v1_val * 10 + int(v1_split[v1])
            else:
                v1_val *= 10

            if v2 < v2_length:
                v2_val = v2_val * 10 + int(v2_split[v2])
            else:
                v2_val *= 10
            v1, v2 = v1 + 1, v2 + 1

        if v1_val > v2_val:
            return 1
        elif v2_val > v1_val:
            return -1
        else:
            return 0


x = Solution()
print(x.compareVersion("1.01", "1.001"))
