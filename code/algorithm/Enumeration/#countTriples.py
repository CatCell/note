# countTriples
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for t in range(j + 1, n + 1):
                    if i * i + j * j == t * t:
                        num += 1
        return 2 * num  # 无序结果数目是有序数目二倍


print(Solution().countTriples(10))
