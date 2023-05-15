class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Length = 0

    def add(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.Length += 1
class Solution:
    def swapNodes(self, head: Node, k: int):
        curr = head
        for _ in range(k - 1):
            curr = curr.next
        l = curr
        r = head
        while curr.next:
            curr = curr.next
            r = r.next
        l.data, r.data = r.data, l.data
        return head


nodes = LinkedList()
nodes.add(1)
nodes.add(2)
nodes.add(3)
nodes.add(4)
nodes.add(5)

x = Solution()
newHead = x.swapNodes(nodes.head, 2)

current = newHead
while current.next:
    print(current.data , end= " ----> ")
    current = current.next
print(current.data)