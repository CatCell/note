# mypow
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / Solution().myPow(x, -n)
        if n == 0:
            return 1
        return Solution().myPow(x, n - 1) * x


print(Solution().myPow(2, -2))
# 有最大迭代的报错，测试样例可以通过.
