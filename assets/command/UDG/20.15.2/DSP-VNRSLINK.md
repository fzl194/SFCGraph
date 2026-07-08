---
id: UDG@20.15.2@MMLCommand@DSP VNRSLINK
type: MMLCommand
name: DSP VNRSLINK（查询VNRS链路）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VNRSLINK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 系统管理
- 链路管理
- VNRS链路
status: active
---

# DSP VNRSLINK（查询VNRS链路）

## 功能

该命令用于查询到VNRS的链路信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU的名称，通过<br>**[LST SERVICERUSTATE](../../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>获得。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0 ~ 63位字符串 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程类型。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “PROC_TYPE_MNCP(PROC_MNCP) ” |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程号。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~63 |
| LINKINDEX | 链路索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示链路索引。<br>数据来源：本端规划<br>默认值：无<br>取值范围：0~127 |
| LINKSTATUS | 链路状态 | 可选必选说明：可选参数<br>参数含义：该参数用于表示链路状态。<br>数据来源：本端规划<br>默认值：无<br>取值范围：<br>- “LINK NOTCONNECTED(未连接) ”<br>- “LINK NORMAL(正常) ” |

## 操作的配置对象

- [[configobject/UDG/20.15.2/VNRSLINK]] · VNRS链路（VNRSLINK）

## 使用实例

查询所有VNRS链路信息：

DSP VNRSLINK:;

```
%%DSP VNRSLINK:;%%
RETCODE = 0  操作成功
结果如下:
-------------------------
      RU名称  =  CSLB_IP_RU2_0068
    进程类型  =  PROC_MNCP
      进程号  =  1
    链路索引  =  0
      IP类型  =  IPV4
 本端VNFC ID  =  3
本端IPv4地址  =  172.17.2.25
本端IPv6地址  =  ::
  本端端口号  =  53277
 对端VNFC ID  =  1
对端IPv4地址  =  172.17.0.2
对端IPv6地址  =  ::
  对端端口号  =  3868
    链路状态  =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询VNRS链路（DSP-VNRSLINK）_29627098.md`
