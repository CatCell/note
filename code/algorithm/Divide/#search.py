# search
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mid = len(nums) // 2

        if len(nums) == 1:
            if nums[0] != target:
                return -1
            else:
                return nums[0]
        if nums[mid] <= target:
            return self.search(nums[mid:], target)
        else:
            return self.search(nums[:mid], target)


# 没实现寻找下标
x = Solution().search([-1, 0, 3, 5, 9, 12], 5)
print(x)
