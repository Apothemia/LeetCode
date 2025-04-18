import pytest


class Solution:
    def countAndSay(self, n: int) -> str:
        def digit_frequencies(s) -> list:
            frequencies = []
            count, last_digit = 1, s[0]
            for digit in (s + '$')[1:]:
                if digit != last_digit:
                    frequencies.append([count, last_digit])
                    count, last_digit = 0, digit
                count += 1
            return frequencies

        say_str = '1'
        for i in range(n - 1):
            say_str = ''.join(f'{freq[0]}{freq[1]}' for freq in digit_frequencies(say_str))
        return say_str


@pytest.mark.parametrize('n, out', [
    (4, '1211'),
    (1, '1'),
])
def test_all(n, out):
    test_sol = Solution()
    assert test_sol.countAndSay(n) == out
