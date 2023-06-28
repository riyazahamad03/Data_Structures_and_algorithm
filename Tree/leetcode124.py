class TreeNode:
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val):
        newNode = TreeNode(val)
        if not self.root:
            self.root = newNode
        else:
            curr = self.root
            while True:
                if val < curr.val:
                    if curr.left == None:
                        curr.left = newNode
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = newNode
                        break
                    else:
                        curr = curr.right


class solution:
    def maxPathSum(self, root: TreeNode):
        res = root.val

        def dfs(root):
            if not root:
                return 0
            lftMax = dfs(root.left)
            rgtMax = dfs(root.right)

            lftMax = max(lftMax, 0)
            rgtMax = max(rgtMax, 0)

            print(root.val, lftMax, rgtMax)
            nonlocal res
            # with split
            res = max(res, root.val + lftMax, rgtMax)
            
            # withot split
            return root.val + max(lftMax, rgtMax)
        dfs(root)
        return res


root = Tree()
root.insert(10)
root.insert(2)
root.insert(14)
root.insert(4)
root.insert(11)
root.insert(22)

x = solution()
print(x.maxPathSum(root.root))
