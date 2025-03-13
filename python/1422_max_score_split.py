class Solution:
    def maxScore(self, s: str) -> int:

        max_score = 0

        zeroes = 0
        ones = s.count('1')
        for i in range(1, len(s)):
            if s[i] == '0':
                zeroes += 1
            else:
                ones -= 1
            max_score = max(max_score, zeroes + ones)

        return max_score


if __name__ == '__main__':
    input_str = '011101'

    s = Solution()
    # print(s.maxScore(input_str))

    med_values = [1, 2, 1, 0, 3, 4, 1, 0, 6, 2]
    med_val_index = [(med_values[i], i) for i in range(len(med_values))]
    print('MED Values:', med_values)
    print(med_val_index)

    sorted_med = list(sorted(med_val_index, key=lambda x: x[0]))
    print(sorted_med)

    print('Minimum MED indices:', [pair[1] for pair in sorted_med[:5]])
    