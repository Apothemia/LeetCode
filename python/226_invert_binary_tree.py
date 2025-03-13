from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode[{self.val}]'


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return TreeNode()

        queue = [root]

        while queue:
            curr_node = queue.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

        return root


def initialize_tree(node_list):
    if not node_list:
        return None

    root = TreeNode(node_list[0])
    queue = [root]
    index = 1

    while queue and index < len(node_list):
        current = queue.pop(0)

        if index < len(node_list):
            current.left = TreeNode(node_list[index])
            queue.append(current.left)
            index += 1

        if index < len(node_list):
            current.right = TreeNode(node_list[index])
            queue.append(current.right)
            index += 1

    return root


def display_tree(root):
    if not root:
        print("Tree is empty")
        return

    queue = deque([(root, 0)])  # Node and its level
    current_level = 0
    result = []

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            print(" ".join(str(n) if n is not None else "." for n in result))
            result = []
            current_level = level

        result.append(node.val if node else None)

        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

    print(" ".join(str(n) if n is not None else "." for n in result))


if __name__ == '__main__':
    # nodes = [4, 2, 7, 1, 3, 6, 9]
    nodes = [4]
    tree_root = initialize_tree(nodes)
    display_tree(tree_root)

    s = Solution()
    inverted_root = s.invertTree(tree_root)
    display_tree(inverted_root)
