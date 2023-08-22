# LeetCode

[刷 leetcode 需要哪些基础？](https://cloud.tencent.com/developer/article/2193927)
[算法通关手册](https://algo.itcharge.cn/00.Introduction/01.Data-Structures-Algorithms/)

## 序

### 数据结构和算法

> **数据结构是程序的骨架，而算法则是程序的灵魂。** [^1]

[^1]: **《算法 + 数据结构 = 程序》** Pascal 语言之父 Niklaus Emil Wirth

> 数据结构：组织数据的方式，程序的骨架。

- 逻辑数据结构
  - 集合结构：元素无序，数据元素唯一
  - 线性结构：数据元素形成一对一关系
  - 树：数据元素之间形成 1 对多关系
  - 图：数据源之间形成多对多关系
- 物理数据结构
  - 顺序数据结构
  - 链式存储结构

> 算法：解决具体问题的方法

- 确定性
- 有穷性
- 可行性：能够在计算机上可执行

> 好的算法应该追求

- 基本追求
  - 更小的存储空间
  - 更快的运行速度
- 其他追求
  - 健壮性：对于非法操作的处理
  - 可读性：方便阅读和调试
  - 正确性

### 算法复杂度

> 渐进符号将忽略步数函数中低增长率部分，分为三种。

- $\Theta$:紧确界符号
- $O$：上界符号
- $\Omega$: 下界符号

> 时间复杂度的求解遵守加法原则和乘法原则

$$
O(f(n)+g(n))=max(O(f(n),g(n))) \\
O(f(n)*g(n))=O(f(n))*O(g(n))
$$

| 时间复杂度   | 举例                         |
| ------------ | ---------------------------- |
| $O(1)$       | 等差数列的高斯算法           |
| $O(n)$       | 数列的累项求和               |
| $O(n^2)$     | 两层嵌套循环                 |
| $O(log_2n)$  | 二分查找问题                 |
| $O(n!)$      | 旅行商问题暴力求解，全排列？ |
| $O(nlog_2n)$ | 快速排序                     |

> 最坏，最佳，平均时间复杂度
> 比如线性结构的寻值算法，不同的排布情况导致同一问题规模具有不同的求解步数。

> 空间复杂度
> 比如两数之和算法就是$O(1)$的空间复杂度

```python
# factori
def fac(n):
    if n == 1:
        return 1

    return n * fac(n - 1)
```

> 在此例中时间复杂度为$O(n)$空间复杂度为$O(n)$

# 数据结构

## 数组

### 概念

线性表 连续的内存空间
数组可以进行随机访问数据元素

### 基本操作

- 增
  - 在指定位置增加元素
  - 在结尾增加元素
- 删
  - 在指定位置删除元素 pop
  - 删除尾部元素 pop
- 改
- 查 差找元素值为 val 的位置

### 数组排序

### 二分查找

# 算法

## 基础算法

### 枚举算法

> **枚举算法（Enumeration Algorithm）** ：也称为穷举算法，指的是按照问题本身的性质，一一列举出该问题所有可能的解，并在逐一列举的过程中，将它们逐一与目标状态进行比较以得出满足问题要求的解。在列举的过程中，既不能遗漏也不能重复

枚举算法是遇到问题最先想到的方法，一般来说效率不高，但是容易验证正确性。

#### 百钱百鸡问题

#### 两数之和

```python
# twosum
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

#### 记数质数

#### 统计平方和三元数数目

```python
# countTriples
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for t in range(j + 1, n + 1):
                    if i * i + j * j == t * t:
                        num += 1
        return 2 * num  # 无序结果数目是有序数目二倍

```

#### 信号网络中最好的网格

```python
import math
class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """

        def get1towermaypointlist(tower, radius):
            templist = []
            x_start, x_end = tower[0] - radius, tower[0] + radius
            y_start, y_end = tower[1] - radius, tower[1] + radius
            for i in range(x_start, x_end + 1):
                for j in range(y_start, y_end + 1):
                    templist.append((i, j))
            return set(templist)  # 返回二维数组集{()()}

        def getmaypointlist(towers, radius):
            maypointset = set()
            for tower in towers:
                maypointset = maypointset.union(get1towermaypointlist(tower, radius))
            return maypointset  # {()()}

        def isreachable(point, tower, radius):
            d2 = (point[0] - tower[0]) ** 2 + (point[1] - tower[1]) ** 2
            if d2 <= radius**2:
                return True
            else:
                return False

        resultlist = []
        for point in getmaypointlist(towers, radius):  # point 二维数组
            power = 0
            for tower in towers:
                if isreachable(point, tower, radius):
                    d = math.sqrt(
                        (point[0] - tower[0]) ** 2 + (point[1] - tower[1]) ** 2
                    )
                    power += int(tower[2] / (1 + d))  # 少加括号
            resultlist.append([point, power])  # [[(),5],[(),6]]

        resultlist.sort(key=lambda x: (-x[1], x[0][0], x[0][1]))  # 这东西没有返回值
        if resultlist[0][1] == 0:
            return [0, 0]
        else:
            return list(resultlist[0][0])

```

#### 最大正方形

```python
# maximalSqure
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height, width = len(matrix), len(matrix[0])
        thero_max = min(height, width)

        def isAllone(x, y, size, matrix):
            temp = 0
            for i in range(x, x + size):
                for j in range(y, y + size):
                    if matrix[i][j] == "1":  # str
                        temp += 1
            if temp == size * size:
                return True
            else:
                return False

        for possiblemax in range(thero_max, 0, -1):
            height_low, height_high = 0, height - possiblemax
            width_low, width_high = 0, width - possiblemax
            for i in range(height_low, height_high + 1):
                for j in range(width_low, width_high + 1):
                    if isAllone(i, j, possiblemax, matrix):
                        return possiblemax**2
        else:
            return 0
```

#### 和为 k 的子数组

...再写

### 递归算法

> **递归（Recursion）**：指的是一种通过重复将原问题分解为同类的子问题而解决的方法。在绝大数编程语言中，可以通过在函数中再次调用函数自身的方式来实现递归。
> 递归和数学归纳法

| 数学归纳法 | 初始条件 | 归纳关系 |
| ---------- | -------- | -------- |
| 递归       | 终止条件 | 回归过程 |

递归三步

1. 写出递归关系
2. 写出终止条件
3. 翻译为代码

#### 汉诺塔

```python
# Hannoi
def move(n, a, b, c):
    if n == 1:
        print(a + "-->" + c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, "A", "B", "C")

```

#### 求整数次幂

#### 交换两两列表之间的节点

```python
# swapPairs
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 链表不是很懂
        start = ListNode(0)
        start.next = head
        curr = start
        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next
            curr.next = node2
            node1.next = node2.next  # 需要和后面链接
            node2.next = node1
            curr = node1
        return start.next

```

#### 斐波那契数列

```python
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

```

#### 计算整数幂

```python
# mypow
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / Solution().myPow(x, -n)
        if n == 0:
            return 1
        return Solution().myPow(x, n - 1) * x


print(Solution().myPow(2, -2))
# 有最大迭代的报错，测试样例可以通过.


# mypow2
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        elif n == 1:
            return x
        else:
            return self.myPow(x, n // 2) ** 2 * x


# 这个不应该嵌套次数是log2n吗，这还会溢出？
print(Solution().myPow(2, -2))

```

### 分治算法

> **分治算法（Divide and Conquer）** ：字面上的解释是「分而治之」，就是把一个复杂的问题分成两个或更多的相同或相似的子问题，直到最后子问题可以简单的直接求解，原问题的解即子问题的解的合并。

递归算法是分治算法的子集，除了递归之外，还有迭代算法可以实现某些分治。如快速傅里叶变换算法(?)、二分查找算法、非递归实现的归并排序算法等等。

#### 归并排序

```python
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

```

#### 二分查找

```python
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

```

## 动态规划
