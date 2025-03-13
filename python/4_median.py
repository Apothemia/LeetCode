def find_median_sorted_arrays(nums1, nums2):
    i_1 = 0
    i_2 = 0
    median_1 = -1
    median_2 = -1
    for i in range((len(nums1) + len(nums2)) // 2 + 1):
        median_2 = median_1
        if i_1 < len(nums1) and i_2 < len(nums2):
            if nums1[i_1] < nums2[i_2]:
                median_1 = nums1[i_1]
                i_1 += 1
            else:
                median_1 = nums2[i_2]
                i_2 += 1
        elif i_1 >= len(nums1):
            median_1 = nums2[i_2]
            i_2 += 1
        else:  # elif i_2 >= len(nums2)
            median_1 = nums1[i_1]
            i_1 += 1

    if (len(nums1) + len(nums2)) % 2 == 0:
        return (median_1 + median_2) / 2
    else:
        return median_1

# Faster solution xd
def just_sort(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    median = nums1[len(nums1) // 2]
    if len(nums1) % 2 == 0:
        median = (median + nums1[len(nums1) // 2 - 1]) / 2
    return median

if __name__ == '__main__':
    num_list_1 = [1, 3]
    num_list_2 = [2]
    print(just_sort(num_list_1, num_list_2))
