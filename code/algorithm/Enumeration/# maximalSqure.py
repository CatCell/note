# maximalSqure
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height, width = len(matrix), len(matrix[0])
        thero_max = min(height, width)

        def isAllone(x, y, size, matrix):
            temp = 0
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if matrix[i][j] == "1":  # str
                        temp += 1
            if temp == size * size:
                return True
            else:
                return False

        for possiblemax in range(thero_max, 0, -1):
            height_low, height_high = 0, height - possiblemax
            width_low, width_high = 0, width - possiblemax
            for i in range(height_low, height_high + 1):
                for j in range(width_low, width_high + 1):
                    if isAllone(i, j, possiblemax, matrix):
                        return possiblemax**2
        else:
            return 0


if __name__ == "__main__":
    x = Solution().maximalSquare(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )  # 有一个很大的矩阵超时了，需要修改...
    print(x)
