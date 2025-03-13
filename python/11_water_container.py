def max_area(height: list[int]) -> int:
    most_area = min(height[0], height[-1]) * (len(height) - 1)
    left_idx = 0
    right_idx = len(height) - 1

    for _ in range(len(height)):
        if height[left_idx] < height[right_idx]:
            area = height[left_idx] * (right_idx - left_idx)
            left_idx += 1
        else:
            area = height[right_idx] * (right_idx - left_idx)
            right_idx -= 1

        if area > most_area:
            most_area = area

    return most_area


if __name__ == '__main__':
    height_list = [2, 3, 4, 5, 18, 17, 6]
    print(max_area(height=height_list))
