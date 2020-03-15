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
        res, q = [], deque()
        zigzag = False
        q.appendleft(root)
        while q:
            cnt = len(q)
            level = []
            for _ in range(cnt):
                if zigzag:
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            res.append(level)
            zigzag = not zigzag
        return res
