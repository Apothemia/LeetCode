from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations_done = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = abs(nums[i] - 1)
                nums[i + 1] = abs(nums[i + 1] - 1)
                nums[i + 2] = abs(nums[i + 2] - 1)
                operations_done += 1

        return operations_done if sum(nums[-2:]) == 2 else -1


if __name__ == '__main__':
    s = Solution()
    inputs = [[0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1, 1]]

    selected_input = 1
    print(s.minOperations(nums=inputs[selected_input]))
