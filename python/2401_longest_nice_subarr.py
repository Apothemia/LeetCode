from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
         8: 001000 | ws=0
         1: 000001 |
        11: 001011 | we=2
        48: 110000 |
         4: 000100 |
         !conflict | max_len=max(0, 2-0) = 2

         8: 001000 |
         1: 000001 |
        11: 001011 | ws=2
        48: 110000 |
         4: 000100 |
              !end | we=5 -> max_len=max(2, 5-2) = 3
        """
        window_start = window_end = max_len = bit_check = 0
        while window_end < len(nums):
            if max_len == 30:
                return max_len

            while bit_check & nums[window_end] != 0:
                max_len = max(max_len, window_end - window_start)
                bit_check ^= nums[window_start]
                window_start += 1

            bit_check |= nums[window_end]
            window_end += 1

        return max(max_len, window_end - window_start)


if __name__ == '__main__':
    s = Solution()
    inputs = [[1, 3, 8, 48, 10], [3, 1, 5, 11, 13], [8, 1, 11, 48, 4]]

    selected_input = 2
    print(s.longestNiceSubarray(inputs[selected_input]))
