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


class solution:
    def pairSum(self, head: Node):
        slow, fast = head, head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        res = 0
        while prev:
            res = max(res, prev.data + slow.data)
            prev = prev.next
            slow = slow.next
        return res


nodes = LinkedList()
nodes.add(1)
nodes.add(2)
nodes.add(3)
nodes.add(4)

x = solution()
print(x.pairSum(nodes.head))