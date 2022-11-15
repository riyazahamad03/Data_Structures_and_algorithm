class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
# Insert Node
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
# Preorder traversal
# Root -> Left ->Right
# Inorder Traversal 
# left -> root -> right
# postorder traversal 
# left -> right -> root
   def PreorderTraversal(self, root):
    res = []
    if root!=None:
        #  res.append(root.data) 
        # preorder
        res = res + self.PreorderTraversal(root.left)
        res.append(root.data) 
        # inorder
        # print(res)
        res = res + self.PreorderTraversal(root.right)
        # res.append(root.data) 
        # postorder
    return res
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
# root.PrintTree()
print(root.PreorderTraversal(root))