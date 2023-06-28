class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


class Codec:
    def serialize(self, root: TreeNode):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.idx = 0

        def dfs():
            if vals[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(vals[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


root = Tree()
root.insert(10)
root.insert(2)
root.insert(14)
root.insert(4)
root.insert(11)
root.insert(22)

ser = Codec()
deser = Codec()

ans = deser.deserialize(ser.serialize(root.root))


def printAns(node):
    if not node:
        return None
    print(node.val, end=" ")
    printAns(node.left)
    printAns(node.right)


printAns(ans)
