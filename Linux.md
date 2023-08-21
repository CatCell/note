# Linux

[鳥哥的 Linux 私房菜](https://linux.vbird.org/)
[Linux 入门教程](https://www.xinbaoku.com/linux_tutorial/)

## 基础知识

### 选购硬件

1. 内存：服务器内存比 CPU 重要，高峰期内存不够使用 SWAP 会显著拖慢

### 安装操作系统

1. 磁盘
   1. 分区 MBR(Master boot region) GPT
   2. 格式化 Filesystem
      1. 日志文件系统 NTFS xfs
      2. FAT 闪存
      3. block 大小 1k 2k 4k
   3. VFS 负责 linux 各种文件系统的管理
2.

#### 简答

1. Linux 安装时如果自己配置分区，为什么在使用 GPT 分区时安装程序要求设置 boot 分区？

   > GPT 分区的磁盘为了适应硬件上的 BIOS，设置了 BIOS 相容分区 LBA0，如果还有别的 Boot loader 则需要单独设置分区 BIOS boot 放置 grub 等 bootloader。
   > 此外说明，BIOS 虽然不认识 GPT 但是能通过相容分区 LBA0 读取到 bootload，如果 bootloader 不认识 GPT 如古早 winXP 配合 GPT 磁盘则找不到核心文件，启动就会失败。
   > GPT 的一个好处就是支持多个主分区，每个分区都可以格式化不影响其他分区。这是写在 LBA1 里的，他在 LBA0 之后 128\*128 字节，里面记录了 GUID，最大分区数等等，注意 128 分区和容量无关，里面记录了第一个可用分区 LBA 和最后一个可用分区 LBA 位置。
   > LBA 作用除了规定分区数之外还有检验码机制 CRC32，如果校验码出错就会使用存在最后的 34 个 LBA 区块恢复 LBA1
   > LBA 是由 LBA 区块组成的

2. 为什么 MBR 分区格式最多支持导 2TB？

   > 这个和 32 位操作系统没有关系完全是 MBR 分区表规范的原因
   > ![MBR分区表](https://img2020.cnblogs.com/blog/741682/202010/741682-20201008184307747-1604693136.gif)
   > MBR 分区表仅有 64B，而且还分成四份，一个分区记录只用了 16B，它的结构和上图是一样的，限制在于最后使用了 4B 记录之前的扇区数和总扇区数，观察一个分区表至多只能支持$2^{32}$个扇区

   $$
   2^{32+9+3}=2^{2+3+40} \tag{每个扇区512B}
   $$

   所以最多支持 2TB

3.

### 使用

1. 目录树
   1. [目录树](https://linuxhandbook.com/content/images/2020/06/linux-system-directoies-poster.png)
2. 使用者和群组，权限
   1. 使用者分组 owner,group,others
   2. 文件和目录权限
      1. 文件 r w x
      2. 目录 r 可读取目录文件名 ls，w 可以修改目录 block 即删除添加内的文件（不是修改文件内容）
   3. 数字表示方式 4r,2w,1x
3. 存储
   1. 创建目录:Group block
   2.

## 案例

1. 由于我的系统原本分区的不够好，我的用户希望能够独立一个 filesystem 附挂在 /srv/myproject 目录下。 那你该如何创建新的 filesystem ，并且让这个 filesystem 每次开机都能够自动的挂载到 /srv/myproject ， 且该目录是给 project 这个群组共享的， 其他人不可具有任何权限。且该 filesystem 具有 1GB 的容量。
   > 创建分区并且进行格式化
   > gdisk /dev/vda
   > partprobe
   > mkfs.xfs /dev/vda
   > 在指定目录创建文件夹并配置自动挂载配置文件
   > mkdir automountfolder
   > vi /etc/fstab /dev/vda3 /srv/automountfolder
   > mount -a
   > 设置权限
   > chgrp /dev/vda3 users
   > chmod 2770 /dev/vda3
   > 测试是否符合要求
   > df /srv/users
   > ls -al
2. 我想要寻找名为 passwd 的文件，他在一个月之前创建，我应该如何寻找？
   > 如果是很久之间建立的文件，那么索引中已经存在，可以用 locate；否则首先受用 whereis，最后的选择 find
3. 运维准备为不同的用户使用不同的欢迎界面，技术人员希望在欢迎界面中标注内核版本，操作系统版本，终端机接口,硬件等级，网络名称。普通用户希望得到日期和可视化的界面。
   Ubuntu 系统较为曲折，以 CentoS 为例
   前者：\r\S\l \m \n
   后者：\d\t
4. ls，cd 是最常使用的指令，找出他们是如何被 kernal 使用的。
   > type ls # alias ''
   > **type** cd #built-in command
   > cd 式 bash 内置的,ls 有两个可执行文件，但他是加上参数‘--color=auto’作为别名
5. 把/data 内以非小写字母开头，中间有数字，结尾为中间字符为 a 的 5 个字符的文件复制到临时目录中去?
   > mkdir /tmp/test ; cp -a /data/[^a-z]\*[0-9]\*??a?? /tmp/test
6. cat 创建一个由键盘输入内容文件，在不清楚目录是否存在的情况下创建文件
   > ll /test||touch /test&&cat > /test/txt
   > 如果交换顺序是不行的，会导致在目录存在的时候重复创建，不存在的时候在不存在的目录上新建文件
7. xargs 是一个常用的，分析下面那些会被执行成功，为什么？

```bash
[dmtsai@study ~]$ id $(cut -d ':' -f 1 /etc/passwd | head -n 3)
[dmtsai@study ~]$ cut -d ':' -f 1 /etc/passwd | head -n 3 | id
[dmtsai@study ~]$ cut -d ':' -f 1 /etc/passwd | head -n 3 | xargs id
[dmtsai@study ~]$ cut -d ':' -f 1 /etc/passwd | head -n 3 | xargs -n 1 id
```

第一句话在 centos 因为 id 金额能接受一个参数所以会失败，但是在 ubuntu 是可以成功的
第二个命令由于 id 不是管道命令所以会失败
第三同第二
第四是一定可以成功的，他分别处理参数
