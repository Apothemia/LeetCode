import pytest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'<{self.val}>'

    def __repr__(self):
        return f'<{self.val}>'


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_lca(curr_node, depth):
            if curr_node is None:
                return curr_node, depth
            left_lca, left_depth = find_lca(curr_node.left, depth + 1)
            right_lca, right_depth = find_lca(curr_node.right, depth + 1)
            if left_depth > right_depth:
                return left_lca, left_depth
            elif left_depth < right_depth:
                return right_lca, right_depth
            return curr_node, right_depth

        return find_lca(root, 0)[0]

    def construct_tree(self, nodes):
        root = TreeNode(val=nodes.pop(0))
        queue = [root]
        while len(nodes) > 0:
            curr_node = queue.pop(0)
            left_child, right_child = nodes.pop(0), nodes.pop(0)
            if left_child is not None:
                curr_node.left = TreeNode(val=left_child)
                queue.append(curr_node.left)
            if right_child is not None:
                curr_node.right = TreeNode(val=right_child)
                queue.append(curr_node.right)
        return root


@pytest.mark.parametrize('nodes, out', [
    ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [2, 7, 4]),
])
def test_lca_nodes_with_children(nodes, out):
    test_sol = Solution()
    root = test_sol.construct_tree(nodes)
    deepest_leaves = test_sol.lcaDeepestLeaves(root)
    assert [deepest_leaves.val, deepest_leaves.left.val, deepest_leaves.right.val] == out


@pytest.mark.parametrize('nodes, out', [
    ([1], [1]),
    ([0, 1, 3, None, 2], [2])
])
def test_single_lca_nodes(nodes, out):
    test_sol = Solution()
    root = test_sol.construct_tree(nodes)
    deepest_leaves = test_sol.lcaDeepestLeaves(root)
    assert [deepest_leaves.val] == out
