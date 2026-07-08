---
id: UDG@20.15.2@MMLCommand@DSP CNTTMPDIR
type: MMLCommand
name: DSP CNTTMPDIR（查询容器引擎临时目录）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CNTTMPDIR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 容器管理
status: active
---

# DSP CNTTMPDIR（查询容器引擎临时目录）

## 功能

该命令用于查询节点的容器引擎临时目录。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。

> **说明**
> 若执行 **DSP CNTTMPDIR** 返回结果中某节点 “详细信息” 为“容器引擎未启动”，请联系华为技术支持。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODEIP | 节点IP | 可选必选说明：可选参数。<br>参数含义：用于指示系统需要查询哪个节点的数据。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的容器引擎临时目录信息。 |

## 操作的配置对象

- [容器引擎临时目录（CNTTMPDIR）](configobject/UDG/20.15.2/CNTTMPDIR.md)

## 使用实例

1、查询所有节点配置信息：

```
%%DSP CNTTMPDIR:;%% 
RETCODE = 0  操作成功  
操作结果如下 
------------ 
节点IP           容器临时路径类型  详细信息    
10.0.0.0         DISK              成功       
10.0.0.1         DISK              成功       
10.0.0.2         DISK              成功      
(结果个数 = 3)  
---    END
```

2、查询 “节点IP” 为“10.0.0.0”的节点配置信息：

```
%%DSP CNTTMPDIR: NODEIP="10.0.0.0";%% 
RETCODE = 0  操作成功  
操作结果如下 
------------           
节点IP  =  10.0.0.0 
容器临时路径类型  =  DISK         
详细信息  =  成功 
(结果个数 = 1)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询容器引擎临时目录（DSP-CNTTMPDIR）_88993080.md`
