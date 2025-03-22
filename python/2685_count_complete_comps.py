from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        node_to_edges = {node: [] for node in range(n)}
        for edge in edges:
            node_to_edges[edge[0]].append(edge[1])
            node_to_edges[edge[1]].append(edge[0])

        complete_components = 0

        visited_nodes = set()
        for node in range(n):
            if not node in visited_nodes:
                component = []
                stack = [node]
                while len(stack) > 0:
                    curr_node = stack.pop(-1)
                    if curr_node not in visited_nodes:
                        component.append(curr_node)
                        visited_nodes.add(curr_node)
                    for adj_node in node_to_edges[curr_node]:
                        if adj_node not in visited_nodes:
                            stack.append(adj_node)

                is_complete = True
                for comp_node in component:
                    if len(component) - 1 != len(node_to_edges[comp_node]):
                        is_complete = False
                        break

                if is_complete:
                    complete_components += 1

        return complete_components


if __name__ == '__main__':
    s = Solution()
    inputs = [
        {'n': 4, 'edges': [[1, 0], [2, 0], [3, 1], [3, 2]]},
        {'n': 6, 'edges': [[0, 1], [0, 2], [1, 2], [3, 4]]},
        {'n': 6, 'edges': [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]}
    ]

    input_idx = 2
    print(s.countCompleteComponents(inputs[input_idx]['n'],
                                    inputs[input_idx]['edges']))
