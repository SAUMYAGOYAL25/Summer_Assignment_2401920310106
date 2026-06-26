# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, None, None)

    def helper(self, node, low, high):
        if not node:
            return True

        if low is not None and node.val <= low:
            return False

        if high is not None and node.val >= high:
            return False

        return self.helper(node.left, low, node.val) and \
               self.helper(node.right, node.val, high)
