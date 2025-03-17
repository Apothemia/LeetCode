from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        :param ranks: Ranks of mechanics. An r rank mechanic can repair n cars in r * n^2 minutes
        :param cars: The total number of cars waiting in the garage to be repaired
        :return: The minimum time taken to repair all the cars
        """

        low = 1
        high = max(rank * (cars // len(ranks) + 1) ** 2 for rank in ranks)

        while low < high:
            mid = (low + high) // 2

            if sum([int((mid / rank) ** 0.5) for rank in ranks]) >= cars:
                high = mid
            else:
                low = mid + 1

        return low


if __name__ == '__main__':
    s = Solution()
    inputs = [{'ranks': [1, 3, 1, 2, 1, 1], 'cars': 21}, {'ranks': [5, 1, 8], 'cars': 6}]

    selected_input = 0
    print(s.repairCars(ranks=inputs[selected_input]['ranks'], cars=inputs[selected_input]['cars']))
