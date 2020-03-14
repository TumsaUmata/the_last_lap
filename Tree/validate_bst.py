class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        minimum = float('-inf')
        maximum = float('+inf')
        return self.validate(root, minimum, maximum)

    def validate(self, root, minimum, maximum):
        if not root:
            return True
        if not root.left and not root.right:
            if minimum < root.val < maximum:
                return True
            else:
                return False
        if not root.left and root.right:
            return root.val < root.right.val \
                   and self.validate(root.right, root.val, maximum)
        elif root.left and not root.right:
            return root.left.val < root.val \
                   and self.validate(root.left, minimum, root.val)
        else:
            return root.left.val < root.val < root.right.val \
                   and self.validate(root.left, minimum, root.val) \
                   and self.validate(root.right, root.val, maximum)
