# sortArray
class Solution(object):
    # 归并排序求解
    def merge(self, leftarr, rightarr):
        mergeresult = []
        while leftarr and rightarr:
            if leftarr[0] < rightarr[0]:
                mergeresult.append(leftarr.pop(0))
            else:
                mergeresult.append(rightarr.pop(0))
        while leftarr:
            mergeresult.append(leftarr.pop(0))

        while rightarr:
            mergeresult.append(rightarr.pop(0))
        return mergeresult

    def mergesort(self, arr):
        if len(arr) <= 1:  # ==
            return arr
        mid = len(arr) // 2
        leftarr = self.mergesort(arr[:mid])  # 不含mid
        rightarr = self.mergesort(arr[mid:])
        return self.merge(leftarr, rightarr)

    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return self.mergesort(nums)


# 这个速度不够快过不去
x = Solution().sortArray([3, 4, 10, 6, 7])
print(x)
