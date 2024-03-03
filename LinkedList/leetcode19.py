class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(-1, head)
        left = dummy
        right = dummy.next

        for _ in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next


root = ListNode(1, None)
root.next = ListNode(2, None)
root.next.next = ListNode(3, None)
root.next.next.next = ListNode(4, None)
root.next.next.next.next = ListNode(5, None)

x = Solution()
result = x.removeNthFromEnd(root, 2)


current = result
while current:
    print(current.val, end=" ")
    current = current.next
