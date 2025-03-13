def reverse(x: int):
    negativity = -1 if x < 0 else 1
    reversed_x = int(str(abs(x))[::-1]) * negativity
    if -2 ** 31 < reversed_x < 2 ** 31 - 1:
        return reversed_x
    return 0


if __name__ == '__main__':
    num = -123
    print(reverse(num))
