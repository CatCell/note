# 廖雪峰的 Python 教程 笔记

[Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400 "中文，免费，零起点，完整示例，基于最新的Python 3版本。")

## 高级特性

### 切片

很方便截取 list,tuple,string 的部分,实现倒序

```python
def is_palindrome(int0):
temp = str(int0)
if temp == temp[::-1]:
    return True
else:
    return False


output = filter(is_palindrome, range(1, 1000))
print("1~1000:", list(output))
```

### 迭代

遍历 iterable 的内容

```python
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(L):
    if L != []:
        min = L[0]
        max = L[0]
        for i in L:
            min = min if min < i else i
            max = max if max > i else i
        return (min, max)
    else:
        return (None, None)  # 下标越界
```

### 列表生成式

以一种简洁方式生成列表

### 生成器

将列表生成式的[]换为(),或者使用 yield 输出需要时才会计算，节省内存空间

```python
def triangle(n):
def makeNextline(List0):
    List1 = [1]

    for i in range(len(List0) - 1):
        List1.append(List0[i] + List0[i + 1])

    List1.append(1)
    return List1

result = []
temp = [1]
for i in range(n):
    yield (temp)
    result.append(temp)
    temp = makeNextline(temp)

# 更好的写法
def triangles():
L = [1]

while True:
    yield L

    L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]
```

### 迭代器

> 可迭代对象 **iterable** 包括集合数据类型和 generator,
> 迭代器 **iterator** 是指可以被 next()调用的对象

iterator 一定是 iterable 的，而且不通过一步步迭代就不可知长度(不能使用 len 函数)

## 高阶函数

### map/reduce

> map(func, \_iterables) --> map object

将 func 一次作用于后面的\_iterables,可以很方便进行对序列求和，int 序列转换为整数等操作

```python
# 序列变为整数
def f(x,y):
return 10*x+y
reduce(f,[1,2,3,4])

# str2int
from functools import reduce


def str2int(s):
transTable = {"1": 1, "2": 2}

def strDig(str0):
    return transTable[str0]

def f(x, y):
    return 10 * x + y

return reduce(f, map(strDig, s))


print(str2int("1212"))

# str2float
from functools import reduce


def str2float(str0):
DOTpos = str0.index(".")

def charDig(Char0):
    dictT = {"1": 1, "2": 2, "3": 3}
    return dictT[Char0]

def fn(x, y):
    return 10 * x + y

def Num0dot(str0):
    return [i for i in str0 if i != "."]

return reduce(fn, map(charDig, Num0dot(str0))) * 10 ** -(len(str0) - DOTpos - 1)


str0 = "1212.1212"
print(str2float(str0))
```

### filter

> filter(function or None, iterable) --> filter object

按照 func 过滤序列（列表推导式也可以起到过滤的效果，二者都对 iterable 对象可用）

```python
# 埃氏算法求素数
def OriNums():
n = 1
while True:
    n += 2
    yield n


def f(n):
return lambda x: x % n != 0


def Primes():
it = OriNums()
filter(f(2), it)
yield 2
while True:
    Prime0 = next(it)
    yield Prime0
    it = filter(f(Prime0), it)


times = 0
for i in Primes():
times += 1
if times > 10:
    break
print(i)
```

### sorted

> sorted(iterable, /, \*, key=None, reverse=False)

将 iterable 按照 key 进行排序，很方便的选择进行排序和倒序

```python
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序

# name
def by_name(tuple0):
    return tuple0[0]
# score
def by_score(tuple0):
    return tuple0[1]

L = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]
L2 = sorted(L, key=by_score)
L1 = sorted(L, key=by_name)

print(L1, L2)
```

## 函数式编程

### 函数做返回值

> 闭包(Closure):是这样一种程序结构，当返回函数时，相关的参数和变量都会保留在返回的函数中，只有当计算时才会被确定。

