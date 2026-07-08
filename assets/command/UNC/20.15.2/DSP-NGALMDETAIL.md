---
id: UNC@20.15.2@MMLCommand@DSP NGALMDETAIL
type: MMLCommand
name: DSP NGALMDETAIL（显示5G告警详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGALMDETAIL
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

# DSP NGALMDETAIL（显示5G告警详细信息）

## 功能

**适用NF：AMF、SMF**

该命令用于显示批量告警包含的详细故障信息。

## 注意事项

- 当“告警类型”选择为特定告警时，系统内可能存在许多原始告警，导致该命令返回时间过长，可通过在命令中限定“起始时间”和“结束时间”来减少查询记录数。
- 由于批量告警是在原始告警产生后按照一定周期合并的结果，所以原始告警的实际故障时间早于批量告警的产生时间。
- 如果批量告警进行了刷新，原始告警和批量告警的时间可能相差很多，因此当根据某条批量告警产生时间作为查询条件时，建议将“批量告警产生时间”作为本命令的“结束时间”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “NGRAN_LINKDOWN（NG-RAN 链路故障）”：表示ALM-100058 NG-RAN 链路故障告警，对应的批量告警为ALM-100309 批量NG-RAN 链路故障。<br>- “NGRAN_UNREACH（NG-RAN 节点不可达）”：表示ALM-100059 NG-RAN 节点不可达告警，对应的批量告警为ALM-100310 批量NG-RAN 节点不可达。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>- “PFCP_LINKDOWN（PFCP链路故障）”：表示ALM-100056 PFCP链路故障告警，对应的批量告警为ALM-100452 批量PFCP链路故障。<br>- “PFCP_NODE_UNREACHABLE（PFCP对端节点不可达）”：表示ALM-100050 PFCP对端节点不可达告警，对应的批量告警为ALM-100453 批量PFCP对端节点不可达。<br>- “GTPC_TUNNEL_PATHBROKEN（GTPC路径故障）”：表示ALM-80610 GTPC路径故障告警，对应的批量告警为ALM-100590 批量GTPC路径故障。<br>默认值：SUMMARY<br>配置原则：无 |
| SGT | 起始时间 | 可选必选说明：该参数在"ALMTYPE"配置为"NGRAN_LINKDOWN"、"NGRAN_UNREACH"、"PFCP_LINKDOWN"、"PFCP_NODE_UNREACHABLE"、"GTPC_TUNNEL_PATHBROKEN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的产生时间的起始时间。<br>数据来源：本端规划<br>取值范围：DATE。<br>默认值：无<br>配置原则：无 |
| EGT | 结束时间 | 可选必选说明：该参数在"ALMTYPE"配置为"NGRAN_LINKDOWN"、"NGRAN_UNREACH"、"PFCP_LINKDOWN"、"PFCP_NODE_UNREACHABLE"、"GTPC_TUNNEL_PATHBROKEN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的产生时间的结束时间。<br>数据来源：本端规划<br>取值范围：DATE。<br>默认值：无<br>配置原则：无 |
| MAXRECORD | 最大记录数 | 可选必选说明：该参数在"ALMTYPE"配置为"NGRAN_LINKDOWN"、"NGRAN_UNREACH"、"PFCP_LINKDOWN"、"PFCP_NODE_UNREACHABLE"、"GTPC_TUNNEL_PATHBROKEN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的最大记录数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：1000<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGALMDETAIL]] · 5G告警详细信息（NGALMDETAIL）

## 使用实例

- 查询系统中，批量告警的汇总信息：
  ```
  %%DSP NGALMDETAIL: ALMTYPE=SUMMARY;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  告警名称                告警ID   故障个数      文件路径                                                                         

  NG-RAN 链路故障         100309    100        xxx/AlarmDetailRecord/CurrentBatchedNgRanLinkDown.csv
  NG-RAN 节点不可达	100310    100        xxx/AlarmDetailRecord/CurrentBatchedNgRanUnreachable.csv
  (结果个数 = 2)

  ---    END
  ```
- 查询系统中，NG-RAN链路告警信息：
  ```
  %%DSP NGALMDETAIL: ALMTYPE=NGRAN_LINKDOWN, SGT=2021&02&26, EGT=2021&02&26, MAXRECORD=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        告警名称  =  NG-RAN 链路故障
          告警ID  =  100058
        故障时间  =  2021-02-26 10:31:45+08:00
         POD名称  =  usn-pod-5648469cd9-crczm
      移动国家码  =  0
        移动网号  =  0
         S-NSSAI  =  0
  NG-RAN节点类型  =  AMF
  NG-RAN节点标识  =  1927
  NG-RAN节点名称  =  am_10113
     本端IP地址1  =  192.168.0.0
     本端IP地址2  =  192.168.0.1
      本端端口号  =  33
  NG-RAN IP地址1  =  192.168.0.2
  NG-RAN IP地址2  =  192.168.0.3
    NG-RAN端口号  =  22
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGALMDETAIL.md`
