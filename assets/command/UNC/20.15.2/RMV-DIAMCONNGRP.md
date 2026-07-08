---
id: UNC@20.15.2@MMLCommand@RMV DIAMCONNGRP
type: MMLCommand
name: RMV DIAMCONNGRP（删除Diameter链路组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DIAMCONNGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路组
status: active
---

# RMV DIAMCONNGRP（删除Diameter链路组）

## 功能

**适用NF：PGW-C、SMF**

![](删除Diameter链路组（RMV DIAMCONNGRP）_09897263.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除diameter链路组会导致相应Diameter链路中断，进而影响用户使用业务，比如用户被去活等。

该命令用于删除所有Diameter链路组配置信息，或者删除指定名称的Diameter链路组配置信息。

## 注意事项

- 该命令执行后立即生效。
- 当未指定Diameter链路组名时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 删除链路组会导致diamconnection被级联删除，在不存在其他有效链路组的情况下diameter消息相关的业务流程会处理失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DIAMCONNGRP]] · Diameter链路组（DIAMCONNGRP）

## 使用实例

如果希望删除diameter链路组gxconngrp下的所有链路，则可以删除对应的diameter链路组gxconngrp：

```
RMV DIAMCONNGRP:CONNGROUPNAME="gxconngrp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DIAMCONNGRP.md`
