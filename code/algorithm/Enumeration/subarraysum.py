class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        times = 0
        for start in range(len(nums) + 1):
            temp_sum = 0
            lengthrange = len(nums) - start
            for length in range(1, lengthrange + 1):
                for i in range(start, start + length):
                    temp_sum += nums[i]
                    print(times, start, length, i, nums[i])
                    if temp_sum == k:
                        times += 1
                        # print(times, start, length, i, nums[i])
        return times


if __name__ == "__main__":
    print(Solution().subarraySum([1, 2, 3], 3))
