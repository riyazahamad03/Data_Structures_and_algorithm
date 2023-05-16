class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
class solution:
    def swapPairs(self , head : Node):
        dummyNode = Node(0)
        slow , fast = dummyNode , head
        
        while fast and fast.next:
            nextPair = fast.next.next
            second = fast.next

            second.next = fast
            fast.next = nextPair
            slow.next = second

            slow = fast
            fast = nextPair

        return dummyNode.next
    
nodes = LinkedList()
nodes.add(1)
nodes.add(2)
nodes.add(3)
nodes.add(4)
nodes.add(5)

x = solution()
newHead = x.swapPairs(nodes.head)

current = newHead
while current.next:
    print(current.data , end= " ----> ")
    current = current.next
print(current.data)