# Storage

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
| cp 到/dir1     | x     | r          | wx   | .    |

#### 更多权限模式

> SUID, SGID, and Sticky Bits are powerful special permissions you can set for executables and directories on Linux.

##### SUID

> Commonly noted as SUID, the special permission for the user access level has a single function: A file with SUID always executes as the user who owns the file, regardless of the user passing the command. If the file owner doesn't have execute permissions, then use an uppercase S here.

```bash
# linux里的s权限命令
bioinfo23@node02:/usr/bin$ ll /etc/shadow
-rw-r----- 1 root shadow 6558 Aug 28 13:08 /etc/shadow
bioinfo23@node02:/usr/bin$ ll /usr/bin/passwd
-rwsr-xr-x 1 root root 68208 Nov 29  2022 /usr/bin/passwd*
bioinfo23@node02:/usr/bin$ ll /bin/su
-rwsr-xr-x 1 root root 67816 May 30 15:42 /bin/su*
bioinfo23@node02:/usr/bin$ ll /bin/mount
-rwsr-xr-x 1 root root 55528 May 30 15:42 /bin/mount*
bioinfo23@node02:/usr/bin$ ll /bin/ping
-rwxr-xr-x 1 root root 72776 Jan 30  2020 /bin/ping*
```

##### GUID

> This permission set is noted by a lowercase s where the x would normally indicate execute privileges for the group. It is also especially useful for directories that are often used in collaborative efforts between members of a group. Any member of the group can access any new file. This applies to the execution of files, as well. SGID is very powerful when utilized properly.
> As noted previously for SUID, if the owning group does not have execute permissions, then an uppercase S is used.

在团队开发时候让群组内的所有人都对新文件有权限。

```bash
# 创建设置权限，并查找指定权限的文件
(base) bioinfo23@node02:~/hch$ touch testfile
(base) bioinfo23@node02:~/hch$ chmod 2700 testfile
(base) bioinfo23@node02:~/hch$ find -perm -g=s
./testfile
(base) bioinfo23@node02:~/hch$ find -perm g=s
```

##### Stick bit

> The last special permission has been dubbed the "sticky bit." This permission does not affect individual files. However, at the directory level, it restricts file deletion. Only the owner (and root) of a file can remove the file within that directory.

```bash
(base) bioinfo23@node02:/$ ll -d tmp
drwxrwxrwt 1 root root 47448064 Sep  6 08:58 tmp/
```

### Linux 目录配置

#### FHS 简介

> 根据 **FHS(Filesystem Hierarchy Standard)** 的标准文件指出，他们的主要目的是希望让使用者可以了解到已安装软件通常放 置于那个目录下,所以他们希望独立的软件开发商、操作系统制作者、以及想要维护系统的使用者，都能够遵循 FHS 的标准。

