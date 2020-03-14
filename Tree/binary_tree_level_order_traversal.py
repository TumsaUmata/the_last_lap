from collections import deque


class TreeNode:
    def __int__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result
