---
id: UNC@20.15.2@MMLCommand@REL M3LNK
type: MMLCommand
name: REL M3LNK（释放M3UA信令链路）
nf: UNC
version: 20.15.2
verb: REL
object_keyword: M3LNK
command_category: 调测类
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

# REL M3LNK（释放M3UA信令链路）

## 功能

![](释放M3UA信令链路(REL M3LNK)_26306120.assets/notice_3.0-zh-cn_2.png)

释放链路将会导致该链路无法进行业务。

**适用网元：SGSN、MME、SMSF**

该命令用于释放M3UA信令链路。

## 注意事项

- 该命令执行后，链路变为“SCTP偶联未建立”状态。
- 该命令只有在执行[**ADD M3LNK**](增加M3UA信令链路(ADD M3LNK)_72225983.md)命令时配置的参数“C/S模式”为“C(客户端模式)”的情形下才能执行。
- 建议使用优雅方式释放链路，避免数据丢失。
- 该命令执行后立即生效。
- 释放链路将会导致该链路无法进行业务。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M3UA链路号。<br>取值范围：0~1279<br>默认值：无 |
| RELASE_MODE | 释放方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定链路释放模式。<br>取值范围：<br>- “GR（GRACEFUL）”<br>- “UNGR（UNGRACEFUL）”<br>默认值：无<br>说明：GR（优雅），通常不会导致数据丢失。释放链路之前必须先去激活此链路，使链路从“激活”状态进入“非激活”状态；此时对该链路优雅释放，链路从“非激活”状态先进入“DOWN”状态，再进入“SCTP偶联未建立”状态；UNGR（非优雅），通常会导致数据丢失。M3UA链路从“激活”状态直接进入“SCTP偶联未建立”状态。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LNK]] · M3UA信令链路（M3LNK）

## 使用实例

以优雅方式释放链路号为1的M3UA链路：

REL M3LNK: LNK=1, RELASE_MODE=GR;

## 证据

- 原始手册：`evidence/UNC/20.15.2/REL-M3LNK.md`
