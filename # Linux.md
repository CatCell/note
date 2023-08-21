# Linux

## Linux 的安装

## 文件权限和目录配置

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

- ls -a -l:list 隐藏文件，以长数据格式串列出
- 文件操作
  - cp
  - mv：移动，更名(rename 专职批量重命名)
  - rm
- basename:取的文件名
- dirname：取得目录名

### 文件内容查询

- 查阅内容

  - cat tac：concatenate -A(-vRT)
  - nl:顺便输出行号
  - more less
  - head tail：只看头尾
  - od

- status time(stime)
- modification time(mtime)
- access time(atime)

```bash
# 将上个范例的bashrc日期改为2014/06/15 2:02
[dmtsai@study	tmp]#	touch	-t	201406150202	bashrc
```

## Linux 磁盘和文件系统管理

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
