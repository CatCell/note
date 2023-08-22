class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        for i in range(len(nums)):  # 开始位置
            lenmax = len(nums) - i  # 在某一开始位置的最大长度
            for length in range(1, lenmax + 1):  # 1-max
                tempsum = 0
                for j in range(i, length + i):
                    # print(i, length, j)
                    tempsum += nums[j]
                    # print(tempsum)
                if tempsum == k:
                    total += 1
        return total


if __name__ == "__main__":
    testarr0 = [1, 1, 1]
    testarr1 = [1, 2, 3, 4, -1]
    print(Solution().subarraySum(testarr0, 2))  # 一般的可以
    # 第二天很快就写出来了
    # 算法速度不够
