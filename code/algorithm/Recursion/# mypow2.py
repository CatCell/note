# mypow2
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        elif n == 1:
            return x
        else:
            return self.myPow(x, n // 2) ** 2 * x


# 这个不应该嵌套次数是log2n吗，这还会溢出？
print(Solution().myPow(2, -2))
