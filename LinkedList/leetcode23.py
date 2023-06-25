class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        newNode = ListNode(data)
        if not self.head:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode


class solution:
    def mergeKLists(self, lists: list[ListNode]):

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i+1) < len(lists) else None
                mergedList.append(self.kMergeLists(list1, list2))
            lists = mergedList
        return lists[0]

    def kMergeLists(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


l1 = LinkedList()
l1.add(1)
l1.add(4)
l1.add(5)


l2 = LinkedList()
l2.add(1)
l2.add(3)
l2.add(4)

l3 = LinkedList()
l3.add(2)
l3.add(6)

lists = [l1.head, l2.head, l3.head]

x = solution()
res = x.mergeKLists(lists)

# printing the result
while res:
    print(res.val, end=" ")
    res = res.next
