class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class myHashSet:
    def __init__(self) -> None:
        self.hashMap = [ListNode(0) for _ in range(10 ** 4)]

    def add(self, key):
        cur = self.hashMap[key % len(self.hashMap)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key):
        cur = self.hashMap[key % len(self.hashMap)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key):
        cur = self.hashMap[key % len(self.hashMap)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False


myHashSet = myHashSet()
myHashSet.add(1)      
myHashSet.add(2)
myHashSet.contains(1)
myHashSet.contains(3)
myHashSet.add(2)
myHashSet.contains(2)
myHashSet.remove(2)
myHashSet.contains(2)