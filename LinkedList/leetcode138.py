class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class solution:
    def copyRandomList(self, head: Node):
        cur = head
        hashMap = {None: None}
        while cur:
            copy = Node(cur.val)
            hashMap[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = hashMap[cur]
            copy.next = hashMap[cur.next]
            copy.random = hashMap[cur.random]
            cur = cur.next
        return hashMap[head]


head = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
nodes = [Node(item[0]) for item in head]
for i, item in enumerate(head):
    if item[1] is not None:
        nodes[i].random = nodes[item[1]]

x = solution()
x.copyRandomList(nodes[0])
