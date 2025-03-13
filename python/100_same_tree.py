class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode[{self.val}]'


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        p_queue = [p]
        q_queue = [q]

        while p_queue:
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)

            if not p_curr and not q_curr:
                continue

            try:
                if p_curr.val != q_curr.val:
                    return False
            except:
                return False

            p_queue.extend([p_curr.left, p_curr.right])
            q_queue.extend([q_curr.left, q_curr.right])

        return True


if __name__ == '__main__':
    p_node = TreeNode(1, TreeNode(2), TreeNode(3))
    q_node = TreeNode(1, TreeNode(2), TreeNode(3))

    # p_node = TreeNode(1, None, None)
    # q_node = TreeNode(1, None, TreeNode(2))

    s = Solution()
    print(s.isSameTree(p_node, q_node))
