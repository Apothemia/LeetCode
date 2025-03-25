from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        ranges_x = []
        ranges_y = []
        for rectangle in rectangles:
            ranges_x.append((rectangle[0], rectangle[2]))
            ranges_y.append((rectangle[1], rectangle[3]))

        ranges_x.sort()
        cuts = 0
        interval = ranges_x.pop(0)
        for next_interval in ranges_x:
            if next_interval[1] < interval[1]:
                continue
            if next_interval[0] < interval[1]:
                interval = [interval[0], next_interval[1]]
            else:
                cuts += 1
                interval = next_interval
            if cuts == 2:
                return True

        ranges_y.sort()
        cuts = 0
        interval = ranges_y.pop(0)
        for next_interval in ranges_y:
            if cuts == 2:
                return True
            if next_interval[1] < interval[1]:
                continue
            if next_interval[0] < interval[1]:
                interval = [interval[0], next_interval[1]]
            else:
                cuts += 1
                interval = next_interval
            if cuts == 2:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    inputs = [{'n': 5, 'rectangles': [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]}]

    input_idx = 0
    print(s.checkValidCuts(inputs[input_idx]['n'], inputs[input_idx]['rectangles']))
