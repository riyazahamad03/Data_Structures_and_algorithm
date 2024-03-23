# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head) -> None:
        slow , fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first , second = head , prev
        while second:
            temp1 , temp2 = first.next , second.next
            first.next = second
            second.next = temp1
            first,second = temp1 , temp2
        return head
    
x = Solution()
node1 = ListNode(10)
node1.next = ListNode(1)
node1.next.next = ListNode(13)
node1.next.next.next = ListNode(6)
node1.next.next.next.next = ListNode(9)
node1.next.next.next.next.next = ListNode(5)

print(x.reorderList(node1))
