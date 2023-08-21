# Linux

## 计算机概论

### 磁盘

#### 磁盘物理组成

![Alt text](Pic/%E6%9C%BA%E6%A2%B0%E7%A1%AC%E7%9B%98.webp)

- 机械臂
- 读写头
- 盘片
  - 磁道 track：组成了柱面 Cylinder
  - 扇区 Sector：两种设计：512Bytes 4KBytes
- 主轴马达
  ![Alt text](Pic/%E7%9B%98%E7%89%87.jpg)

#### 分区格式 Partition format

> 而通常磁盘可能有多个盘片，所有盘片的同一个磁道我们称为柱面 （Cylinder）通常那是文件系统的最小单位，也就是分区的最小单位啦！为什么说“通常”呢？因为近来有 GPT 这个可达到 64bit 纪录功能的分区表， 现在我们甚至可以使用扇区（sector）号码来作为分区单位哩！

- 分区最小单位：因为一个分区对应一个文件系统，所以也是文件系统最小单位。
- 可以看出 GPT 支持更细的分区
- “64bit”记录功能的分区表

##### MBR

MBR 最多支持 4 个分区。

最高支持 2.2T 容量硬盘(不使用逻辑分区情况下)

为什么 MBR 分区格式最多支持 2TB？

> 这个和 32 位操作系统没有关系完全是 MBR 分区表规范的原因
> ![MBR分区表](https://img2020.cnblogs.com/blog/741682/202010/741682-20201008184307747-1604693136.gif)
> MBR 分区表仅有 64B，而且还分成四份，一个分区记录只用了 16B，它的结构和上图是一样的，限制在于最后使用了 4B 记录之前的扇区数和总扇区数，观察一个分区表至多只能支持$2^{32}$个扇区

$$
2^{32+9+3}=2^{2+3+40} \tag{每个扇区512B}
$$

所以最多支持 2TB

##### GPT(GUID Partition Table)

LBA（Logical Block Address, LBA）为了兼容 4K 和 512Byte

| LBA0(MBR 相容区块)                                    | LBA1(GPT 表头记录)                                          | LBA2-33(实际记录分区)             | 最后 43LBA 区块 |
| ----------------------------------------------------- | ----------------------------------------------------------- | --------------------------------- | --------------- |
| 446Bytes 开机启动程序，相容模式(带一个特殊标志分区表) | 分区表本身的位置大小，备份 GPT 分区所在位置，CRC 校验机制码 | 一个分区记录四笔，共计 128 笔分区 | 备份 GPT 分区   |

##### 开机启动流程

1.  BIOS 最先启动，寻找磁盘第一个分区里的开机管理程序 446Bytes
2.  1.  MBR：开机管理程序(Boot loader)是 OS 安装时提供，故认识磁盘，拉取核心文件
    2.  GPT：LBA 仅提供第一阶段 bootloader，需要 BIOS boot 分区存放开机管理程序(实现多重开机)
3.  交给操作系统

## Linux 的安装

## Linux 文件权限和目录配置

### 使用者 User 与群组 Group

Linux 分对象设置权限,有 Owner,Group,Others,Root.

### Linux 文件权限

#### Linux 文件属性

```bash
ubuntu@VM-4-5-ubuntu:~$ ls -al
total 60
drwxr-x--- 6 ubuntu ubuntu 4096 Aug 21 00:01 .
drwxr-xr-x 4 root   root   4096 Aug 10 00:44 ..
-rw------- 1 ubuntu ubuntu 2345 Aug 20 23:53 .bash_history
-rw-r--r-- 1 ubuntu ubuntu  220 Jan  7  2022 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Jan  7  2022 .bashrc
drwx------ 2 ubuntu ubuntu 4096 May 18  2022 .cache
drwx------ 3 ubuntu ubuntu 4096 Aug 10 00:22 .config
drwxrwxr-x 2 ubuntu ubuntu 4096 May 18  2022 .pip
-rw-r--r-- 1 ubuntu ubuntu  807 Jan  7  2022 .profile
-rw-rw-r-- 1 ubuntu ubuntu   73 Aug 10 00:15 .pydistutils.cfg
drwx------ 2 ubuntu ubuntu 4096 May 18  2022 .ssh
-rw-r--r-- 1 ubuntu ubuntu    0 Aug 10 00:27 .sudo_as_admin_successful
-rwxrw-r-x 1 ubuntu ubuntu  282 Aug 17 11:15 test.py
-rw------- 1 ubuntu ubuntu 7351 Aug 17 11:15 .viminfo
-rw------- 1 ubuntu ubuntu   59 Aug 21 00:01 .Xauthority

```

| 权限       | 链接 | 拥有者 | 群组   | 文件大小(Byte) | 修改日期     | 文件名 |
| ---------- | ---- | ------ | ------ | -------------- | ------------ | ------ |
| drwxr-x--- | 6    | ubuntu | ubuntu | 4096           | Aug 21 00:15 | .pip   |

#### Linux 改变文件属性

- **chgrp [-R] grpname filename**:改变群组
- **chown [-R] username filename**：改变拥有者，如 CP 前先 chown
- **chmod [-R] 770/...**：改变权限，按照规则计算 OGO 的权限数值

#### 目录和文件的权限区别

| 元件 | 内容   | 叠代物件？ | r        | w          | x        |
| ---- | ------ | ---------- | -------- | ---------- | -------- |
| 文件 | data   | 文件数据夹 | 读       | 写         | 执行     |
| 目录 | 文件名 | 可分类抽屉 | 读文件名 | 修改文件名 | 进入目录 |

#### 执行操作和需要的权限

| 操作           | /dir0 | /dir0/file | dir1 | 核心 |
| -------------- | ----- | ---------- | ---- | ---- |
| 读取 file 内容 | x     | r          | -    | .    |
| 修改           | x     | w          | -    | .    |
| 执行           | x     | x          | -    | .    |
| 删除           | wx    | -          | -    | .    |
| 复制到/dir1    | x     | w          | wx   | .    |

### Linux 目录配置

#### FHS 简介

> 根据 **FHS(Filesystem Hierarchy Standard)** 的标准文件指出，他们的主要目的是希望让使用者可以了解到已安装软件通常放 置于那个目录下,所以他们希望独立的软件开发商、操作系统制作者、以及想要维护系统的使用者，都能够遵循 FHS 的标准。

![FHS](https://images0.cnblogs.com/blog/443733/201409/021134253607650.gif)

#### FHS 目录的四种交互形态

| case     | shareable                                           | unshareable                            |
| -------- | --------------------------------------------------- | -------------------------------------- |
| static   | /usr(软件放置) /opt(第三方软件)                     | /etc(配置文件) /boot(开机和核心档)     |
| variavle | /var/mail(使用者邮件信箱) /var/spool/news(新闻群组) | /var/lock(程序相关) /var/run(程序相关) |

## Linux 文件和目录管理

### 目录与路径

- **cd**:change dire
- **pwd**: print wd
- **mkdir [-p] [-m 711]**: make dir
- **rmdir**: remove

\${PATH}:环境变量

### 文件与目录管理

- **ls -a -l**:list 隐藏文件，以长数据格式串列出
- 文件操作
  - **cp**
  - **mv**：移动，更名(rename 专职批量重命名)
  - **rm**
- **basename**:取得文件名
- **dirname**：取得目录名

### 文件内容查询

- 查阅内容

  - **cat tac**：concatenate -A(-vRT)
  - **nl**:同时输出行号
  - more less
  - **head tail**：只看头尾
  - od

- status time(stime)
- modification time(mtime)
- access time(atime)

```bash
# 将上个范例的bashrc日期改为2014/06/15 2:02
[dmtsai@study	tmp]#	touch	-t	201406150202	bashrc
```

## Linux 磁盘和文件系统管理

### 认识 linux 文件系统

#### 文件系统特性

- 索引式文件系统
  - superblock：文件系统整体信息
    - block 和 inode 总量
    - 已使用/未使用的 inode/blocl
    - block inode 大小
    - filesystem 挂载时间，最近写入数据时间(不定时同步)，最近一次校验磁盘时间
    - valid bit：显示是否怪哉(0 正常)
  - inode：（每个文件只占用一个 inode）
    - 文件存取模式
    - owner group
    - 容量
    - atime，ctime，mtime
    - pointer 实际指向位置
  - datablock：实际数据存放
- 非索引式文件系统(FAT,闪存盘)
  - 需要磁盘重组

#### Linux 的 EXT2 文件系统（inode）

索引式文件系统--> block group
datablock 按大小分为 1，2，4K，这和扇区大小不同，基本都是 4K 去创建文件系统

#### 与目录树的关系

1. 查看/下文件夹 id，文件夹创建对应文件系统进行什么创建，你发现了 inode 和 4096 的关系了吗，为什么 usr 比较大？

读取/etc/passwd 的流程

1. /的 inode /的 block
2. etc 的 inode etc 的 block
3. passwd 的 inode passwd 的 block

#### EXT2/EXT3/EXT4 文件的存取与日志式文件系统的功能

##### 创建新文件的流程

1. 确定使用者对于目录 w 与 x 的权限；
2. 根据 inode bitmap 找到没有使用的 inode 号码，并将新文件的权限/属性写入；
3. 根据 block bitmap 找到没有使用中的 block 号码，并将实际的数据写入 block 中，且更新 inode 的 block 指向数据；
4. 将刚刚写入的 inode 与 block 数据同步更新 inode bitmap 与 block bitmap，并更新 superblock 的内容。

##### 日志文件系统

Journaling filesystem 是为了解决**不一致(inconsistent)问题**，简化 一致性检查的操作.

1. 当系统写入文件前，首先在日志上记录
2. 实际写入过程
3. 写入完成后且完成 metadata 更新后，在日志记录

#### Linux 文件系统的运行

**非同步处理 （asynchronously）** 是为了解决磁盘和内存读写速度差距过大问题上的。Linux 讲不定是将内存中修改的 Dirty data 写入磁盘。
可以使用 sync 强制写入，关机时系统会调用 sync。

#### 挂载点的意义 （mount point）

#### 其他 Linux 支持的文件系统与 VFS

#### XFS 文件系统简介

### 文件系统的简单操作

### 磁盘的分区格式化，检验和挂载

### 设置开机挂载

### SWAP 之创建

### 文件系统的特殊观察与操作

# bala

## 认识与学习 BASH

## 正则表达式与文件格式化处理

## 学习 Shell Script

## 账号管理与 ACL 权限设置

## 认识系统服务 Daemons

## 认识与分析登陆文件

## 开机流程，模块管理与 Loader

## 基础系统设置和备份策略

## 软件安装 RPM，SRPM 与 YUM
