import pytest
from typing import List
from heapq import heappop, heappush


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # len(grid) = m x n, len(queries) = k
        # start top left cell of the matrix (grid[0][0])
        # +1 point if queries[i] > current_cell and first time visiting
        # move any adjacent cell in 4 directions
        # answer[i] = max num of points for queries[i]

        k = len(queries)
        m, n = len(grid), len(grid[0])
        queries = list(sorted([(queries[i], i) for i in range(k)]))

        queue = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        answers = [0] * k
        answer = 0
        for query, query_i in queries:
            while len(queue) > 0 and queue[0][0] < query:
                answer += 1
                cell_val, i, j = heappop(queue)
                adj_cells = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for adj_i, adj_j in adj_cells:
                    if 0 <= adj_i < m and 0 <= adj_j < n and (adj_i, adj_j) not in visited:
                        heappush(queue, (grid[adj_i][adj_j], adj_i, adj_j))
                        visited.add((adj_i, adj_j))
            answers[query_i] = answer
        return answers


@pytest.mark.parametrize('grid, queries, out', [
    ([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2], [5, 8, 1]),
    ([[5, 2, 1], [1, 1, 2]], [3], [0]),
    ([[249472, 735471, 144880, 992181, 760916, 920551, 898524, 37043, 422852, 194509, 714395, 325171], [295872, 922051, 900801, 634980, 644237, 912433, 857189, 98466, 725226, 984534, 370121, 399006], [618420, 573065, 587011, 298153, 694872, 12760, 880413, 593508, 474772, 291113, 852444, 77998], [67650, 426517, 146447, 190319, 379151, 184754, 479219, 106819, 138473, 865661, 799297, 228827], [390392, 789371, 772048, 730506, 7144, 862164, 650590, 21524, 879440, 396198, 408897, 851020], [932044, 662093, 436861, 246956, 128943, 167432, 267483, 148325, 458128, 418348, 900594, 831373], [742255, 795191, 598857, 441846, 243888, 777685, 313717, 560586, 257220, 488025, 846817, 554722], [252507, 621902, 87704, 599753, 651175, 305330, 620166, 631193, 385405, 183376, 432598, 706692], [984416, 996917, 586571, 324595, 784565, 300514, 101313, 685863, 703194, 729430, 732044, 349877], [155629, 290992, 539879, 173659, 989930, 373725, 701670, 992137, 893024, 455455, 454886, 559081], [252809, 641084, 632837, 764260, 68790, 732601, 349257, 208701, 613650, 429049, 983008, 76324], [918085, 126894, 909148, 194638, 915416, 225708, 184408, 462852, 40392, 964501, 436864, 785076], [875475, 442333, 111818, 494972, 486734, 901577, 46210, 326422, 603800, 176902, 315208, 225178], [171174, 458473, 744971, 872087, 680060, 95371, 806370, 322605, 349331, 736473, 306720, 556064], [207705, 587869, 129465, 543368, 840821, 977451, 399877, 486877, 327390, 8865, 605705, 481076]], [690474, 796832, 913701, 939418, 46696, 266869, 150594, 948153, 718874], [85, 145, 166, 171, 0, 1, 0, 171, 126])])
def test_all(grid, queries, out):
    test_sol = Solution()
    assert test_sol.maxPoints(grid, queries) == out
