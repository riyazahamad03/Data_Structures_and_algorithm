# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        def reverse(head):
            prev, curr = None, head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        head = reverse(head)
        curr = head
        curr_max = curr.val
        while curr.next:
            if curr.next.val < curr_max:
                curr.next = curr.next.next
            else:
                curr_max = curr.next.val
                curr = curr.next
        return reverse(head)


head = ListNode()
head.next = ListNode(4)
head.next.next = ListNode(5)
head.next.next.next = ListNode(10)
head.next.next.next.next = ListNode(3)

x = Solution()
print(x.removeNodes(head))
