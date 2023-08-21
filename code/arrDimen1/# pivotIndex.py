# Pivotindex
""" 
class Solution(object):
    def pivotIndex(self, nums):
        def ispivotIndex(nums, pos):
            if sum(nums[0:pos]) == sum(nums[-1:pos:-1]):
                return True
            else:
                return False

        for pos, value in list(enumerate(nums)):
            if ispivotIndex(nums, pos):
                return pos

        return -1
# 算法复杂度N2
         """


# 计算出nuns综合，从左向右找到是否存在为总和一半的位置


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _sum = sum(nums)
        currValue = 0
        for pos in range(len(nums)):
            if currValue * 2 + nums[pos] == _sum:  #
                return pos
            currValue += nums[pos]  #
        return -1


# 时间复杂度O(N)
print(Solution().pivotIndex([1, 2, 1]))
