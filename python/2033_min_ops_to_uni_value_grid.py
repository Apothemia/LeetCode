from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat_list = []
        mod = grid[0][0] % x
        for grid_row in grid:
            for num in grid_row:
                if num % x != mod:
                    return -1
                flat_list.append(num // x)
        print(flat_list)
        flat_list.sort()

        uni_val = flat_list[len(flat_list) // 2]
        return sum(abs(num - uni_val) for num in flat_list)


if __name__ == '__main__':
    s = Solution()
    inputs = [{'grid': [[2, 4], [6, 8]], 'x': 2}]

    in_idx = 0
    print(s.minOperations(inputs[in_idx]['grid'], inputs[in_idx]['x']))
