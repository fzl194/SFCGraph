---
id: UNC@20.15.2@MMLCommand@LCK M3LNK
type: MMLCommand
name: LCK M3LNK（锁定M3UA信令链路）
nf: UNC
version: 20.15.2
verb: LCK
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

# LCK M3LNK（锁定M3UA信令链路）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于锁定M3UA信令链路。该命令不会引起链路状态变化，不影响业务。M3UA链路状态有四种，分别为：“SCTP偶联未建立”、“SCTP偶联建立”、“未激活”和“激活”。链路锁定后，链路状态仅能进行如下情况的变化：

- “SCTP偶联未建立”到“SCTP偶联建立”
- “SCTP偶联建立”到“SCTP偶联未建立”
- “未激活”到“SCTP偶联未建立”
- “未激活”到“SCTP偶联建立”
- “激活”到“SCTP偶联未建立”
- “激活”到“SCTP偶联建立”
- “激活”到“未激活”

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

- [[configobject/UNC/20.15.2/M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

锁定链路号为1的M3UA链路：

LCK M3LNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/锁定M3UA信令链路（LCK-M3LNK）_72225987.md`
