import pytest
from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            return len([num for num in range(1, 10) if num % k == 0])
        good_int_count = 0
        digit_combinations = set()
        mid_point = (n + 1) // 2
        for half in range(10 ** (mid_point - 1), 10 ** mid_point):
            half_str = str(half)
            if n % 2 == 0:
                full_str = half_str + half_str[::-1]
            else:
                full_str = half_str + half_str[-2::-1]
            palindrome_num = int(full_str)
            if palindrome_num % k == 0:
                digit_counts = tuple(Counter(full_str).items())
                dict_key = [f'{i}:0' for i in range(10)]
                for digit, count_value in digit_counts:
                    dict_key[int(digit)] = f'{digit}:{count_value}'
                dict_key = '-'.join(dict_key)
                if dict_key not in digit_combinations:
                    numerator, denominator = 0, 1
                    zero_count = 0
                    for digit, count_value in digit_counts:
                        if digit == '0':
                            zero_count = count_value
                        numerator += count_value
                        denominator *= factorial(count_value)
                    total_permutations = factorial(numerator) / denominator
                    # If there is a 0 among the digits, it cannot be used as the first digit
                    # n!/(f0!*f1!*...) - (n-1)!/((f0-1)!*f1!*...) = (n-1)!/((f0-1)!*f1!*...) * (n/f0 - 1).
                    # So, if 0 exists, I can convert the non-zero answer by multiplying the result with (1 - f0/n)
                    if zero_count != 0:
                        total_permutations *= 1 - zero_count / numerator
                    good_int_count += round(total_permutations)
                    digit_combinations.add(dict_key)
        return good_int_count


@pytest.mark.parametrize('n, k, out', [
    (3, 5, 27),
    (1, 4, 2),
    (5, 6, 2468),
    (10, 1, 41457024),
    (6, 1, 10944),
])
def test_all(n, k, out):
    test_sol = Solution()
    assert test_sol.countGoodIntegers(n, k) == out
