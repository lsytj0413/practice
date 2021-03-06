# Linux #

本目录下存放与linux相关的一些文本记录.

## 书籍笔记 ##

- [<The Linux Command Line读书笔记>](./TheLinuxCommandLine)
- [<LinuxShell脚本攻略 读书笔记>](./LinuxShellScriptingCookbook)

## Linux ##

### 查看CPU详情 ###

- 具有相同 core id 的 CPU 是同一个 core 的超线程
- 具有相同 physical id 的 CPU 是同一个 CPU 封装的线程或核心

```
# 物理 CPU 个数
cat /proc/cpuinfo | grep "physical id" | sort | uniq | wc -l
# 每个物理CPU的 core个数(核数)
cat /proc/cpuinfo | grep "cpu cores" | uniq
# 逻辑CPU个数
cat /proc/cpuinfo | grep "processor" | wc -l
```

### 查看内存使用情况 ###

```
$ free -m
              total        used        free      shared  buff/cache   available
Mem:           7879        2315         671        1283        4891        3924
Swap:          3814           0        3814
# total: 内存总数
# used: 已使用
# free: 空闲
# shsared: 多个进程共享的内存总数
# buffers/cache: 缓存
# available: 可用
```

### 查看硬盘使用情况 ###

#### 查看硬盘及分区 ####

```
$ fdisk -l
Disk /dev/nvme0n1: 238.5 GiB, 256060514304 bytes, 500118192 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 7589C78C-EA41-4C6D-AF7B-4B065A9060F3

设备              Start    末尾    扇区   Size 类型
/dev/nvme0n1p1     2048    391167    389120   190M EFI System
/dev/nvme0n1p2   391168   4296703   3905536   1.9G Linux filesystem
/dev/nvme0n1p3  4296704  62889983  58593280    28G Linux filesystem
/dev/nvme0n1p4 62889984  70703103   7813120   3.7G Linux swap
/dev/nvme0n1p5 70703104 500117503 429414400 204.8G Linux filesystem
```

#### 查看磁盘空间占用 ####

```
$ df -h
文件系统        容量  已用  可用 已用% 挂载点
udev            3.9G     0  3.9G    0% /dev
tmpfs           788M  9.5M  779M    2% /run
/dev/nvme0n1p3   28G  9.1G   17G   35% /
tmpfs           3.9G  107M  3.8G    3% /dev/shm
tmpfs           5.0M  4.0K  5.0M    1% /run/lock
tmpfs           3.9G     0  3.9G    0% /sys/fs/cgroup
/dev/nvme0n1p2  1.9G  152M  1.6G    9% /boot
/dev/nvme0n1p5  202G   22G  170G   12% /home
/dev/nvme0n1p1  188M  3.5M  184M    2% /boot/efi
tmpfs           788M  116K  788M    1% /run/user/1000
```

#### 查看硬盘I/O ####

```
$ iostat -x 1 10
Linux 4.4.0-81-generic (soren-ubuntu16) 	2017年06月26日 	_x86_64_	(4 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
          16.09    0.07    3.45    0.88    0.00   79.52

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    2.90   16.48    75.72   347.22    43.64     0.02    1.21    0.33    1.37   0.26   0.51

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.75    0.00    0.75    0.25    0.00   98.25

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.79    0.00    0.00    0.26    0.00   98.95

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.26    0.00    0.50    0.25    0.00   97.99

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.76    0.00    0.75    0.25    0.00   97.24

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.75    0.00    0.50    0.25    0.00   98.50

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00   10.00     0.00    40.00     8.00     0.00    0.40    0.00    0.40   0.40   0.40

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.75    0.00    0.25    0.25    0.00   98.75

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.50    0.00    0.00    0.00    0.00   99.50

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.01    0.00    0.00    0.25    0.00   98.74

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.50    0.00    0.50    0.25    0.00   98.75

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.75    0.00    0.25    0.00    0.00   98.99

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.25    0.00    0.25    0.25    0.00   98.25

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.50    0.00    0.00    0.25    0.00   98.25

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.51    0.00    0.00    0.00    0.00   99.49

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.25    0.00    0.25    0.25    0.00   98.25

Device:         rrqm/s   wrqm/s     r/s     w/s    rkB/s    wkB/s avgrq-sz avgqu-sz   await r_await w_await  svctm  %util
nvme0n1           0.00     0.00    0.00    0.00     0.00     0.00     0.00     0.00    0.00    0.00    0.00   0.00   0.00
```

