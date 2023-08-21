# DiagonalOrder


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        Height = len(mat) - 1  # 矩阵行数
        Length = len(mat[0]) - 1  # 矩阵列数
        i, j = 0, 0  # 初始坐标
        dirc = 1  # 代表斜向上的方向
        List0 = [mat[0][0]]
        # 只有一个元素的特殊情况
        if len(mat) == 1 and len(mat[0]):
            return mat[0]
        # 一般情况
        else:
            for step in range(len(mat) * len(mat[0])):  # 考虑转弯的两种情况
                Turn_case1 = dirc == 1 and (i == 0 or j == Length)
                Turn_case0 = dirc == 0 and (j == 0 or i == Height)
                if Turn_case0 or Turn_case1:
                    if Turn_case1:
                        dirc = 0

                        if j == Length:  # 考虑撞到对角情况。优先当作J等于0
                            i += 1
                        else:
                            j += 1

                    else:
                        dirc = 1
                        if i == Height:  # 考虑撞到对角情况。优先考虑j等于0
                            j += 1

                        else:
                            i += 1
                    List0.append(mat[i][j])
                else:  # 考虑前进的两种情况
                    if dirc == 1:
                        i, j = i - 1, j + 1
                    else:
                        i, j = i + 1, j - 1
                    List0.append(mat[i][j])
                # 结束条件
                if i == Height and Length == j:
                    break

            return List0


print(Solution().findDiagonalOrder([[1, 2], [3, 4], [5, 6]]))
