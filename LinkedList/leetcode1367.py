# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head, root) -> bool:
        def helper(list_node, tree_node):
            if not list_node:
                return True
            if not tree_node or list_node.val != tree_node.val:
                return False

            return helper(list_node.next, tree_node.left) or helper(
                list_node.next, tree_node.right
            )

        if helper(head, root):
            return True
        if not root:
            return False
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


x = Solution()
bin_tree = TreeNode(5)
bin_tree.left = TreeNode(6)
bin_tree.right = TreeNode(7)

linked_list = ListNode(5)
linked_list.next = ListNode(6)
linked_list.next.next = ListNode(7)

print(x.isSubPath(linked_list, bin_tree))
