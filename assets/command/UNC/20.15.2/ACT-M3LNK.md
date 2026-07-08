---
id: UNC@20.15.2@MMLCommand@ACT M3LNK
type: MMLCommand
name: ACT M3LNK（激活M3UA信令链路）
nf: UNC
version: 20.15.2
verb: ACT
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

# ACT M3LNK（激活M3UA信令链路）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于激活M3UA信令链路，M3UA链路激活成功后将恢复承载业务。

- 该命令执行后，如果链路没有建立成功，M3UA则会自动重复建立链路的过程。
- 如果链路处于“SCTP偶联未建立”状态、“DOWN”状态或者“非激活”状态，执行该命令后，链路直接进入“激活”态。

## 注意事项

- 激活被锁定的M3UA链路时，需要先对其进行解锁操作（[**ULK M3LNK**](解锁M3UA信令链路（ULK M3LNK）_72345909.md)）。
- 该命令只能在AS端或者IPSP的客户端操作。
- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M3UA链路号。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

激活链路号为1的M3UA链路：

ACT M3LNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-M3LNK.md`
