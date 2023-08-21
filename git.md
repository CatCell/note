# Git 教程

[廖雪峰 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600/896067008724000 "史上最浅显易懂的git教程")

## git 简介

### 概念

- 工作区，暂存区，版本库
  - **工作区(working directory)**：电脑里看到的目录，不包括.git
  - **版本库(repository)**：.git 目录
  - **暂存区**：git add 后文件所在位置，commit 会将暂存区内容一次提交至 repository
- 分布式版本控制系统和中心式版本控制系统

case：

- git 是管理修改而不是文件：可以将修改分布 git add git commit，这样是不同的，每次的修改都会被记录

### 安装 Git

windows 较简单
设置好环境变量

### 创建版本库

- git init：用于初始化 git 仓库会生成一个.git 文件夹
- git add /folder1/file：将新文件(更改文件内容，添加文件，移动文件，删除文件都是这个命令)移动至暂存区
- git commit -m "information about commit ":将新文件从暂存区移动至 repository

## 时光机穿梭

- git diff [filename] :具体查看做了哪些修改 ，用在 git add 之前否则不显示修改
- git status：查看 git 状态（暂未添加到暂存区的红色，改变都在暂存区的绿色，还有 clean）常用在 git commit 之前

- git log <--pretty=oneline>:查看修改日志，上有 commit id 相当于版本代号
- git reset --hard \< commit id \>：将版本变为 commit id 的版本（升降均可）
- git reflog：输出所有 commit id

- git checkout \< filename \>:工作区文件回到最近一次 git add 或者 commit 的状态，在文档里写老板小作文还没 add
- git reset Head \< file \>：暂存区文件 clean，工作区修改不变。写了老板的小作文 md

## 远程仓库

### 创建 RSA 公私钥匙对

```bash
ssh-keygen -t rsa -C "mail"
```

之后在 github 里添加公钥，用于确认每次 commit 某个库时你的身份不会被冒充。相应的修改权限的库应该请求管理员添加你指定的公钥。
? 我在 git 文件夹新建了 rsa 钥匙对，然后添加了公钥到 github 账号
必须把私钥公钥放在.ssh 文件夹中

```bash
git clone git@github.com:CatCell/gitskill
cd git remote -v:发现设置好了不需要 git remote add origin git@github.com/...
# 本地修改文件，commit
git pull # 检查当前版本是否是远程的最新版本
git push origin main #或者别的分支

# 改变分支
git push origin main

# 似乎会智能创建和本地同名的分支,能不能本地分支和远程分支不同名然后push
git push orgin localbranch:remotebranch
git pull orgin remotebranch:localbranch
git pull #当同名分支拉去到当前分支上

# 冲突不能一个账号测试出来，因为每次push都是最新的，不会检测冲突
```

### 关联，推送，解除绑定，删除远程库

- git remote add origin git@github.com:username/reponame：添加绑定关系
- git push [-u] origin master：将本地修改的内容推送到远程库 origin 的 master 分支
- git remote rm origin
- 删除远程库：在 github 上手动删除库

- git clone git@github.com:克隆一份库到本地

## 分支管理

### 原理

通过创建 dev 指针和切换 head 指针指向 dev 或者 master 指针来切换目录

- git branch < branchname > :创建新分支，如果只有 branch 则是查看当前分支
- git switch [-c] dev：切换到 xx 分支
- git merge \< the exp to now branch \>：将分支合并到当前分支,注意这一步如果是同名文件部分内容可能冲突。
- git merge --no-ff -m "info" dev
- git branch -d dev ：删除 dev 分支

### 暂存

- git stash:暂存当前
- git stash list:展示算是暂存
- git stash pop: git stash apply stash@{0} git stash drop：恢复暂存
- git cherry-pick [commit id]： 对当前分支进行这次修改

### 解决冲突

解决冲突问题：保留一方或者都保留

### 弃用 feature 分支

- git branch -D [branchname]:删除未合并分支

### 多人工作模式流程

- git checkout -b dev origin/dev:git branch dev /origin/dev 行吗？默认
- git push origin dev：不需要写 origin/dev 吗
- git branch --set-upstream-to <branch-name> origin/<branch-name>：？和上一个命令对比
- git pull:如果不是最新

### rebase 解决 merge 分支问题

当多人协作时经常出现 push 时需要先 pull 别人的修改，这样会导致 log 出现很多分叉不便于阅读，于是使用 git rebase
这就让我们实际基于原本快照放在所有操作之前，将别人的操作不基于原快照。虽然我们先 pull 再 push 的操作基于别人的版本，但是 gitbash 可以改变这种不必要的逻辑关系，同样达到效果。
效果见下方
为什么我在本地 git base 没有成功？

```bash
$ git rebase
There is no tracking information for the current branch.
Please specify which branch you want to rebase against.
See git-rebase(1) for details.

    git rebase '<branch>'

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=<remote>/<branch> master
```

```bash
$ git log --graph --pretty=oneline --abbrev-commit
*   e0ea545 (HEAD -> master) Merge branch 'master' of github.com:michaelliao/learngit
|\
| * f005ed4 (origin/master) set exit=1
* | 582d922 add author
* | 8875536 add comment
|/
* d1be385 init hello

# git rebase
$ git log --graph --pretty=oneline --abbrev-commit
* 7e61ed4 (HEAD -> master) add author
* 3611cfe add comment
* f005ed4 (origin/master) set exit=1
* d1be385 init hello
```

## 标签管理

标签指向 是 commit id 更有意义的名字

- git tag -a "tagnamev1" -m "append GPL" [commit id]:添加标签

- git tag -d [tagname]:删除标签
- git push origin [tagname]/--tags：push 标签，所有标签
- git push origin: refs/tags/[tagname]：删除远程标签

## 使用 Github & Gitee

## 自定义 Git

### .gitignore

某些需要放在工作目录但是不应该放在 repository 的，比如垃圾文件，数据库密码配置文件。
书写 ignore 的语法规则:

```text
# 排除所有.开头的隐藏文件:
.*
# 排除所有.class文件:
*.class

# 不排除.gitignore和App.class:
!.gitignore
!App.class

```

[gitignore generator](https://gitignore.itranswarp.com/)
[github/gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)

### alias

可以让自己偷懒少输入点字
git config --global alias.st status
git config --global alias.unstage "reset HEAD"
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
global 配置文件在 .gitconfig
每个仓库在 .git/config

### 自己搭建 git 服务器

1. 创建用户运行 git 服务
2. 收集公钥
3. 禁用 shell 服务
