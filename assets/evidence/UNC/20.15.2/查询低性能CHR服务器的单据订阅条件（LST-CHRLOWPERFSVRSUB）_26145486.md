# 查询低性能CHR服务器的单据订阅条件（LST CHRLOWPERFSVRSUB）

- [命令功能](#ZH-CN_MMLREF_0000001126145486__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145486__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145486__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145486__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145486__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145486__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145486__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145486)

**适用网元：SGSN、MME**

该命令用于进行CHR单据上报时，在 UNC 查询指定CloudUDN或全部CloudUDN的CHR单据订阅条件。

#### [注意事项](#ZH-CN_MMLREF_0000001126145486)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145486)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145486)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145486)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126145486)

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

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145486)

请参见 [**SET CHRLOWPERFSVRSUB**](设置低性能CHR服务器的单据订阅条件（SET CHRLOWPERFSVRSUB）_72345083.md) 的参数说明。
