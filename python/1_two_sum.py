def two_sum_solution(nums, target):
    index_list = list(range(len(nums)))
    nums_indices_sorted = sorted(zip(nums, index_list))

    i_start = 0
    i_end = len(nums) - 1
    while i_start != i_end:
        current_sum = nums_indices_sorted[i_start][0] + nums_indices_sorted[i_end][0]

        if current_sum == target:
            return [nums_indices_sorted[i_start][1], nums_indices_sorted[i_end][1]]

        if current_sum > target:
            i_end -= 1
        else:
            i_start += 1

    return None


if __name__ == '__main__':
    n = [0, 4, 3, 0]
    t = 0
    print(two_sum_solution(n, t))
