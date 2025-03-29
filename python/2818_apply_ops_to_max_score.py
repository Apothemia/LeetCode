import pytest
from typing import List
from heapq import heapify, heappop


class Solution:
    def find_prime_score(self, num):
        prime_factors = set()
        if num <= 1:
            return 0
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                prime_factors.add(i)
                num /= i
        if num > 1:
            prime_factors.add(num)
        return len(prime_factors)

    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        max_score = 1
        scored_nums = [(-num, self.find_prime_score(num), i) for i, num in enumerate(nums)]

        left, right, stack = [-1] * n, [n] * n, []
        for _, score, index in scored_nums:
            while stack and scored_nums[stack[-1]][1] < score:
                right[stack.pop()] = index
            if stack:
                left[index] = stack[-1]
            stack.append(index)

        heapify(scored_nums)
        while k > 0:
            num, score, index = heappop(scored_nums)
            num *= -1
            ops = min(k, (index - left[index]) * (right[index] - index))
            k -= ops
            max_score = (max_score * pow(num, ops, mod)) % mod
        return max_score


@pytest.mark.parametrize('nums, k, out', [
    ([3289, 2832, 14858, 22011], 6, 256720975),
    ([8, 3, 9, 3, 8], 2, 81),
    ([19, 12, 14, 6, 10, 18], 3, 4788),
])
def test_all(nums, k, out):
    test_sol = Solution()
    assert test_sol.maximumScore(nums, k) == out


@pytest.mark.parametrize('num, out', [
    (1, 0), (2, 1), (3, 1), (4, 1),
    (3289, 3), (2832, 3), (14858, 4), (22011, 4)
])
def test_factorization(num, out):
    test_sol = Solution()
    assert test_sol.find_prime_score(num) == out
