# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


root = ListNode(5)
root.next = ListNode(6)
root.next.next = ListNode(55)
root.next.next.next = ListNode(3)

x = Solution()
print(x.middleNode(root))
