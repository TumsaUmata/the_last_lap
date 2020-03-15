from collections import deque


class TreeNode:
    def __init(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrderNoReverse(self, root):
        if not root:
            return []
        result, queue = [], deque()
        zigzag = False
        queue.appendleft(root)
        while queue:
            cnt = len(queue)
            level = []
            for _ in range(cnt):
                if zigzag:
                    node = queue.pop()
                    level.append(node.val)
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)
                else:
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            result.append(level)
            zigzag = not zigzag
        return result
