def edit_dist_dp(s1, s2):
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                ins_cost = dp[i - 1][j]
                del_cost = dp[i][j - 1]
                rep_cost = dp[i - 1][j - 1]

                ins_del_min = min(ins_cost, del_cost)
                if rep_cost < ins_del_min:
                    dp[i][j] = rep_cost + 2
                else:
                    dp[i][j] = ins_del_min + 1

    i, j = m, n

    while i > 0 or j > 0:
        if s1[i - 1] == s2[j - 1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j - 1] + 2:
            print(f"Replace {s1[i - 1]} with {s2[j - 1]}")
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i][j - 1] + 1:
            print(f"Insert {s2[j - 1]}")
            j -= 1
        elif dp[i][j] == dp[i - 1][j] + 1:
            print(f"Delete {s1[i - 1]}")
            i -= 1

    print('    ' + ' '.join(word_1))
    for j in range(n + 1):
        if j != 0:
            print(word_2[j - 1] + ' ', end='')
        else:
            print('  ', end='')
        for i in range(m + 1):
            print(dp[i][j], end=' ')
        print()

    return dp[m][n]


# Driver code
word_1 = "altruism"
word_2 = "plasma"

'''
altruism
pltruism
plruism
pluism
plism
plasm
plasma
'''
print(edit_dist_dp(word_1, word_2))
