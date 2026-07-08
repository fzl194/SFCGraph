---
id: UNC@20.15.2@MMLCommand@ULK M3LNK
type: MMLCommand
name: ULK M3LNK（解锁M3UA信令链路）
nf: UNC
version: 20.15.2
verb: ULK
object_keyword: M3LNK
command_category: 动作类
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

# ULK M3LNK（解锁M3UA信令链路）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于解锁M3UA信令链路。解锁后链路变回原来的实际状态，对业务无影响。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能在SG端或者IPSP的服务器端操作。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M3UA链路号。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

解锁链路号为1的M3UA链路：

ULK M3LNK:LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ULK-M3LNK.md`
