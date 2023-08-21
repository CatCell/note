# findMAxones
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxcombo = 0
        temp = 0
        for i in nums:
            if i == 1:
                temp += 1
            else:
                if temp > maxcombo:
                    maxcombo = temp
                temp = 0
        if temp > maxcombo:
            maxcombo = temp
        return maxcombo


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
