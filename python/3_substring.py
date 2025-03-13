def length_of_longest_unique_substring(s):
    longest_substring = ''
    i_start = 0

    for i_end in range(len(s)):
        substring = s[i_start:i_end]
        # print(f'{s[i_end]} -> "{substring}"')

        if s[i_end] in substring:
            i_start = i_end - len(substring) + substring.index(s[i_end]) + 1
        else:
            substring += s[i_end]

        if len(longest_substring) <= len(substring):
            longest_substring = substring
            # print('Longest =', longest_substring, '\n')

    return len(longest_substring)

if __name__ == '__main__':
    string = 'asdasdcsf'
    print(length_of_longest_unique_substring(string))
