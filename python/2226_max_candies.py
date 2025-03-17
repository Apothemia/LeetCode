from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        start = 0
        end = max(candies)

        while start < end:
            mid = (start + end + 1) // 2
            dist_candies = sum(candy // mid for candy in candies)

            if dist_candies >= k:
                start = mid
            else:
                end = mid - 1

        return start


if __name__ == '__main__':
    s = Solution()
    inputs = [([5, 8, 6], 3)]

    selected_input = 0
    print(s.maximumCandies(inputs[selected_input][0], inputs[selected_input][1]))
