# productEx
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 要求不能用除法，时间复杂度还要在N。
        # 没想出来
        length = len(nums)
        res = [1 for i in range(length)]
        proLeft = 1
        for i in range(length):
            res[i] = proLeft
            proLeft *= nums[i]

        proRight = 1
        for i in range(length - 1, -1, -1):  # 0 -1
            res[i] = res[i] * proRight
            proRight *= nums[i]
        return res


print(Solution().productExceptSelf([1, 2, 3, 4]))
