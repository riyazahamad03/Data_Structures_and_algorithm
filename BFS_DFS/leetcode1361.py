import collections


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: list[int], rightChild: list[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            print(children)
            for i in range(n):
                if i not in children:
                    return i
            return -1

        root = find_root()
        if root == -1:
            return False

        q = collections.deque([root])
        visit = set([root])
        while q:
            node = q.popleft()
            for nei in [leftChild[node], rightChild[node]]:
                if nei != -1:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
                    else:
                        return False
        return len(visit) == n


x = Solution()
print(x.validateBinaryTreeNodes(n=2, leftChild=[1, 0], rightChild=[-1, -1]))
