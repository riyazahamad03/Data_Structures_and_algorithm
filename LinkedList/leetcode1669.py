# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        left = ListNode(-1, list1)
        right = list1
        dummy = left
        diff = b - a
        while diff > 0:
            right = right.next
            diff -= 1

        while a > 0:
            left = left.next
            right = right.next
            a -= 1
        end = list2
        while end and end.next:
            end = end.next

        left.next = list2
        end.next = right.next
        return dummy.next


node1 = ListNode(10)
node1.next = ListNode(1)
node1.next.next = ListNode(13)
node1.next.next.next = ListNode(6)
node1.next.next.next.next = ListNode(9)
node1.next.next.next.next.next = ListNode(5)


node2 = ListNode(10000)
node2.next = ListNode(100001)
node2.next.next = ListNode(100002)


x = Solution()
print(x.mergeInBetween(node1, 3, 5, node2))