各参数说明如下表:

| 参数 | 描述 | 备注 |
|:--|:--|:--|
| rrqm/s | 每秒进行 merge 的读操作数目, 即 delta (rmerge) /s | |
| wrqm/s | 每秒进行 merge 的写操作数目, 即 delta (wmerge) /s | |
| r/s | 每秒完成的读I/O设备次数, 即 delta (rio) /s | |
| w/s | 每秒完成的写I/O设备次数, 即 delta (wio) /s | |
| rsec/s | 每秒读扇区数, 即 delta (rsect) /s | |
| wsec/s | 每秒写扇区数, 即 delta (wsect) /s | |
| rkB/s | 每秒读K字节数, 是 rsect/s 的一半, 因为每扇区大小为512字节 | |
| wkB/s | 每秒写K字节数, 是 wsect/s 的一半 | |
| avgrq-sz | 平均每次设备I/O操作的数据大小, 即 delta (resct + wsect) / delta (rio + wio) | |
| avgqu-sz | 平均I/O队列长度, 即 delta (aveq) /s/1000, aveq单位为毫秒 | |
| await | 平均每次设备I/O操作等待时间, 毫秒, 即 delta (ruse + wuse) / delta (rio + wio) | |
| r_await | 平均每次读设备I/O操作等待时间, 毫秒, 即 delta (ruse) / delta (rio) | |
| w_await | 平均每次写设备I/O操作等待时间, 毫秒, 即 delta (wuse) / delta (wio) | |
| svctm | 平均每次I/O操作的服务时间, 毫秒, 即 delta (use) / delta (rio + wio) | |
| % util | 一秒中有百分之多少时间用于I/O操作, 等价于一秒中有多少时间I/O队列非空, 即 delta (use) /s/1000, use单位为毫秒 | |

一般会关注以下方面:

- 如果 % util 接近100%, 说明 I/O系统已经满负荷, 磁盘可能存在瓶颈
- 如果 idle 小于 70%, I/O压力一般比较大, 进程中有较多的 wait, 同时可以结合 vmstat 查看 b 参数(等待资源的进程数) 和 wa 参数(I/O等待占用的CPU时间百分比, 大于30%则为I/O压力高)
- svctm 应该小于 await, 请求过多会导致 svctm 增加
- await 大小取决于服务时间(svctm)以及 I/O 队列的长度和 I/O 请求的发出模式, 如果 svctm 接近于 await, 说明 I/O 几乎没有等待时间; 如果 await 远大于 svctm, 说明 I/O 队列太长

#### 查看目录大小 ####

```
$ du -sh /root
# 找出目录中占用空间最多的前10个文件或目录
$ du -d0 -cks * | sort -rn | head -n 10
```

#### dd ####

dd 命令可以把指定的输入文件拷贝到指定的输出文件中, 并且在拷贝过程中可以进行格式转换:

```
# 制作交换文件
$ dd if=/dev/zero of=/swapfile bs=1024 count=65536

# 制作驱动盘
$ dd if=rhel40.img of=/dev/fd0 bs=10k
# 或
$ dd if=mptlinux-3.02.68-1-rhel4.i686.dd of=/dev/fd0 bs=10k

# 制作ISO镜像, 可以使用 mkisofs 命令
$ dd if=/dev/cdrom of=/root/cd1.iso
```

dd 命令常用参数如下表:

| 参数 | 描述 | 备注 |
|:--|:--|:--|
| if=file | 输入文件, 默认为标准输入 | |
| of=file | 输出文件, 默认为标准输出 | |
| ibs=bytes | 一次读入 bytes 个字节, 即一个块大小为 bytes 字节 | |
| obs=bytes | 一次写 bytes 个字节, 即一个块大小为 bytes 字节 | |
| bs=bytes | 同时设置读写块的大小为 bytes | |
| cbs=bytes | 一次转换 bytes 字节, 即转换缓冲区大小 | |
| skip=blocks | 从输入文件开头跳过 blocks 个块之后开始复制 | |
| seek=blocks | 从输出文件开头跳过 blocks 个块之后开始复制 | |
| count=blocks | 仅拷贝 blocks 个块 | |

### 系统平均负载 ###

