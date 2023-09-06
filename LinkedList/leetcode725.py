class Node:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


class solution:
    def splitLinkedList(self, head: Node, k: int):
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1

        part, rem = length // k, length % k
        curr, res = head, []

        for _ in range(k):
            res.append(curr)
            for _ in range(part - 1 + (1 if rem else 0)):
                if not curr:
                    break
                curr = curr.next

            rem -= (1 if rem else 0)
            if curr:
                tmp = curr.next
                curr.next = None
                curr = tmp
        return res


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)


x = solution()
print(x.splitLinkedList(node, 3))
