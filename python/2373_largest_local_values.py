def largest_local(grid):
    max_local_grid = [[0 for _ in range(len(grid) - 2)] for _ in range(len(grid) - 2)]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            local_i_0 = grid[i - 1][j - 1:j + 2]
            local_i_1 = grid[i][j - 1:j + 2]
            local_i_2 = grid[i + 1][j - 1:j + 2]
            max_local_grid[i - 1][j - 1] = max(max(local_i_0), max(local_i_1), max(local_i_2))
    return max_local_grid


if __name__ == '__main__':
    sample_grid = [[9, 9, 8, 1],
                   [5, 6, 2, 6],
                   [8, 2, 6, 4],
                   [6, 2, 2, 2]]
    print(largest_local(sample_grid))