闭包跟函数最大的不同在于，当捕捉闭包的时候，它的自由变量会在捕捉时被确定，这样即便脱离了捕捉时的上下文，它也能照常运行。
在使用闭包结构时要注意，返回结果中不要含有任何循环变量或者后来会发生改变的变量。

```python
# 以下是一个不当使用闭包的例子
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
```

```python
# 练习
def createCounter():
x = 0

def counter():
    nonlocal x  # 必须声明nonlocal否则不能成功
    x += 1
    return x

return counter
counterB = createCounter()
print(counterB(), counterB(), counterB(), counterB(), counterB())
```

### 匿名函数

匿名函数是用来简化某些简单函数的使用

```python
# 改为匿名函数
# def is_odd(n):
#     return n % 2 == 1
L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)
```

### 装饰器

装饰器可以在不修改原函数定义的情况下改变，原函数的输出内容。
如果想要让装饰器带参数就要多加一层嵌套用来接受 func 参数，最外层函数接受新增加的参数。

```python
# 不可以接受参数的装饰器
def docorator(func):
    def wrapper(*args, **kw):
        print("LonglongAgo...")
        return func(*args, **kw)

    return wrapper
# 可以接受参数的装饰器
def fine(text):
def docorator(func):
    def wrapper(*args):  # from func
        print(text)
        return func(*args)

    return wrapper

return docorator

# 在前后增加内容
import functools


def docorator(func):
    functools.wraps(func)

    def wrapper(*args, **kw):
        print("begin call")
        temp = func(*args, **kw)
        print("end call")
        return temp

    return wrapper
```

### 偏函数

偏函数是用于简化复杂函数参数的设置，是 functiontools 模块提供的功能（就像 bash 里的 alias 一样）

```python
import functools

printf = functools.partial(print, end="")
printf("Hello,")
printf("World!")
```

## 面向对象编程

### 概念

1. 类和实例

> 类(Class)是实例(Instance)的模板，实例是类的具象。

具体来说，实例具有所有类的属性和方法(私有属性)，在此基础上类允许实例具有各不相同的属性和方法。

2. 封装，继承，多态

> 封装(Encapsulation)是指把对象的某些部分隐藏起来，在外部看不到。在 Python 中只需要在方法或属性前加上**\_\_**就可实现封装以限制访问。
> 继承(Inheritance)使得代码重用。
> 多态(polymorphic)指的是子类方法覆盖父类方法，实现同名方法的不同效果。

> 鸭子类型(Duck Typing)指的是动态语言中的一种编程风格(不是一种数据类型)。动态语言只有在程序运行中才能知道数据类型和执行的操作，这种编程风格不关心究竟是何种数据类型传入，而关心这种数据类型有没有相应的方法。

### 编程

1. 为 student 类设置一个随着实例创建逐次加一的类属性

```python
# stuNum
class Student:
   Total = 0

   def __init__(self, name) -> None:
         Student.Total += 1  #
         self.name = name


print(Student.Total)
Student("Tom")
print(Student.Total)
```

## 面向对象高级编程

### slots

一般来说，实例可以自由拥有除类属性之外的属性。slots 用于限制实例的属性添加。

> 注意 slots 对继承子类是不起作用的。

```python
class student:
__slots__ = ("name", "ID")
```

### @property

> @Property 装饰器用实例属性的方式访问变量同时添加对参数的检查

```python
class screen:
    @property
    def wid(self):
        return self._wid

    @wid.setter
    def wid(self, value):
        self._wid = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._wid

    # 如果按照设置属性的写法，是没有办法设置的因为resolution没有setter
```

### 多重继承

设计类的时候通常是单一继承下来的，但有时需要在类中混入两个以上类的功能，可以使用 **MinIN**。(多数时候是不推荐的)

```python
class Dog(Object,Animal,canivore):
    pass
```

### 定制类

> 以双下划线开头结尾的特殊名称的函数具有特殊功能
> **str**(),**repr**()
> 前者返回 print(instance1) 后者返回 instance1 的值
> **iter**(),**next**()
> 使得创建的实例 iterable

