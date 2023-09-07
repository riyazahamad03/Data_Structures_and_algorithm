class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Node):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        l, r = head, prev
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True


node = Node(0)
node.next = Node(1)
node.next.next = Node(1)
node.next.next.next = Node(0)


X = Solution()
print(X.isPalindrome(node))
