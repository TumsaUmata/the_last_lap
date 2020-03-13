"""https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space"""


class NodeList:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        node = None
        while slow:
            next = slow.next
            slow.next = node
            node = slow
            slow = next

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