```
# 使用uptime
$ uptime
 20:33:52 up 11:44,  1 user,  load average: 0.25, 0.21, 0.18

# 使用 w 命令
$ w
 20:34:34 up 11:44,  1 user,  load average: 0.33, 0.24, 0.20
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
soren    tty7     :0               日08   35:44m 35:53   0.46s /sbin/upstart --user

# 使用 top 命令
$ top
top - 20:35:16 up 11:45,  1 user,  load average: 0.43, 0.28, 0.21
Tasks: 229 total,   2 running, 227 sleeping,   0 stopped,   0 zombie
%Cpu(s): 14.4 us,  3.0 sy,  0.1 ni, 81.6 id,  0.9 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem :  8068220 total,   273228 free,  2466728 used,  5328264 buff/cache
KiB Swap:  3906556 total,  3906556 free,        0 used.  3802932 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND                                                                                                            
 2419 soren     20   0 1448112 130808  76240 S  18.8  1.6  37:09.91 compiz                                                                                                             
 1078 root      20   0 1411612 900224 878700 S  12.5 11.2  35:57.36 Xorg                                                                                                               
25357 root      20   0   45612   3764   3092 R  12.5  0.0   0:00.03 top                                                                                                                
 3004 soren     20   0 2693960 556480 245960 S   6.2  6.9  32:59.75 chromium-browse                                                                                                    
31646 soren     20   0 1251204 174180  53344 R   6.2  2.2   1:04.57 evince                                                                                                             
    1 root      20   0  187488   8184   4048 S   0.0  0.1   0:02.65 systemd                                                                                                            
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.03 kthreadd                                                                                                           
    3 root      20   0       0      0      0 S   0.0  0.0   0:00.38 ksoftirqd/0                                                                                                        
    5 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/0:0H                                                                                                       
    7 root      20   0       0      0      0 S   0.0  0.0   1:02.16 rcu_sched                                                                                                          
    8 root      20   0       0      0      0 S   0.0  0.0   0:00.00 rcu_bh                                                                                                             
    9 root      rt   0       0      0      0 S   0.0  0.0   0:00.08 migration/0                                                                                                        
   10 root      rt   0       0      0      0 S   0.0  0.0   0:00.26 watchdog/0                                                                                                         
   11 root      rt   0       0      0      0 S   0.0  0.0   0:00.25 watchdog/1                                                                                                         
   12 root      rt   0       0      0      0 S   0.0  0.0   0:00.07 migration/1                                                                                                        
   13 root      20   0       0      0      0 S   0.0  0.0   0:00.85 ksoftirqd/1                                                                                                        
   15 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/1:0H                                                                                                       
   16 root      rt   0       0      0      0 S   0.0  0.0   0:00.24 watchdog/2                                                                                                         
   17 root      rt   0       0      0      0 S   0.0  0.0   0:00.08 migration/2                                                                                                        
   18 root      20   0       0      0      0 S   0.0  0.0   0:00.42 ksoftirqd/2                                                                                                        
   20 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/2:0H                                                                                                       
   21 root      rt   0       0      0      0 S   0.0  0.0   0:00.24 watchdog/3                                                                                                         
   22 root      rt   0       0      0      0 S   0.0  0.0   0:00.18 migration/3                                                                                                        
   23 root      20   0       0      0      0 S   0.0  0.0   0:00.24 ksoftirqd/3                                                                                                        
   25 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kworker/3:0H                                                                                                       
   26 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kdevtmpfs                                                                                                          
   27 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 netns                                                                                                              
   28 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 perf                                                                                                               
   29 root      20   0       0      0      0 S   0.0  0.0   0:00.05 khungtaskd                                                                                                         
   30 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 writeback                                                                                                          
   31 root      25   5       0      0      0 S   0.0  0.0   0:00.00 ksmd                                                                                                               
   32 root      39  19       0      0      0 S   0.0  0.0   0:01.70 khugepaged                                                                                                         
   33 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 crypto                                                                                                             
   34 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kintegrityd                                                                                                        
   35 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 bioset                                                                                                             
   36 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kblockd                                                                                                            
   37 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 ata_sff                                                                                                            
   38 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 md                                                                                                                 
   39 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 devfreq_wq                                                                                                         
   43 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kswapd0                                                                                                            
   44 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 vmstat                                                                                                             
   45 root      20   0       0      0      0 S   0.0  0.0   0:00.04 fsnotify_mark                                                                                                      
   46 root      20   0       0      0      0 S   0.0  0.0   0:00.00 ecryptfs-kthrea                                                                                                    
   62 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 kthrotld                                                                                                           
   63 root       0 -20       0      0      0 S   0.0  0.0   0:00.00 acpi_thermal_pm      
```

