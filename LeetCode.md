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

### 枚举算法(Enumeration Algorithm)

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

## 动态规划
