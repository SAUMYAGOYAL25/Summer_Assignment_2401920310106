class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level = []
            size = len(queue)

            for i in xrange(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result