```python
# fibINiter
class Fib:
    def __init__(self) -> None:
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


for i in Fib():
    if i > 1000:
        break
    print(i)
```

> **getitem**(),**setitem**(),**delitem**()
> 使得 iterable 可以使用切片，像列表，字典一样(duck typing)
> **getattr**()
> 当引用不存在或者额外属性时生效
> **call**()
> 使得实例可以 call 自身

```python
class chain:
    def __init__(self, path="") -> None:
        self._path = path

    def __call__(self, name) -> Any:
        return chain(self._path + "/" + name)

    def __getattr__(self, __name: str) -> Any:  #
        return chain(self._path + "/" + __name)

    def __str__(self):
        return self._path


print(chain().users("MIchael").Location)
```

### 使用枚举类

为常量定义一个类，每个常量都是这个类的唯一实例，这可以通过 **\@property** 和 MixIN **unique**,**Enum** 类来实现。

```python
# 将student的gender属性改造为枚举类型
from enum import Enum, unique


@unique
class gender(Enum):
    male = 0
    female = 1


class student:
    def __init__(self, name, gender) -> None:
        self._gender = gender
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value


s0 = student("Tom", gender.male)
print(s0.
```

### 使用元类

使用 type 函数定义类，和之前的写法效果相同
metaclass 没怎么看懂，跳过了

```python
# typeDefine
def Fn(self):
    print("I am Method1")


Hello = type("Hello", (object,), dict(method1=Fn))  # dict
Hello0 = Hello()
Hello0.method1()
```

## 错误调试和测试

### 错误处理

> **try...except...finally...**:当 try 语句中出现 except 中的异常，停止 try 语句执行 except 最后执行 finally 语句。

只需要在合适的位置使用 try-except-finally 语句就可以简化错误调试

> 抛出异常 raise，记录错误 logging

阅读异常信息

```python
from functools import reduce
def str2num(s):
    return int(s) #此处改为float()
def calc(exp):
    ss = exp.split("+")
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)
def main():
    r = calc("100 + 200 + 345")
    print("100 + 200 + 345 =", r)
    r = calc("99 + 88 + 7.6")
    print("99 + 88 + 7.6 =", r)
main()

Traceback (most recent call last):
  File "C:\Users\PC\Desktop\PyLXF\test\youbing.py", line 21, in <module>
#21出错是由于17
    main()
  File "C:\Users\PC\Desktop\PyLXF\test\youbing.py", line 17, in main
    r = calc("99 + 88 + 7.6")
        ^^^^^^^^^^^^^^^^^^^^^
#17出错是由于11
  File "C:\Users\PC\Desktop\PyLXF\test\youbing.py", line 11, in calc
    return reduce(lambda acc, x: acc + x, ns)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#11出错是由于5
  File "C:\Users\PC\Desktop\PyLXF\test\youbing.py", line 5, in str2num
    return int(s)
           ^^^^^^
#最终定位出错位置在5
ValueError: invalid literal for int() with base 10: ' 7.6'
```

### 调试

> 调试程序的几种方式

- print,assert：print 和 assert 会使程序调试信息和内容混在一起，assert 唯一的好处是不需要删除只需要添加参数 -o 就可以关闭 assertion
- logging：的好处有可以设置输出日志的级别，还可以分别将内容输出到文件和命令行
- pdb，单步调试和设置断点

```python
# logging
import logging
logging.basicConfig(level=debug)
string0 = "0"
int0 = int(string0)
logging.info(int0)
print(10 / int0)
```

logging 才是终极武器？
体会是实际调试程序时单步调试只要程序稍微复杂一些，效果就很差甚至比不上 print 检查。

### 单元测试

可以为一个模块或者一个函数编写单元测试，当需要修改时如果能保证修改前后单元测试均能通过则可以相对确定代码更新没有 BUG

**setup()**, **tearDown()** 可以单元测试的每一类测试中先进行 setup 后进行 teardown 内容不需要重复编写。

