---
id: UNC@20.15.2@MMLCommand@DSP NGALMCHECK
type: MMLCommand
name: DSP NGALMCHECK（显示5G告警核查状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGALMCHECK
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 告警管理
- 告警核查
status: active
---

# DSP NGALMCHECK（显示5G告警核查状态）

## 功能

**适用NF：AMF、SMF**

本命令用于查询系统当前的告警核查状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “NGRAN_LINKDOWN（NG-RAN 链路故障）”：表示ALM-100058 NG-RAN 链路故障告警，对应的批量告警为ALM-100309 批量NG-RAN 链路故障。<br>- “NGRAN_UNREACH（NG-RAN 节点不可达）”：表示ALM-100059 NG-RAN 节点不可达告警，对应的批量告警为ALM-100310 批量NG-RAN 节点不可达。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>- “PFCP_LINKDOWN（PFCP链路故障）”：表示ALM-100056 PFCP链路故障告警，对应的批量告警为ALM-100452 批量PFCP链路故障。<br>- “PFCP_NODE_UNREACHABLE（PFCP对端节点不可达）”：表示ALM-100050 PFCP对端节点不可达告警，对应的批量告警为ALM-100453 批量PFCP对端节点不可达。<br>- “GTPC_TUNNEL_PATHBROKEN（GTPC路径故障）”：表示ALM-80610 GTPC路径故障告警，对应的批量告警为ALM-100590 批量GTPC路径故障。<br>默认值：SUMMARY<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGALMCHECK]] · 5G告警核查（NGALMCHECK）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGALMCHECK.md`
