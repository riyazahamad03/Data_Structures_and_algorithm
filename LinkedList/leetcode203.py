class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Node, val: int):
        dummy = Node(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


node = Node(0)
node.next = Node(1)
node.next.next = Node(1)
node.next.next.next = Node(0)

x = Solution()

print(x.removeElements(node, 1))
