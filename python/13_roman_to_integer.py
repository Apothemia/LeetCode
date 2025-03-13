class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Symbol  Value
        I       1
        V       5
        X       10
        L       50
        C       100
        D       500
        M       1000
        """
        symbol_values = [1000, 500, 100, 50, 10, 5, 1]
        symbol_idx_dict = {'M': 0, 'D': 1, 'C': 2, 'L': 3, 'X': 4, 'V': 5, 'I': 6}

        int_sum = 0
        for i in range(len(s) - 1):
            curr_symbol_idx = symbol_idx_dict[s[i]]
            next_symbol_idx = symbol_idx_dict[s[i + 1]]

            if curr_symbol_idx > next_symbol_idx:
                int_sum -= symbol_values[curr_symbol_idx]
            else:
                int_sum += symbol_values[curr_symbol_idx]

        int_sum += symbol_values[symbol_idx_dict[s[-1]]]

        return int_sum


if __name__ == '__main__':
    s = Solution()
    roman_num = 'MCMXCIV'
    print(s.romanToInt(roman_num))