```python
# 编写一个mydict，写一个unittest
from typing import Any
import unittest

class Mydict(dict):
    def __init__(self, **kws):
        super().__init__(**kws)

    def __setattr__(self, key: str, value: Any) -> None:
        self[key] = value

    def __getattr__(self, value) -> Any:
        try:
            return self[value]
        except KeyError:
            raise AttributeError

class testMydict(unittest.TestCase):
    def test_basicUse(self):
        md0 = Mydict(a=1, b=2)
        self.assertEqual(md0.a, md0["a"])

unittest.main()
```

### 文档测试

再看代码库时经常看到在定义开头的特殊格式注释起来的示例代码，python 的模块 doctest 允许检查实例代码输入使出是否一致.
更多的是一种说明作用，方便使用.

```python
# 在编写的Mydict基础上继续编写他的doctest
# doctest
class Mydict(dict):
    """
    Mydict is dict but also support access as x.y style.

    Example:

    >>> d1=Mydict()
    >>> d1["x"]=10
    >>> d1.x
    10
    """
    def __init__(self, **kws):
        super().__init__(**kws)

    def __setattr__(self, key: str, value: any) -> None:
        self[key] = value

    def __getattr__(self, value) -> any:
        try:
            return self[value]
        except KeyError:
            raise AttributeError

if __name__ == "__main__":
    import doctest

    doctest.testmod()
```

## IO 编程

### 小结

> 同步 IO 和异步 IO

### 文件读写

> 文件读写的三种写法(写法 2 自动关闭文件对象，写法简洁)：

- f=open(path,mode);f.read();f.close()
- with open(path,mode) as f: f.read()
- try: f=open(path,mode) finally if f: f.close()

> "rb" 读取二进制文件
> encoding="gbk":读取非 UTF-8 文本

> 打开文件模式汇总表