其中 load average 字段表示的是过去的 1分钟, 5分钟和 15分钟进程队列中的平均进程数量.

### 系统其他参数 ###

#### wmstat ####

vmstat 可以用来观察系统的进程状态, 内存使用情况, 虚拟内存的使用情况, 磁盘I/O, 中断, 上下文切换, CPU的使用情况等性能信息.

```
$ vmstat 1 4
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 272988 386556 4936696    0    0    24   116  281  130 14  3 82  1  0
 0  0      0 273468 386556 4936804    0    0     0     0  262  564  2  0 98  0  0
 0  0      0 273468 386556 4936804    0    0     0     0  297  932  2  0 98  0  0
 1  0      0 273344 386556 4936804    0    0     0     0  402 1440  1  0 99  0  0
```

显示的信息描述如下:

- procs
    - r: 等待运行的进程数
    - b: 处在非中断睡眠状态的进程数
    - w: 被交换出去的可运行的进程数
- memory
    - swap: 虚拟内存的使用情况, 单位为 KB
    - free: 空闲的内存, 单位为 KB
    - buff: 被用作缓存的内存, 单位为 KB
- swap
    - si: 从磁盘交换到内存的交换页数量, 单位为 KB
    - so: 从内存交换到磁盘的交换页数量, 单位为 KB
- io
    - bi: 发送到块设备的块数, 单位为块
    - bo: 从块设备接收的块数, 单位为块
- system
    - in: 每秒的中断数, 包括时钟终端
    - cs: 每秒的环境(上下文)切换次数
- cpu
    - us: CPU使用时间, 百分比
    - sy: CPU系统使用时间, 百分比
    - id: 闲置时间, 百分比

默认情况下, r应该小于5, b应该约等于0. 假设出现如下情况:

- r 经常大于3或4, 且 id 经常小于50, 表示CPU负载大
- bi, bo 长期不等于0, 表示内存不足
- disk 经常不等于0, 且在 b 列中的队列大于2或3, 表示I/O性能不好

#### 查看系统内核 ####

```
# 查看内核版本
$ uname -a
$ uname -r

# 判断系统是 32 还是 64 位, 通过查找 /lib64 目录
$ ls -lF | grep /$
# 通过 file 命令判断系统位数
$ file /sbin/init
```

#### 查看发行版信息 ####

```
$ lsb_release -a
$ cat /proc/version
$ cat /proc/issue
```

#### 查看已加载模块 ####

```
# 查看 lvs 模块是否已经载入
$ lsmod | grep ip_vs
```

#### 查找 PCI 设置 ####

```
# 查看网卡信息
$ lspci | grep Ether
```

### 网络配置 ###

#### 配置网卡 ####

```
# 检查网卡是否正常安装
$ lspci | grep Ether
$ dmesg | grep error

# 编辑网卡文件
$ vim /etc/network/interfaces
```

#### 修改 hostname ####

```
$ vim /etc/hostname
```

#### 修改 hosts ####

```
$ vim /etc/hosts
```

#### DNS ####

```
# 修改resolv
$ vim /etc/resolvconf/resolv.conf.d/base
nameserver 8.8.8.8

# 使修改生效
$ resolvconf -u
```

#### 查看网络配置 ####

```
$ ifconfig
$ ifconfig eth0

$ ifconfig eth0 | grep "inet addr" | awk -F[:" "]+ '{print $4}'
```

#### ping ####

```
$ ping -c 5 www.163.com
```

#### netstat ####

该命令的功能是显示网络连接, 路由表和网络接口的信息. 常用的参数如下表:

| 参数 | 描述 |
|:--|:--|
| -A | 显示任何关联的协议控制块的地址, 主要用于调试 |
| -a | 显示所有套接字状态, 一般不显示与服务器进程相关联的套接字 |
| -i | 显示自动配置接口的状态, 在系统引导后配置的接口状态不在输出 |
| -m | 显示网络存储器的使用情况 |
| -n | 打印实际地址, 而不是显示主机或网络名 |
| -r | 打印路由选择表 |
| -f address | 对给出名字的地址簇打印统计数字和控制块信息, 支持 inet |
| -I interface | 只打印给出名字的接口状态 |
| -p protocol-name | 只打印给出名字的统计数字和协议控制块信息 |
| -s | 打印每个协议的统计数字 |
| -t | 在输出显示中用时间信息代替队列长度信息 |

