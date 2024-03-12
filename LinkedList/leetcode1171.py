# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: ListNode):
        dummy = ListNode(0, head)
        start = dummy
        while start:
            pref = 0
            end = start.next

            while end:
                pref += end.val

                if pref == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return dummy.next


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(-3)
root.next.next.next = ListNode(3)
root.next.next.next.next = ListNode(1)
x = Solution()
print(x.removeZeroSumSublists(root))
