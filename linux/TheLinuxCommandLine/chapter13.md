# 第十三章: 定制提示符 #

## 13.1 提示符的分解 ##

系统默认的提示符如下:

```
soren@soren-ubuntu16:~$ 
```
在提示符中包含了用户名, 主机名和当前的工作目录. 提示符是由名为PS1的环境变量定义的.

shell提示符中使用的转义字符如下表:

| 转义字符 | 含义 |
|:--|:--|
| \a | ASCII铃声 |
| \d | 当前日期, 用星期, 月, 日的形式显示 |
| \h | 本地机器的主机名, 不带域名 |
| \H | 完整的主机名 |
| \j | 当前shell会话中进行的任务个数 |
| \l | 当前终端设备名称 |
| \n | 换行符 |
| \r | 回车符 |
| \s | shell程序的名称 |
| \t | 24小时制的当前时间, 格式为小时:分钟:秒 |
| \T | 12小时制的当前时间 |
| \@ | 12小时制的当前时间, 格式为 AM/PM |
| \A | 24小时制的当前时间, 格式为小时:分钟 |
| \u | 当前用户的用户名 |
| \v | shell版本号 |
| \V | shell的版本号和发行号 |
| \w | 当前工作目录名 |
| \W | 当前工作目录名的最后一部分 |
| \! | 当前命令的历史编号 |
| \# | 当前shell会话中输入的命令数 |
| \$ | 在非管理员权限下输出[$], 管理员权限下输出[#] |
| \[ | 标志一个或多个非打印字符序列的开始, 用于嵌入非打印的控制字符, 比如移动光标或更改文本颜色 |
| \] | 标志着非显示字符序列的结束 |

## 13.2 尝试设计提示符 ##

## 13.3 添加颜色 ##

## 13.4 移动光标 ##

## 13.5 保存提示符 ##