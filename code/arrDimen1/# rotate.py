class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums_temp = nums * 2
        n = len(nums)
        return [i for i in nums_temp[n - k : 2 * n - k]]


print(Solution().rotate([-1, -100, 3, 99], 2))
# 输出和本地不一致？
