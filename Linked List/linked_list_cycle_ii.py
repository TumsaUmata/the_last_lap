class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        entry = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return entry
        return None


class Solution2:
    def detectCycle(self, head):
        current = head
        visited = set()
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next
        return None
