import pytest


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Even indices -> [0, 2, 4, 6, 8] = 5 possible digits
        # Odd indices  -> [2, 3, 5, 7]    = 4 possible digits
        # n = 5
        #     0   1   2   3
        #     5 x 4 x 5 x 4 = 400
        mod = 10 ** 9 + 7
        num_of_odd_indices = n // 2
        return (pow(4, num_of_odd_indices, mod) * pow(5, n - num_of_odd_indices, mod)) % mod


@pytest.mark.parametrize('n, out', [
    (1, 5),
    (4, 400),
    (50, 564908303),
    (806166225460393, 643535977)
])
def test_all(n, out):
    test_sol = Solution()
    assert test_sol.countGoodNumbers(n) == out
