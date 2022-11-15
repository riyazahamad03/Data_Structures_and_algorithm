from requests import head


class Node():
    def __init__(self,data):
        self.data = data
        self.next=None
class FirstLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        NewNode=Node(data)
        if self.head == None:
            self.head=NewNode
            self.tail = self.head
            self.length=1
        else:
            self.tail.next = NewNode
            self.tail = NewNode
            self.length+=1
    def pop(self):
        prev = self.head

        while prev.next != self.tail:
            prev = prev.next

        prev.next = None
        self.tail = prev
        return self.tail.data
        

l=FirstLinkedList()
l.append(1021)
l.append(1)
l.append(21)
l.append(41)
l.append(31)
l.pop()
print(l.tail.data)     