def num_steps_no_overflow(s):
    step = 0
    s_binary = int(s, 2)
    while s_binary != 1:
        step += 1
        if s_binary % 2 == 0:
            s_binary = s_binary // 2
        else:
            s_binary += 1
    return step


def num_steps(s):
    max_digits = 31
    step = 0
    overflow = None

    if len(s) > max_digits:
        overflow = s[:-max_digits]
        s = s[-max_digits:]

    s_binary = int(s, 2)
    while s_binary != 1:
        if s_binary % 2 == 0:
            s_binary /= 2
        else:
            s_binary += 1
        step += 1

    if overflow:
        overflow_binary = int(overflow, 2)
        while overflow_binary != 1:
            if overflow_binary % 2 == 0:
                overflow_binary /= 2
            else:
                overflow_binary += 1
            step += 1

    return step


def num_steps_shift(s):

    s_r = s[::-1]

    if len(s_r) > 31:
        s_overflow = s_r[32:]
        s_r = s_r[:32]

    steps = 0

    while s_r != '1':
        if s_r[0] == '1':
            s_r.replace('0', '1', 1)
            s_r = '0' + s_r[1:]
        else:
            s_r = s_r[1:]
        steps += 1
        print(s_r)

    return steps


if __name__ == '__main__':
    input_str = '1111011110000011100000110001011011110010111001010111110001'

    print('Number:', int(input_str, 2))
    print('Normal Calc:', num_steps_no_overflow(input_str))
    print('Overflow Split:', num_steps(input_str))
    # print('List Shift:', num_steps_shift(input_str))
