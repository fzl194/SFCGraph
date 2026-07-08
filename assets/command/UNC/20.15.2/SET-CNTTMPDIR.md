---
id: UNC@20.15.2@MMLCommand@SET CNTTMPDIR
type: MMLCommand
name: SET CNTTMPDIR（设置容器引擎临时目录）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CNTTMPDIR
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 设备管理
- 容器管理
status: active
---

# SET CNTTMPDIR（设置容器引擎临时目录）

## 功能

![](设置容器引擎临时目录（SET CNTTMPDIR）_89151642.assets/notice_3.0-zh-cn_2.png)

该命令为高危命令，此命令会修改容器引擎临时目录并复位容器引擎，可能出现容器引擎启动失败或容器引擎启动过程中业务中断，最终导致业务受损，请务必在华为技术支持人员的指导下使用该命令。

该命令用于设置节点的容器引擎临时目录。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

## 注意事项

- 若执行**SET CNTTMPDIR**返回结果节点“详细信息”为“容器引擎未启动”，请联系华为技术支持。

- 该命令存在系统初始记录，参数的初始设置值如下：
  | CNTTMPDIR |
  | --- |
  | TMPFS（内存） |

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODEIP | 节点IP | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要设置哪个节点的数据。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：无。 |
| CNTTMPDIR | 容器临时路径类型 | 可选必选说明：必选参数。<br>参数含义：用于设置指定节点IP的容器临时路径类型。<br>取值范围：<br>- “TMPFS（内存）”：容器临时路径类型为内存类型。<br>- “DISK（硬盘）”：容器临时路径类型为硬盘类型。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CNTTMPDIR]] · 容器引擎临时目录（CNTTMPDIR）

## 使用实例

1、设置 “节点IP” 为“10.0.0.0”， “容器临时路径类型” 为“TMPFS”的参数信息：

```
%%SET CNTTMPDIR: NODEIP="10.0.0.0", CNTTMPDIR=TMPFS;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------           
节点IP  =  10.0.0.0
容器临时路径类型  =  TMPFS         
详细信息  =  成功 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置容器引擎临时目录（SET-CNTTMPDIR）_89151642.md`
