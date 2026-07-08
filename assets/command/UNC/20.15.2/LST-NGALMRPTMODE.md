---
id: UNC@20.15.2@MMLCommand@LST NGALMRPTMODE
type: MMLCommand
name: LST NGALMRPTMODE（查询5G告警上报模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGALMRPTMODE
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 告警管理
- 告警上报模式
status: active
---

# LST NGALMRPTMODE（查询5G告警上报模式）

## 功能

**适用NF：AMF、SMF**

该命令用于查询5G告警上报模式及相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “NGRAN_LINKDOWN（NG-RAN 链路故障）”：表示ALM-100058 NG-RAN 链路故障告警，对应的批量告警为ALM-100309 批量NG-RAN 链路故障。<br>- “NGRAN_UNREACH（NG-RAN 节点不可达）”：表示ALM-100059 NG-RAN 节点不可达告警，对应的批量告警为ALM-100310 批量NG-RAN 节点不可达。<br>- “HTTP_LINKDOWN（HTTP链路故障）”：该枚举值已废弃，可以通过SET MASALMRPTMODE命令设置HTTP链路故障告警上报模式。<br>- “PFCP_LINKDOWN（批量PFCP链路故障）”：表示ALM-100056 PFCP链路故障告警，对应的批量告警为ALM-100452 批量PFCP链路故障。<br>- “PFCP_NODE_UNREACHABLE（批量PFCP对端节点不可达）”：表示ALM-100050 PFCP对端节点不可达告警，对应的批量告警为ALM-100453 批量PFCP对端节点不可达。<br>- “GTPC_TUNNEL_PATHBROKEN（批量GTPC路径故障）”：表示ALM-80610 GTPC路径故障告警，对应的批量告警为ALM-100590 批量GTPC路径故障。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGALMRPTMODE]] · 5G告警上报模式（NGALMRPTMODE）

## 使用实例

查询系统中，ALM-100058 NG-RAN 链路故障的告警上报模式：

```
%%LST NGALMRPTMODE: ALMTYPE=NGRAN_LINKDOWN;%%
RETCODE = 0  操作成功

结果如下
------------------------
         告警类型  =  NG-RAN 链路故障
  批量告警上报开关  =  开
  批量告警上报开关  =  60
  批量告警上报开关  =  100
  批量告警上报开关  =  10
批量恢复百分比(%)  =  56
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGALMRPTMODE.md`
