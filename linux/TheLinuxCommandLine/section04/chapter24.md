# 第二十四章: 编写第一个shell脚本 #

## 24.1 什么是shell脚本 ##

shell脚本是一个包含一系列命令的文, shell读取这个文件, 然后执行文件中的所有命令.

shell不仅是一个功能强大的命令行接口, 也是一个脚本语言解释器.

## 24.2 怎样写shell脚本 ##

为了成功的创建和运行一个shell脚本, 需要做以下三件事:

1. 编写一个脚本: shell脚本就是一个普通的文本文件.
2. 使脚本文件可执行: 设置脚本文件的权限来允许其可执行.
3. 把脚本放置到shell能够找到的地方: 当没有指定可执行文件明确的路径名时, shell会自动的搜索某些目录来查找此可执行文件.

### 24.2.1 脚本文件的格式 ###

以编写一个简单的脚本hello_world为例, 脚本内容如下:

```
#!/bin/bash
# This is our first script.
echo 'Hello World!'
```

文本行中, 所有 # 符号之后的字符都会被作为注释忽略.
脚本的第一行中的 #! 字符序列是一种特殊的结构, 叫做 shebang, 用来告诉操作系统将执行此脚本所用的解释器的名字, 每个脚本都应该把这一文本行作为第一行.

### 24.2.2 可执行权限 ###

使用chmod命令修改文件的权限:

```
chmod 755 hello_world
```

为了能够执行脚本, 脚本必须是可读的.

### 24.2.3 脚本文件的位置 ###

当设置了脚本权限之后, 使用如下命令执行脚本:

```
./hello_world
```

### 24.2.4 脚本的理想位置 ###

个人所用脚本存放在 ~/bin 目录是一个不错的选择, 如果系统中的每个用户都需要使用脚本, 则传统的存放位置是 /usr/local/bin, 系统管理员使用的脚本通常存放在 /usr/local/sbin 目录.

## 24.3 更多的格式诀窍 ##

### 24.3.1 长选项名 ###

许多命令都有长短两种选项名称:

```
ls -ad
# 等价于
ls --all --directory
```

在命令行中输入选项的时候, 短选项更受欢迎; 在书写脚本的时候, 长选项能提供可读性.

### 24.3.2 缩进和行连接 ###

当使用长命令的时候, 通过把命令在几个文本行中展开, 可以提高命令的可读性:

```
find playground \( -type f -not -perm 0600 -exec
chmod 0600 '{}' ';' \) -or \( -type d -not -perm 0711 -exec chmod
0711 '{}' ';' \)
```

可以这样书写来提高可读性:

```
find playground \
    \( \
        -type f \
        -not -perm 0600 \
        -exec chmod 0600 '{}' ';' \
    \) \
    -or \
    \( \
        -type d \
        -not -perm 0711 \
        -exec chmod 0711 '{}' ';' \
    \)
```

可以使用如下方式来配置vim提高脚本书写能力:

:syntax on    打开语法高亮

:set hlsearch    高亮查找结果 

:set tabstop=4    设置tab字符等价的空格数, 默认为8

:set autoindent    自动缩进, 可以使用 Ctrl+d 停止缩进

可以将这些配置写入到 ~/.vimrc 文件中, 使配置永久生效.

## 24.5 本章结尾语 ##
