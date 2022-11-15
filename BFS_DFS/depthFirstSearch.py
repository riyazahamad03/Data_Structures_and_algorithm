
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class DFS():
    def __init__(self):
        self.root = None
    def insert(self,data):
        NewNode = Node(data)
        if self.root == None:
            self.root = NewNode
            return self
        else:
            currentNode = self.root
            while(True):
                if data < currentNode.data:
                    if currentNode.left == None:
                        currentNode.left = NewNode
                        return
                    else:
                        currentNode = currentNode.left
                elif data > currentNode.data:
                    if currentNode.right == None:
                        currentNode.right = NewNode
                        return
                    else:
                        currentNode = currentNode.right

            
    def Lookup(self,data):
        currentNode = self.root
        if currentNode == None:
            return False
        if currentNode == currentNode.data:
            return True
        elif data < currentNode.data:
            currentNode = currentNode.left
        else :
            currentNode = currentNode.right

    # Inorder : left -- > root -- > right
    # PreOrder : root --> left --> right 
    # PostOrder : left --> right --> root 


    def InOrderTraversal(self,root,res):
        if root.left:
            self.InOrderTraversal(root.left,res)
        res.append(root.data)
        if root.right:
            self.InOrderTraversal(root.right,res)
        return res

    def PreOrderTraversal(self,root,res):
        res.append(root.data)
        if root.left:
            self.PreOrderTraversal(root.left,res)
        if root.right:
            self.PreOrderTraversal(root.right,res)
        
        return res


    def PostOrderTraversal(self,root,res):
        if root.left:
            self.PostOrderTraversal(root.left,res)
        if root.right:
            self.PostOrderTraversal(root.right,res)
        res.append(root.data)
        return res

    # program to find the lead node sum
    def LeafNodeSum(self,node,lst):
        if not node:
            return 0 
        if node.left == None or node.right == None:
            lst.append(node.data)
        self.LeafNodeSum(node.left,lst)
        self.LeafNodeSum(node.right,lst) 
        return sum(lst)
    # LeetCode 98 Validate Bst Using Dfs Traversal
    def ValidateBst(self,node,left,right):
        if not node:
            return True
        if not(node.data < right and node.data > left ):
            return False
        return (self.ValidateBst(node.left,left,node.data) and self.ValidateBst(node.right,node.data,right))

    


tree = DFS()
tree.insert(9)
tree.insert(5)
tree.insert(20)
tree.insert(30)
tree.insert(15)
print(tree.InOrderTraversal(tree.root,[]))
print(tree.PostOrderTraversal(tree.root,[]))
print(tree.PreOrderTraversal(tree.root,[]))

print(tree.ValidateBst(tree.root,float("-inf"),float("inf")))
print(tree.LeafNodeSum(tree.root,[]))