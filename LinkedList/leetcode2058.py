# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        def is_critical(prev, cur, nxt):
            return prev.val > cur.val < nxt.val or prev.val < cur.val > nxt.val

        if not head or not head.next or not head.next.next:
            return [-1, -1]

        prev, cur, nxt = head, head.next, head.next.next
        min_dist, max_dist = float("inf"), -1
        first_crit_idx, prev_crit_idx = -1, -1
        i = 1

        while nxt:
            if is_critical(prev, cur, nxt):
                if first_crit_idx == -1:
                    first_crit_idx = i
                else:
                    min_dist = min(min_dist, i - prev_crit_idx)
                prev_crit_idx = i
                max_dist = i - first_crit_idx
            prev, cur, nxt = cur, nxt, nxt.next
            i += 1

        if min_dist == float("inf"):
            min_dist = -1

        return [min_dist, max_dist]


x = Solution()
head = ListNode(0)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
print(x.nodesBetweenCriticalPoints(head))