```
$ netstat -an | grep -v unix
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:902             0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:8307          0.0.0.0:*               LISTEN     
tcp        0      0 127.0.1.1:53            0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:1080          0.0.0.0:*               LISTEN     
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN     
tcp        0      0 127.0.0.1:1080          127.0.0.1:44480         ESTABLISHED
tcp        1      0 192.168.0.106:35758     101.201.173.115:80      CLOSE_WAIT 
tcp        0    378 192.168.0.106:40962     61.55.167.91:80         ESTABLISHED
tcp        0      1 192.168.0.106:39982     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40010     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39960     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39962     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39996     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39958     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39990     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40026     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40040     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40038     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39928     93.46.8.89:443          SYN_SENT   
tcp        1      0 192.168.0.106:35730     101.201.173.115:80      CLOSE_WAIT 
tcp        0      1 192.168.0.106:39998     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39970     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39992     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40022     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39942     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39986     93.46.8.89:443          SYN_SENT   
tcp        0      0 192.168.0.106:54180     115.159.241.221:443     ESTABLISHED
tcp        0      1 192.168.0.106:40008     93.46.8.89:443          SYN_SENT   
tcp        0      0 192.168.0.106:35334     192.30.253.124:443      ESTABLISHED
tcp        0      1 192.168.0.106:39974     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40000     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39954     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40028     93.46.8.89:443          SYN_SENT   
tcp        0      0 127.0.0.1:44480         127.0.0.1:1080          ESTABLISHED
tcp        0      1 192.168.0.106:40024     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40002     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39932     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39972     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39978     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39980     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39936     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39944     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39966     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40034     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39934     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40020     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40030     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40006     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39988     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40014     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39964     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39946     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39984     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40036     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39948     93.46.8.89:443          SYN_SENT   
tcp        0      0 192.168.0.143:55740     192.168.0.50:139        ESTABLISHED
tcp        0      1 192.168.0.106:41610     61.135.186.152:80       FIN_WAIT1  
tcp        0      1 192.168.0.106:40018     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39930     93.46.8.89:443          SYN_SENT   
tcp        0      0 192.168.0.106:38802     45.76.103.176:1160      ESTABLISHED
tcp        0      1 192.168.0.106:39938     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39940     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39976     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40032     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39994     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39950     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40012     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39952     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40016     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:40004     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39968     93.46.8.89:443          SYN_SENT   
tcp        0      1 192.168.0.106:39956     93.46.8.89:443          SYN_SENT   
tcp6       0      0 :::902                  :::*                    LISTEN     
tcp6       0      0 :::443                  :::*                    LISTEN     
udp        0      0 127.0.0.1:1080          0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*                          
udp        0      0 0.0.0.0:5353            0.0.0.0:*                          
udp        0      0 0.0.0.0:39229           0.0.0.0:*                          
udp        0      0 127.0.1.1:53            0.0.0.0:*                          
udp        0      0 0.0.0.0:68              0.0.0.0:*                          
udp        0      0 0.0.0.0:49708           0.0.0.0:*                          
udp        0      0 0.0.0.0:631             0.0.0.0:*                          
udp6       0      0 :::5353                 :::*                               
udp6       0      0 :::5353                 :::*                               
udp6       0      0 :::5353                 :::*                               
udp6       0      0 :::5353                 :::*                               
udp6       0      0 :::42656                :::*                               
raw        0      0 0.0.0.0:1               0.0.0.0:*               7          
raw6       0      0 :::58                   :::*                    7          
活跃的UNIX域套接字 (服务器和已建立连接的)
Proto RefCnt Flags       Type       State         I-Node   路径
```

state 字段的含义如下:

- LISTEN: 侦听来自远方的TCP端口的连接请求
- SYN_SENT: 在发送连接请求后等待匹配的连接请求
- SYS_RECEIVED: 在收到和发送一个连接请求后等待对方对连接请求进行确认
- ESTABLISHED: 代表一个打开的连接, 作为并发连接数
- FIN\_WAIT\_1: 等待远程TCP连接中断请求, 或先前的连接中断请求的确认
- FIN\_WAIT\_2: 从远程TCP等待连接中断请求
- CLOSE\_WAIT: 等待从本地用户发来的连接中断请求
- CLOSING: 等待远程TCP对连接中断请求的确认
- LAST\_ACK: 等待原来发向远程TCP的连接中断请求的确认
- TIME\_WAIT: 等待足够的时间以确保远程TCP接收到连接中断请求的确认
- CLOSED: 没有任何连接状态

