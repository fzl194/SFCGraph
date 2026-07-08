---
id: UNC@20.15.2@MMLCommand@LST CHRLOWPERFSVRSUB
type: MMLCommand
name: LST CHRLOWPERFSVRSUB（查询低性能CHR服务器的单据订阅条件）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHRLOWPERFSVRSUB
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 低性能CHR服务器的单据订阅条件
status: active
---

# LST CHRLOWPERFSVRSUB（查询低性能CHR服务器的单据订阅条件）

## 功能

**适用网元：SGSN、MME**

该命令用于进行CHR单据上报时，在 UNC 查询指定CloudUDN或全部CloudUDN的CHR单据订阅条件。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHRLOWPERFSVRSUB]] · 低性能CHR服务器的单据订阅条件（CHRLOWPERFSVRSUB）

## 使用实例

查询低性能CloudUDN的单据订阅条件：

LST CHRLOWPERFSVRSUB:;

```
%%LST CHRLOWPERFSVRSUB:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
Gb模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & Inter System Change & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & Suspend & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14 & RESERVED15
Gb模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & Inter System Change & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & Suspend & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14 & RESERVED15
Iu模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & SRNS Relocation & Inter System Change & IU Release & Service Request & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & RAB Assignment in Service Request & Suspend & Location Report & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14
Iu模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Routing Area Update & SRNS Relocation & Inter System Change & IU Release & Service Request & PDP Context Activation & PDP Context Deactivation & PDP Context Modification & Paging & RAB Assignment in Service Request & Suspend & Location Report & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6 & RESERVED7 & RESERVED8 & RESERVED9 & RESERVED10 & RESERVED11 & RESERVED12 & RESERVED13 & RESERVED14
S1模式流程成功时上报选项  =  Other Procedure & Attach & Detach & Tracking Area Update & Inter System Change & S1 Handover & X2 Handover & Service Request & Paging & S1 Release & UE Requested PDN Connectivity & UE or MME Requested PDN Disconnection & Dedicated Bearer Activation & Bearer Modification & Dedicated Bearer Deactivation & SGS Paging & SRVCC & Location Report & Control Plane Service Request & P-GW-initiated PDN Disconnect & Connection Suspend & Connection Resume & Reroute NAS & E-RAB Modification Indication & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6
S1模式流程失败时上报选项  =  Other Procedure & Attach & Detach & Tracking Area Update & Inter System Change & S1 Handover & X2 Handover & Service Request & Paging & S1 Release & UE Requested PDN Connectivity & UE or MME Requested PDN Disconnection & Dedicated Bearer Activation & Bearer Modification & Dedicated Bearer Deactivation & SGS Paging & SRVCC & Location Report & Control Plane Service Request & P-GW-initiated PDN Disconnect & VoLTE Bearer Deleted Unexpectedly & Connection Suspend & Connection Resume & Reroute NAS & E-RAB Modification Indication & Cancel Location & RESERVED1 & RESERVED2 & RESERVED3 & RESERVED4 & RESERVED5 & RESERVED6
      冲突流程时上报选项  =  LTE UE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHRLOWPERFSVRSUB.md`
