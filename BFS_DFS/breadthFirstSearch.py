from collections import deque
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
class BFS():
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
    def breadthFirstSearch(self):
        MyList  = []
        queue = []
        currentNode = self.root
        queue.append(currentNode)

        while len(queue) > 0:
            currentNode = queue[0]
            # del queue[0]
            queue.pop(0)
            MyList.append(currentNode.data)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return MyList
    def breadthFirstSearchRecurrsive(self,queue,List):
        if len(queue) == 0:
            return List
        currentNode = queue[0]
        queue.pop(0)
        List.append(currentNode.data)
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        return self.breadthFirstSearchRecurrsive(queue,List)
    # program to find the maximum depth of bst using BFS
    # LeetCode Challenge: 104. Maximum Depth of Binary Tree
    def MaxDepth(self):
        if not self.root:
            return None
        level = 0 
        q = deque([self.root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level


x = BFS()
x.insert(10)
x.insert(20)
x.insert(5)
print(x.breadthFirstSearch())
print(x.breadthFirstSearchRecurrsive([x.root],[]))
print(x.MaxDepth())