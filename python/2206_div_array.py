from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                num_set.remove(num)

        return len(num_set) == 0


if __name__ == '__main__':
    s = Solution()
    inputs = [[3, 2, 3, 2, 2, 2], [1, 2, 3, 4]]

    selected_input = 0
    print(s.divideArray(nums=inputs[selected_input]))
