# fib
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in (0, 1):
            return n
        else:
            return Solution().fib(n - 1) + Solution().fib(n - 2)


x = Solution().fib(4)
print(x)
