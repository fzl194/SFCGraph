---
id: UNC@20.15.2@MMLCommand@SET PCCFLOWCONTROL
type: MMLCommand
name: SET PCCFLOWCONTROL（设置PCC流控配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCCFLOWCONTROL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC公共参数
status: active
---

# SET PCCFLOWCONTROL（设置PCC流控配置）

## 功能

**适用NF：PGW-C、SMF**

此命令用于配置UNC重授权请求的消息发送速率和SMF接收PCF的Npcf_SMPolicyControl_UpdateNotify消息的速率。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 大量用户在短时间内触发重授权请求上报可能造成PCRF过载。为了避免对端过载导致系统异常，通过此命令配置重授权请求的消息发送速率。
- 每个POD每秒发送请求消息的实际速率为“速率等级*速率系数/秒”。速率系数取决于POD内业务处理单元的个数。
- PCF在短时间内向SMF大量发送Npcf_SMPolicyControl_UpdateNotify消息可能导致SMF或SMF周边网元过载。为了避免过载导致系统异常，通过此命令配置SMF接收PCF的Npcf_SMPolicyControl_UpdateNotify消息的速率。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | REVALIDATRATE | UPDREQRATE | TEMREQRATE |
| --- | --- | --- | --- |
| 初始值 | 25 | 2000 | 2000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| REVALIDATRATE | Revalidation发送速率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置大量用户在短时间内触发重授权交互场景下每个进程每秒发送请求消息的速率等级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～100。<br>默认值：无<br>配置原则：无 |
| UPDREQRATE | UpdateNotify消息接收速率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF每个POD每秒接收PCF的Npcf_SMPolicyControl_UpdateNotify消息（指示更新）的数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无<br>配置原则：该参数配置为0时，表示取消对该消息的接入速率限制。 |
| TEMREQRATE | TerminateNotify消息接收速率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMF每个POD每秒接收PCF的Npcf_SMPolicyControl_UpdateNotify消息（指示删除）的数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无<br>配置原则：该参数配置为0时，表示取消对该消息的接入速率限制。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCFLOWCONTROL]] · PCC流控配置（PCCFLOWCONTROL）

## 使用实例

配置revalidation消息发送速率等级为10，UpdateNotify接收速率为2000，TerminateNotify接收速率为2000：

```
SET PCCFLOWCONTROL: REVALIDATRATE=10, UPDREQRATE=2000, TEMREQRATE=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PCC流控配置（SET-PCCFLOWCONTROL）_09897059.md`
