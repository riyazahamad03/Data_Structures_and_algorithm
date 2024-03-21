class LinkedList:
    def __init__(self , val : str , next = None):
        self.val = val
        self.next = next

class solution:
    def isCons(self, x):
        return x not in 'aeiouAEIOU'
    
    def deleteLastCons(self , head):
        dummy = LinkedList("-1" , head)
        deleteNode = None
        curr = dummy
        while curr and curr.next:
            if self.isCons(curr.next.val):
                deleteNode = curr
            curr = curr.next
        deleteNode.next = deleteNode.next.next
        return head
    

head = LinkedList("Q")
head.next = LinkedList("U")
head.next.next = LinkedList("E")
head.next.next.next = LinkedList("E")
head.next.next.next.next = LinkedList("N")

x = solution()
res = x.deleteLastCons(head)
while res:
    print(res.val)
    res = res.next