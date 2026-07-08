# 显示5G告警核查状态（DSP NGALMCHECK）

- [命令功能](#ZH-CN_MMLREF_0000001147491961__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001147491961__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001147491961__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001147491961__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001147491961__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001147491961)

**适用NF：AMF、SMF**

本命令用于查询系统当前的告警核查状态。

## [注意事项](#ZH-CN_MMLREF_0000001147491961)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001147491961)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001147491961)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “NGRAN_LINKDOWN（NG-RAN 链路故障）”：表示ALM-100058 NG-RAN 链路故障告警，对应的批量告警为ALM-100309 批量NG-RAN 链路故障。<br>- “NGRAN_UNREACH（NG-RAN 节点不可达）”：表示ALM-100059 NG-RAN 节点不可达告警，对应的批量告警为ALM-100310 批量NG-RAN 节点不可达。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>- “PFCP_LINKDOWN（PFCP链路故障）”：表示ALM-100056 PFCP链路故障告警，对应的批量告警为ALM-100452 批量PFCP链路故障。<br>- “PFCP_NODE_UNREACHABLE（PFCP对端节点不可达）”：表示ALM-100050 PFCP对端节点不可达告警，对应的批量告警为ALM-100453 批量PFCP对端节点不可达。<br>- “GTPC_TUNNEL_PATHBROKEN（GTPC路径故障）”：表示ALM-80610 GTPC路径故障告警，对应的批量告警为ALM-100590 批量GTPC路径故障。<br>默认值：SUMMARY<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001147491961)

查询告警核查：

```
%%DSP NGALMCHECK: ALMTYPE=NGRAN_LINKDOWN;%%
RETCODE = 0  操作成功

结果如下
--------
告警名称  =  NG-RAN 链路故障
核查类型  =  无
核查状态  =  空闲
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001147491961)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 告警名称 | 产生批量告警的原始告警的名称。<br>取值说明：<br>- “NGRAN_LINKDOWN（NG-RAN 链路故障）”：表示ALM-100058 NG-RAN 链路故障告警，对应的批量告警为ALM-100309 批量NG-RAN 链路故障。<br>- “NGRAN_UNREACH（NG-RAN 节点不可达）”：表示ALM-100059 NG-RAN 节点不可达告警，对应的批量告警为ALM-100310 批量NG-RAN 节点不可达。<br>- “PFCP_LINKDOWN（PFCP链路故障）”：表示ALM-100056 PFCP链路故障告警，对应的批量告警为ALM-100452 批量PFCP链路故障。<br>- “PFCP_NODE_UNREACHABLE（PFCP对端节点不可达）”：表示ALM-100050 PFCP对端节点不可达告警，对应的批量告警为ALM-100453 批量PFCP对端节点不可达。<br>- “GTPC_TUNNEL_PATHBROKEN（GTPC路径故障）”：表示ALM-80610 GTPC路径故障告警，对应的批量告警为ALM-100590 批量GTPC路径故障。 |
| 核查类型 | 该参数用于输出核查类型。<br>取值说明：<br>- “AUTO（自动）”：当前的核查是系统自动运行的。<br>- “MANUAL（手动）”：当前的核查是通过STR ALMCHECK命令触发的。<br>- “NO（无）”：当前没有核查任务。 |
| 核查状态 | 该参数用于输出核查状态。<br>取值说明：<br>- “CHECKING（正在核查）”：当前正在运行核查任务。<br>- “IDLE（空闲）”：当前没有核查任务。 |
