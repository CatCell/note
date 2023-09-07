# 数据迁移

## 数据迁移方式

1. 挂载 NTFS 文件系统

```bash
# from ChatGPT
sudo apt-get install ntfs-3g
sudo fdisk -l
sudo mkdir /media/ntfs_mount
sudo mount -t ntfs-3g /dev/sdX# /media/ntfs_mount
# 进入NTFS分区查看
sudo umount /media/ntfs_mount
```

2. 调整 NTFS 分区大小

```bash

```

3. 新建 vfat4 分区

```bash

```

4. 跨文件系统迁移
5. 删除 NTFS 分区(适当预留一些空间)
6. 扩容 vfat4 分区

### 云盘备份(备选)

上传至百度云盘

## 数据分类

### 冷数据

个人档案，多媒体文件(照片视频，录音)，书库

### 应用迁移

docker,jellyfin,qbit,AB

# 选择系统盘

经过测试，两块固态性能基本一致，选择读写次数较少的 sumsang

# 硬件兼容性

现在流行 linux 操作系统在消费级硬件少有不兼容现象
