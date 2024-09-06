# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums, head):
        hashMap = set(nums)
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while prev.next:
            if curr.val in hashMap:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dummy.next


nodes = ListNode(5)
nodes.next = ListNode(6)
nodes.next.next = ListNode(7)
x = Solution()
x.modifiedList([1, 2, 4], nodes)
