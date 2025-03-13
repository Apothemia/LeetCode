class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolor = k + 1
        for i in range(len(blocks) - k + 1):
            window = blocks[i:i + k]
            window_recolor_cost = window.count('W')
            if window_recolor_cost == 0:
                return 0
            if window_recolor_cost < min_recolor:
                min_recolor = window_recolor_cost
        return min_recolor


if __name__ == '__main__':
    s = Solution()
    print(s.minimumRecolors(blocks="WBWBBBW", k=2))