![FHS](https://images0.cnblogs.com/blog/443733/201409/021134253607650.gif)

#### FHS 目录的四种交互形态

| case     | shareable                                           | unshareable                            |
| -------- | --------------------------------------------------- | -------------------------------------- |
| static   | /usr(软件放置) /opt(第三方软件)                     | /etc(配置文件) /boot(开机和核心档)     |
| variavle | /var/mail(使用者邮件信箱) /var/spool/news(新闻群组) | /var/lock(程序相关) /var/run(程序相关) |

> **/etc** ：系统的配置文件目录。密码文件，设置网卡信息，环境变量的设置，网络配置文件都在此目录。
> **/boot** ：存放系统内核和系统启动文件系统启动时最先被装载。

### 自测

1. FHS
   1. 解释什么是 FHS，他是受什么需求而产生的。
   2. 指出那些目录是可分享，不变动的。
   3. 运维经常需要修改配置文件而且 docker 官网上会展示如何通过 yml 文件配置，所以配置文件时可分享不变动的，对吗？

#### cp 的最低要求

```bash
# 推断最低要求为
# fromdir：--x
# textforCP:r--
# todir:-wr

# 验证
bioinfo23@node02:~/hch$ mkdir dir0
bioinfo23@node02:~/hch$ cd dir0
bioinfo23@node02:~/hch$ mkdir dir1
# 创建dir0，dir1，test文件
bioinfo23@node02:~/hch/dir0$ touch test
bioinfo23@node02:~/hch/dir0$ vi test
bioinfo23@node02:~/hch/dir0$ cat test
Hello world
# 修改权限
bioinfo23@node02:~/hch/dir0$ chmod 400 test
bioinfo23@node02:~/hch/dir0$ cd ..
bioinfo23@node02:~/hch$ chmod 100 dir0
bioinfo23@node02:~/hch$ chmod 300 dir1
# 测试cp指令
bioinfo23@node02:~/hch$ cp dir0/test dir1
bioinfo23@node02:~/hch$ cd dir1
bioinfo23@node02:~/hch/dir1$ ll
ls: cannot open directory '.': Permission denied # 验证了r的权限仅限于使用ls命令
bioinfo23@node02:~/hch/dir1$ cat test
Hello world
```

#### rm -rf 的最低要求

首先不能直接删除空目录

```bash
bioinfo23@node02:~/hch$ mkdir test
bioinfo23@node02:~/hch$ touch test/testfile
bioinfo23@node02:~/hch$ rm -d test
rm: cannot remove 'test': Directory not empty
```

探索最低要求过程

```bash
# 之前权限是--x,内有一个test文件权限为r--
bioinfo23@node02:~/hch$ rm -rf dir0
rm: cannot remove 'dir0': Permission denied
# -w- 无论是r还是w前提都是x
bioinfo23@node02:~/hch$ chmod 200 dir0
bioinfo23@node02:~/hch$ rm -rf dir0
rm: cannot remove 'dir0': Permission denied
bioinfo23@node02:~/hch$ chmod 600 dir0
bioinfo23@node02:~/hch$ rm -rf dir0
rm: cannot remove 'dir0/test': Permission denied
# 必须设置权限为rwx
# x:进入文件，r:读取所有文件，w:删除文件
bioinfo23@node02:~/hch$ chmod 700 dir0
bioinfo23@node02:~/hch$ rm -rf dir0
```

## Linux 文件和目录管理

### 目录与路径

- **cd**:change dire
- **pwd**: print wd
- **mkdir [-p] [-m 711]**: make dir
- **rmdir**: remove

\${PATH}:环境变量

### 文件与目录管理

- **ls -a -l**:list 隐藏文件，以长数据格式串列出
- **ls -i** ：list 出每个文件的 inode
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

### 本章练习题

1. list 根目录下所有文件的详细信息并认识每列属性？[^3]

[^3]:
    “l”是链接文件，相当于 windows 的快捷方式；
    “b”是块设备，硬盘就是一个例子；
    “c”是字符设备文件，鼠标，键盘算是；
    “d”是目录文件，相当于 windows 的文件夹。

2. 新建目录和文件并修改：
   1. 新建一个 textdr 的目录，发现拼写错误后改名为 testdr，创建名为 testtxt 的空文件，修改他的修改日期为两天前，编辑内容为 content1；
   2. 改编拥有者为 root，**改变群组**到 root，权限设置为 owner 拥有文件全部权限，group 缺少修改文件的权限，其他人无权限也不能观察到文件的存在，只有 owner 能够使用 ls 命令看到所有文件。[^1]

[^1]: 如果希望设置 suid(Set UID)，那么就将相应的权限位之前的那一位设置为 4；如果希望设置 guid(Set GID)，那么就将相应的权限位之前的那一位设置为 2；如果希望两者都置位，那么将相应的权限位之前输入 6

3. 最后新建一个名为 new 的目录，将这个目录移动到 new 中，并将 new 文件删除
4. 阅读一份说明文档(自带的有哪些？)：
   1. 我想要查看文件尾部的签名
   2. 我想要显示行号我应该用 cat 或者 cat -n 吗
   3. more 和 less 命令如何操作
5. 平时看到的时间信息是什么时间信息？如何查看其他两种时间信息？
6. 提示符前面就是当前文件路径，所以 pwd 是一个无用的操作对吗？
   1. 不要经常用 root：如果这样说明你经常使用 root 用户操作，这可能导致无法挽回的错误，是一个坏习惯
   2. 不应该单独思考每个指令的用处：事实上在自动化获取路径中，pwd 非常有用

## Linux 磁盘和文件系统管理

### 认识 linux 文件系统

#### 文件系统特性

- 索引式文件系统[^4]

[^4]: 文件系统可以分为无结构文件系统（又称为字节流）和有结构文件系统（包括索引文件系统，顺序文件系统，还有索引顺序文件系统）

- **superblock**：文件系统整体信息
  - block 和 inode 总量
  - 已使用/未使用的 inode/block
  - block inode 大小
  - filesystem 挂载时间，最近写入数据时间(不定时同步)，最近一次校验磁盘时间
  - valid bit：显示是否怪哉(0 正常)
- **inode**：存放文件的属性信息，每个文件占用一个 inode
  - 文件存取模式
  - 文件属性如 owner group
  - 文件权限如 770
  - 容量
  - atime，ctime，mtime
  - pointer 实际指向位置
- **datablock**：实际数据存放的地方
- 非索引式文件系统(FAT,闪存盘)
  - 如果每个 block 太过分散则需要磁盘重组
  - ？这难道不是很糟糕，fat 有什么好处，而且现在的 U 盘不是也能存放文件属性吗，也就是说现在 u 爬满也不再使用 fat 了？

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

### 文件系统的简单操作

#### 概念简答

1. 比较 hardlink 和 symbolic link 的区别？
   简要来说 hardlink 指向某文件的 inode，即使改名源文件也不会影响 hardlink；而 symbolic link 指向某文件的文件名，改名会受到影响。

2. 什么是 link 数目？
   在使用 ls -l 时有一列 link 数目的属性表示有多少 link 指向该文件。mkdir 子文件夹由于自然生成..所以源文件夹 link 数目会加一.

### 磁盘的分区，格式化，检验和挂载

#### 分区，格式化

gdisk,mkfs.xfs

#### 挂载

> mount/unmont

挂载几点注意：

1. 挂载的目录理论上都应该是空目录
2. 单一文件系统不应该被挂载到不同目录
3. 单一目录不应该重复挂载多个文件系统

#### 检验

> 莫名其妙的死机非常可能导致文件系统的错乱。问题来啦，如果文件系统真的发生错乱的话，那该如何是好？就...挽救啊！

检查刚创建的/dev/vda 文件系统(检查修复之前要保证文件系统卸载)：xfs_repair /dev/vda4

#### 文件系统参数修订

**硬件设备代码（major minor）** 是逻辑上的文件和设备沟通的桥梁，可以在官网查到核心支持的硬件设备代码，具有特殊含义不可随意指定。
生成一个 pipe 文件[^2]
[^2]:字节流文件:正式的说，一个字节流是一种特定的抽象化，一个让实体（entity）可以传输一系列的字节给处在另一端实体的一种通信频道。一般来说这种频道会是双向，不过有时有单向的。在几乎所有的状况，这里的频道都具有所谓可靠的特质;也就是，在另一端会按照正确的顺序出现应该出现的字节（现实生活中有些频道，有时会顺序错误，有时会多出或者失去一些字节）。在多数的操作系统，包含类 Unix 系统和 Windows，一个行程（process）想要去获取任何文件都是一种字节流的示例。特别是每个行程都有的三个标准流（stdin, stdout, stderr），这三个字节流可视为是单向字节流的示例。**UNIX 里面 pipe 的机制常被使用于连接不同的行程，并且用来创造行程之间的字节流**。
另外一个在网络传输协议里面比较有名，且会提供字节流给客户端的示例是 TCP/IP 通信协议里面的传输控制协议（TCP），这种协议提供了双向的字节流。

mknod /tmp/pipetest p
更改设备的表头名称：
xfs_admin -L /dev/vda lablename

#### 简答

1. 现有一块新的磁盘需要使用：
   1. 必须经过哪些步骤一块磁盘能够被正确使用？
   2. 再进行分区操作之间应该进行哪两步操作？
   3. 如何进行 GPT 格式的分区？
   4. 分区之后，linux 核心没有使用新的分区表，应该是用什么操作？
   5. 如何创建 xfs 的文件系统？
   6. 在创建文件系统后，挂载之前可选的是进行什么操作？
   7. 如何挂载文件系统，如何设置自动挂载？
2. 挂载文件系统到目录时候 Mount -t [uuid]：
   1. 为什么参数 t 可以省略
   2. 为什么推荐使用 uuid 而不是 label，为什么 uuid 很难重复（x）
3. 什么是 4k 对齐？他和文件系统的 block 大小有什么关系？

   **4k 对齐**是将文件系统格式和硬盘物理结构对应起来，能够提高磁盘使用寿命，提高空间使用效率。

   > 举例来说：现时 Windows 中常见使用的 NTFS 文件系统，默认定义为 4096 字节大小为一个簇。但 NTFS 分区因为其引导区占用了一个磁道共 63 个扇区，真正的文件系统在 63 号扇区之后，这会导致每个簇都会跨越两个扇区，占据第一个扇区的后 512 字节和第二个扇区的前 3584 字节。文件系统在读写某个簇的时候，硬盘需要读写两个物理单元，这会降低读写速度，并缩短使用寿命。现时一般使用一些硬盘分区软件在主引导记录的 63 个扇区后空出数个扇区以对齐文件系统的每簇 4096 字节，以避免过多的读写操作，提升读写速度、延长使用寿命。

### 设置开机挂载

#### fstab

> **/etc/fstab** （filesystem table） 就是将我们利用 mount 指令进行挂载时， 将所有的选项与参数写入到这个文件中就是了。除此之外， /etc/fstab 还加入了 dump 这个备份用指令的支持！与开机时是否进行文件系统检验 fsck 等指令有关。

```bash
ubuntu@VM-4-5-ubuntu:~$ cat /etc/fstab
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/vda2 during curtin installation
/dev/disk/by-uuid/7bccaefa-b039-4ff6-bd32-22dde0066c0b / ext4 defaults 0 1
/dev/disk/by-id/virtio-disk-at1zqboh /root/temp_data ext4 defaults 0 0
```

可以看到分为六栏分别是

- 文件系统名字(可以填 uuid，lable，设备名)
- 挂载点
- 文件系统类型
- 挂载参数（后表）
- dump(和备份有关)
- fsck 校验扇区，xfs 文件系统会自身校验可填 0

挂载参数

| 参数        | 内容                                 |
| ----------- | ------------------------------------ |
| async/sync  | 默认性能较佳的 sync 模式             |
| auto/noauto | 默认 auto，自动挂载                  |
| rw/ro       | 默认以读写 ro 挂载                   |
| exec/noexec | 默认 exec 可执行挂载                 |
| user/nouser | 默认 nouser 挂载，仅有 root 可以挂载 |
| suid/nosuid | 默认允许 suid 生效，前提是 exec      |
| defaults    | 全部使用默认，常用                   |

#### 特殊设备的 loop 挂载

> 如果有光盘镜像文件，或者是 **使用文件作为磁盘** 的方式时，那就得要使用特别的方法来将他 挂载起来，不需要烧录啦！

1. 创建大型文件:dd if=/dev/zero of=/srv/loopdev bs=1M count=512
2. 格式化:mkfs-xfs -f /srv/loopdev
3. 挂载文件: mount -o loop UUID="7dd97bd2-4446-48fd-9d23-a8b03ffdd5ee" /mnt

> **/mnt (mount)** 此目录主要是作为挂载点使用。如挂在 windows 下的某个分区，挂载 iso 文件。
> **/media** 用于挂载多媒体设备
> **/lib** 根文件系统目录下程序和核心模块的共享库，存放着系统最基本的动态链接共享库，类似于 windows 下的 system32 目录，所有应用程序都需要用到这些库
> **/var** 包括系统运行时要改变的数据。其中包括每个系统是特定的，即不能够与其他计算机共享的目录，如/var/log，/var/lock，/var/run。有些目录还是可以与其他系统共享，如/var/mail, /var/cache/man, /var/cache/fonts,/var/spool/news。
> var 目录存在的目的是把 usr 目录在运行过程中需要更改的文件或者临时生成的文件及目录提取出来，由此**可以使 usr 目录挂载为只读的方式。隐含要求 var 目录必须挂载为可以读写的方式**。

### swap 的创建

> 说实话，swap 在目前的桌面电脑来讲，存在的意义已经不大了！这是因为目前的 x86 主机所含的内存实在都太大了 （一般入门级至少也都有 4GB 了）...如果是**针对服务器或者是工作站**这些常年上线的系统来说的话，那么，无论如何，swap 还是需要创建的。

1. dd/分区 ：gdisk(**8200**而不是默认的 linux 文件系统)/dd if=/dev/zero of=/...
2. 格式化(make filesystem):mkswap /dev/vda6
3. 挂载 swapon -a /dev/vda6
   1. swapoff
   2. swapon -s :查看哪些设备作为 swap
   3. free:查看内存使用情况