| Character | Meaning                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------- |
| r         | open for reading (default)                                                                                  |
| w         | open for writing, truncating the file first(eXculsive lock like)                                            |
| x         | open for exclusive creation, failing if the file already exists                                             |
| a         | open for writing, appending to the end of file if it exists                                                 |
| b         | binary mode                                                                                                 |
| t         | text mode (default)是 windows 平台特有的所谓 text mode(文本模式）,区别在于会自动识别 windows 平台的换行符。 |
| +         | open for updating (reading and writing)                                                                     |

```python
# 练习读写文件
# readfile
path = "./text0.txt"
with open(path, "a+") as f:
    # w+模式会删除源文件内容
    # a+模式由于指针位置无法读到文件内容
    f.seek(0, 0)
    str0 = f.read()
    print(str0)

    f.seek(0, 2)
    str1 = "Hello simpleIO"
    f.write(str1)

    f.seek(0, 0)
    str0 = f.read()
    print(str0)

```

### StringIO 和 BytesIO

二者都是在内存中操作 string 和 byte 的方法

```python
# 使用ByteIO
import io

f = io.BytesIO()
f.write("Hello BytesIO".encode("utf8"))
print(f.getvalue())
```

### 操作文件和目录

> 内 os 模块使 python 可以调用系统提供的接口
> os.name 给出操作系统名称,os.environ 查看系统定义的环境变量
> 查看目录 os.path.abspath 合并目录 os.path.join，拆分目录 os.path.splitext，获取拓展名 os.path.splitext
> 复制文件 shutil.copyfile()

```python
# 列出当前目录的所有文件夹
[x for x in os.listdir(".") if os.path.isdir(x)] #os.listdir的作用是列出所有文件，dir有些误导
[x for x in os.listdir(".") if os.path.isfile(x) and os.path.splitext(x)[1]==".py"] #列出当前目录下所有py文件
```

```python
# 将子集文件夹的包含指定字符串的文件找出
```

### 序列化

> 将暂时存在于内存中的变量变为可以存储在磁盘或传出的内容的过程称为序列化 serilization。相反的过程称为反序列化.
> python 提供 pickle 模块实现序列化过程（不同版本不同语言之间不同），但是不如 json 模块通用

```python
# 使用json dump
import json

class student:
    def __init__(self, name, age) -> None:
        self._name = name
        self._age = age

def student2dict(std):
    return {"name": std._name, "age": std._age}

def dict2student(dict0):
    return student(dict0["name"], dict0["age"])

stu0 = student("杰瑞", "male")
json0 = json.dumps(
    stu0, default=student2dict, ensure_ascii=True
)  # ensure_ascii设置为true把所有非ascii字符转变为unicode
print(json0)
print(json.loads(json0, object_hook=dict2student))
```

## 进程和线程

### 前篇 & 进程 vs.线程

> **进程(Process)**:系统资源调度时的独立单位
> **线程(Thread)**:系统进行运算调度的最小单位

程序，进程和线程：一个程序运行至少有一个进程，一个进程至少有一个线程
二者优缺点：进程实现了并发操作，但是进程之间不共享内存，消息沟通麻烦。线程共享内存消息沟通方便，提高了 CPU 的执行效率，但是编写程序容易出错(线程同步问题)。

进行多任务操作时优先使用更加稳定的进程。Fork 操作相较于 ISS 多进程消耗更低，**Apache** 就是采用多进程，ISS 由于多线程稳定就不是很好。
此外由于线程是相互独立的，这是进行分布式计算的基础。

### 多进程

> linux/mac 通过 python 调用系统函数 **fork** 可以轻松创建子进程
> Python 为 windows 提供的跨平台的多进程支持

#### Windows 下使用多进程

```python
from multiprocessing import Process
import os
def run_proc(name):
    print(name + "is running" + str(os.getpid))
p1 = Process(target=run_proc, args=("Proc1",))
p1.run()
if p1.is_alive(): #不能直接Join()，原因不明
    p1.join() #join()等待进程结束继续执行，用于进程同步
else:
    print("has completed")
```

#### 创建多进程

```python
from multiprocessing import Pool  # pool是模块，Pool是函数
import random, os, time
def proc(name): # 子程序出错就没有返回了
    start = time.time()
    print("Run task %s (%s)..." % (name, os.getpid()))
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))

if __name__ == "__main__":  # 不明白为什么没有这行就出错了？
    p = Pool(4)  # Pool开头大写
    print("Parent Proc %s" % os.getpid)
    for i in range(5):
        p.apply_async(proc, args=(i,))
    print("waiting for all done")
    p.close()
    p.join()
    print("Done")
```

#### 向进程内传递信息

```python
import subprocess  # mutiprocessing库
print("$ nslookup www.python.org")
r = subprocess.call(["nslookup", "www.python.org"])
print("Exit code:", r)
# 不明白为什么直接在本机上不可以执行但是可以在进程中执行
```

#### queue 用于进程间传递消息

```python
from multiprocessing import Process, Queue
import os, random, time
def read(q):
    print("read proc working%s" % os.getpid())
    while True:
        value = q.get(True)  # 从队列中取值
        print("get value %s" % value)
def write(q):
    print("write proc working %s" % os.getpid())
    for i in ["A", "B", "C"]:
        print("Put value %s" % i)
        q.put(i)
        time.sleep(random.random() ** 3)

if __name__ == "__main__":
    q = Queue()
    pr = Process(target=read, args=(q,)) #注意写法
    pw = Process(target=write, args=(q,))
    pr.start()
    pw.start()  # 可以交换位置
    pw.join()   # ?等待pw结束
    pr.terminate()
```

### 多线程

之前提到，线程和进程的区别之一就是线程会共享内存空间，那就可能会带来并发操作问题。

并发操作带来的问题有：

- 读脏数据：本是 rollback 的脏数据由于并发被其他线程读取（）
- 丢失更新：两线程先后进行更新操作导致前一个线程更新丢失（）
- 不能重复读：同一变量前后读取值不一致

为解决问题引入三级锁协议:

| 封锁协议     | 内容                                                                                                                                                           |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 一级封锁协议 | 事务 T 在修改数据 R 之前必须先对其加 X 锁，直到事务结束才释放。一级封锁协议能够解决“丢失修改”问题。                                                            |
| 二级封锁协议 | 一级封锁协议加上事务在读取数据 R 之前必须先对其加 S 锁 ，读完后即可释放 S 锁。二级封锁不仅可以解决“丢失修改”问题，而且可以解决读“脏“数据问题。                 |
| 三级封锁协议 | 一级封锁协议加上事务在读取数据 R 之前必须先对其加 S 锁，直到事务结束才释放。三级封锁协议不仅解决了“丢失修改”、读“脏”数据问题，而且进一步解决了“不可重复读”问题 |

#### 使用线程

```python
# loop thread
import time, threading
def loop():
    print(threading.current_thread().name + "will work")
    for i in range(3):
        print(i)
        time.sleep(1)
    print("%s ended" % threading.current_thread().name)

t0 = threading.Thread(target=loop, name="Thread0")  # process 这里是 args=
print("%swill working" % threading.current_thread().name)
t0.start()
t0.join()
print("%s Done" % threading.current_thread().name)

```

#### 使用多线程和上锁

这个实例试图展示多线程可能带来的问题。并使用锁机制去解决。但是发现多线程并没有带来问题，查阅资料后发现是 Python 的问题，但没怎没看懂，（能否用 python 的 GIL 去解释，每时只有一个线程在执行所以就已经加过锁了）。
以下是原文链接[stackoverflow](https://stackoverflow.com/questions/69993959/python-threads-difference-for-3-10-and-others "Python threads difference for 3.10 and others")

```python
# mutithread prob
import threading
def CashInO(amount):
    global balance
    balance += amount
    balance -= amount

def Do4many(amount):
    for i in range(200000):
        lock.acquire()
        try:
            CashInO(amount)  # 这里是加锁的写法，不加锁就是只有这一行
        finally:
            lock.release()

balance = 100
lock = threading.Lock()
t0 = threading.Thread(target=Do4many, args=(4,))
t1 = threading.Thread(target=Do4many, args=(3,))
t0.start()
t1.start()

t0.join()
t1.join()
assert balance == 100
```

#### GIC 锁

**GIC 锁**是 python 在语言设计中的一个老问题，当一个进程中的线程工作时需要首先请求 GIC 锁，否则不能执行所以多线程任务每时每刻只有一个线程在执行，每个进程都有一个 GIC 锁，最大并行数量实际是进程数量。
在下面的例子中，虽然启动了和 cpu 核心数目一样的线程数，但由于 GIC 锁的存在，python 最多占用一个 CPU 核心。而不可能像 C 一样占满 cpu。

```python
# neverEnd
import threading, multiprocessing
def f():
    x = 1
    while True:
        x *= 1
for i in range(multiprocessing.cpu_count()):
    t0 = threading.Thread(target=f)
    t0.start()
```

### Threadlocal

如果每一个线程都需要具有一个同名的局域变量，那参数的参入就会较为复杂，Threadlocal 库就是为了解决这个问题。

```python
# MYthreading local
import threading

temp = threading.local()
def getlocalvar():
    localvar = temp.tempname
    print("Hello getlocalvar working:%s" % localvar)
def thremethod(key):
    temp.tempname = key
    getlocalvar()

t0 = threading.Thread(
    target=thremethod, args=("key0",), name="Thread0"
)  # name是进程名字，args是创建进程传入参数
t1 = threading.Thread(
    target=thremethod, args=("key1",), name="Thread1"
)  # 就算只需要传一个参数也必须写成元组形式
t0.start()
t1.start()
t0.join()
t1.join()
```

### 分布式进程

分布式进程的可行性是建立在进程相互独立的基础之上的，Python 提供一个封装较好的库。

```python
from multiprocessing.managers import BaseManager
```

~~分布式进程主机处的代码报错了，这部分只是粗略看了一下。没有实操~~
