import math


class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """

        def get1towermaypointlist(tower, radius):
            templist = []
            x_start, x_end = tower[0] - radius, tower[0] + radius
            y_start, y_end = tower[1] - radius, tower[1] + radius
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    templist.append((i, j))
            return set(templist)  # 返回二维数组集{()()}

        def getmaypointlist(towers, radius):
            maypointset = set()
            for tower in towers:
                maypointset = maypointset.union(get1towermaypointlist(tower, radius))
            return maypointset  # {()()}

        def isreachable(point, tower, radius):
            d2 = (point[0] - tower[0]) ** 2 + (point[1] - tower[1]) ** 2
            if d2 <= radius**2:
                return True
            else:
                return False

        resultlist = []
        for point in getmaypointlist(towers, radius):  # point 二维数组
            power = 0
            for tower in towers:
                if isreachable(point, tower, radius):
                    d = math.sqrt(
                        (point[0] - tower[0]) ** 2 + (point[1] - tower[1]) ** 2
                    )
                    power += int(tower[2] / (1 + d))  # 少加括号
            resultlist.append([point, power])  # [[(),5],[(),6]]

        resultlist.sort(key=lambda x: (-x[1], x[0][0], x[0][1]))  # 这东西没有返回值
        if resultlist[0][1] == 0:
            return [0, 0]
        else:
            return list(resultlist[0][0])


if __name__ == "__main__":
    towers = [[42, 0, 0]]
    radius = 7
    x = Solution().bestCoordinate(towers, radius)
    print(x)
