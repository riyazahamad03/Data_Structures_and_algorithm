class treeNode:
    def __init__(self,val=0,left=None, right=None):
        self.root = None
        self.val = val
        self.left = left
        self.right = right
    def insert(self,data):
        NewNode = treeNode(data)
        if(self.root == None):
            self.root = NewNode
            return self
        else:
            currNode = self.root
            while(True):
                if(data<currNode.val):
                    if(currNode.left == None):
                        currNode.left = NewNode
                        return
                    else:
                        currNode=currNode.left
                elif (data>currNode.val):
                    if(currNode.right == None):
                        currNode.right = NewNode
                        return
                    else:
                        currNode = currNode.right
class solution:
    def mergeTree(self,t1:treeNode,t2:treeNode):
        if not t1 and not t2:
            return None
        
        val1 = t1.val if t1 else 0
        val2 = t2.val if t2 else 0
        
        root = treeNode(val1  + val2)
        root.left = self.mergeTree(t1.left if t1 else None , t2.left if t2 else None)
        root.right = self.mergeTree(t1.right if t1 else None ,t2.right if t2 else None)
        
        return root
    
t1 = treeNode()
t2 = treeNode()

t1.insert(1)
t1.insert(3)
t1.insert(2)
t1.insert(5)

t2.insert(2)
t2.insert(1)
t2.insert(3)
t2.insert(4)
t2.insert(7)

sol = solution()
print(sol.mergeTree(t1,t2))
