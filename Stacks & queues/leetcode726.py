from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        while i < len(formula):
            if formula[i] == "(":
                stack.append(defaultdict(int))
            elif formula[i] == ")":
                cur_map = stack.pop()
                count = ""
                while i + 1 < len(formula) and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                prev_map = stack[-1]
                for elem in cur_map:
                    prev_map[elem] += cur_map[elem] * count

            else:
                element = formula[i]
                if i + 1 < len(formula) and formula[i + 1].islower():
                    element = formula[i : i + 2]
                    i += 1
                count = ""
                while i + 1 < len(formula) and formula[i + 1].isdigit():
                    count += formula[i + 1]
                    i += 1
                count = 1 if not count else int(count)
                cur_map = stack[-1]
                cur_map[element] += count

            i += 1

        cnt_map = stack[-1]
        res = ""
        for elem in sorted(cnt_map.keys()):
            count = "" if cnt_map[elem] == 1 else cnt_map[elem]
            res += elem + str(count)
        return res


x = Solution()
print(x.countOfAtoms(formula="K4(ON(SO3)2)2"))