```
# 统计网络连接状态
$ netstat -an | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

# 查看路由表
$ route -n
# 等价于
$ netstat -r

# 跟踪网络包路径
$ traceroute www.163.com
```

#### nslookup ####

```
# 查询域名对应的IP
$ nslookup www.baidu.com
Server:		127.0.1.1
Address:	127.0.1.1#53

Non-authoritative answer:
www.baidu.com	canonical name = www.a.shifen.com.
Name:	www.a.shifen.com
Address: 180.97.33.107
Name:	www.a.shifen.com
Address: 180.97.33.108

# 等价于
$ dig www.baidu.com

; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.baidu.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39120
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 5, ADDITIONAL: 6

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;www.baidu.com.			IN	A

;; ANSWER SECTION:
www.baidu.com.		134	IN	CNAME	www.a.shifen.com.
www.a.shifen.com.	71	IN	A	180.97.33.107
www.a.shifen.com.	71	IN	A	180.97.33.108

;; AUTHORITY SECTION:
a.shifen.com.		110	IN	NS	ns3.a.shifen.com.
a.shifen.com.		110	IN	NS	ns2.a.shifen.com.
a.shifen.com.		110	IN	NS	ns4.a.shifen.com.
a.shifen.com.		110	IN	NS	ns5.a.shifen.com.
a.shifen.com.		110	IN	NS	ns1.a.shifen.com.

;; ADDITIONAL SECTION:
ns1.a.shifen.com.	110	IN	A	61.135.165.224
ns2.a.shifen.com.	110	IN	A	180.149.133.241
ns3.a.shifen.com.	110	IN	A	61.135.162.215
ns4.a.shifen.com.	110	IN	A	115.239.210.176
ns5.a.shifen.com.	110	IN	A	119.75.222.17

;; Query time: 3 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Mon Jun 26 21:44:06 CST 2017
;; MSG SIZE  rcvd: 271
```

#### finger ####

```
# 查询用户信息
$ finger
```

#### lsof ####

lsof 是一个列出当前系统打开文件的工具.

```
# 查看22端口的占用
$ lsof -i:22
```

### 服务器优化 ###

#### 调整 TCP/IP 参数 ####

```
$ vim /etc/sysctl.conf
net.ipv4.tcp_syncookies=1
# 减少 TIME_WAIT
net.ipv4.tcp_fin_timeout=30
net.ipv4.tcp_keepalive_time=1200
net.ipv4.tcp_syncookies=1
net.ipv4.tcp_tw_reuse=1
net.ipv4.tcp_tw_recycle=1
net.ipv4.ip_local_port_range=1024 65000
net.ipv4.tcp_max_syn_backlog=8192
net.ipv4.tcp_max_tw_byckets=5000

$ sysctl -p
```

#### 调整最大文件打开数 ####

```
$ vim /etc/security/limits.conf
* soft nofile 60000
* hard nofile 65535

$ vim /etc/rc.local
ulimit -SHn 65535
```

### CentOS6 安装软件 ###

#### 配置源 ####

首先备份原有的源列表:

```
mkdir /opt/centos-yum.bak
mv /etc/yum.repos.d/* /opt/centos-yum.bak/
```

然后下载 aliyun 的源文件:

```
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
```

最后清空缓存:

```
yum clean all
yum makecache
yum list
```

安装第三方的 yum 源:

```
wget http://mirrors.ustc.edu.cn/fedora/epel/6/i386/epel-release-6-8.noarch.rpm
rpm -ivh epel-release-6-8.noarch.rpm
```

有可能出现如下错误:

```
Cannot retrieve metalink for repository: epel. Please verify its path and try again
```

这时可以尝试执行以下命令来修复:

```
yum --disablerepo=epel -y update  ca-certificates
```

#### MongoDB ####

首先编辑 /etc/yum.repos.d/mongodb-org-3.4.repo 文件, 输入以下内容:

```
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
```

然后执行以下命令安装即可:

```
yum repolist
yum install mongodb-org -y
```

#### Redis ####

```
yum install redis
```

#### Nginx ####

```
yum install nginx
```

#### Py3 ####

```
yum list | grep python3
yum install python34

# 安装 pip3
yum install python34-devel
yum install python34-setuptools
cd /usr/lib/python3.4/site-packages
python3 easy_install.py pip
```
