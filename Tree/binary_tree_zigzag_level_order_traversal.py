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
        flag = False
        queue.appendleft(root)
        while queue:
            length = len(queue)
            level = []
            for _ in range(length):
                if flag:
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
            flag = not flag
        return result
