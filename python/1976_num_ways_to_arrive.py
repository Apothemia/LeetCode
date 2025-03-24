from collections import defaultdict
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 1_000_000_007

        edge_map = defaultdict(list)
        for road in roads:
            edge_map[road[0]].append((road[1], road[2]))
            edge_map[road[1]].append((road[0], road[2]))

        distances = [0] + [float('inf')] * (n - 1)
        num_of_ways = 0

        queue = [(0, 0, '0')]
        while len(queue) > 0:
            curr_w, curr_node, curr_info = queue.pop(0)

            if curr_w > distances[curr_node]:
                continue

            if curr_node == n - 1 and curr_w == distances[-1]:
                num_of_ways += 1
                continue

            for adj_node, adj_w in edge_map[curr_node]:
                total_w = curr_w + adj_w
                if total_w <= distances[adj_node]:
                    queue.append((total_w, adj_node, curr_info + '->' + str(adj_node)))
                if total_w < distances[adj_node]:
                    num_of_ways = 0
                    distances[adj_node] = total_w
            queue.sort()

        return num_of_ways


if __name__ == '__main__':
    s = Solution()
    inputs = [{'n': 7, 'roads': [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                                 [0, 4, 5], [4, 6, 2]]}]

    input_idx = 0
    print(s.countPaths(inputs[input_idx]['n'], inputs[input_idx]['roads']))
