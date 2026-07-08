---
id: UNC@20.15.2@MMLCommand@RMV M3LNK
type: MMLCommand
name: RMV M3LNK（删除M3UA信令链路）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M3LNK
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA链路
status: active
---

# RMV M3LNK（删除M3UA信令链路）

## 功能

![](删除M3UA信令链路(RMV M3LNK)_26306116.assets/notice_3.0-zh-cn_2.png)

删除链路可能影响正在进行的业务。

**适用网元：SGSN、MME、SMSF**

该命令用于删除M3UA信令链路。当删除到对端的最后一条链路时，对应的业务将受损。

## 注意事项

- 该命令执行后立即生效。
- 该命令在版本升级过程中禁止执行。
- 删除链路可能影响正在进行的业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M3UA链路号。该参数用来在系统范围内部唯一标识一条M3UA链路。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

删除链路号为0的M3UA链路：

RMV M3LNK: LNK=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-M3LNK.md`
