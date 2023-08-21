from functools import reduce


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # arr2int
        int0 = reduce(lambda x, y: 10 * x + y, digits) + 1

        # int2str2arr
        str0 = str(int0)
        return list(map(int, [x for x in str0]))


print(Solution().plusOne([1, 2, 3]))
