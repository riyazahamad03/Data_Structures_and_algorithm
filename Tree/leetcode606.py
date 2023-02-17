class TreeNode:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None
        

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):

        newNode = TreeNode(data)
        if (self.root == None):
            self.root = newNode
        else:
            currNode = self.root
            while True:
                if (data < currNode.val):
                    if(currNode.left == None):
                        currNode.left = newNode
                        return
                    else:
                        currNode = currNode.left
                elif(data > currNode.val):
                    if(currNode.right == None):
                        currNode.right = newNode
                        return
                    else:
                        currNode = currNode.right

class solution:
    def class2str(self,root:TreeNode):
        res = []

        def preOrder(root):
            if not root:
                return 
            res.append('(')
            res.append(str(root.val))

            if not root.left and root.right:
                res.append("()")
            
            preOrder(root.left)
            preOrder(root.right)

            res.append(')')
        preOrder(root)
        return "".join(res)[1:-1]

root = Tree()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)

x = solution()
print(x.class2str(root.root))