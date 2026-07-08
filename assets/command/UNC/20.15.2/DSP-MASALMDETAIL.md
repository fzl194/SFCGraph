---
id: UNC@20.15.2@MMLCommand@DSP MASALMDETAIL
type: MMLCommand
name: DSP MASALMDETAIL（显示5G告警详细信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MASALMDETAIL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
- 告警上报模式
status: active
---

# DSP MASALMDETAIL（显示5G告警详细信息）

## 功能

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
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTTP_LINKDOWN（HTTP链路故障）”：表示ALM-100155 HTTP链路故障告警，对应的批量告警为ALM-100311 批量HTTP链路故障。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>默认值：SUMMARY<br>配置原则：无 |
| SGT | 起始时间 | 可选必选说明：该参数在"ALMTYPE"配置为"HTTP_LINKDOWN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的产生时间的起始时间。<br>数据来源：本端规划<br>取值范围：DATE。<br>默认值：无<br>配置原则：无 |
| EGT | 结束时间 | 可选必选说明：该参数在"ALMTYPE"配置为"HTTP_LINKDOWN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的产生时间的结束时间。<br>数据来源：本端规划<br>取值范围：DATE。<br>默认值：无<br>配置原则：无 |
| MAXRECORD | 最大记录数 | 可选必选说明：该参数在"ALMTYPE"配置为"HTTP_LINKDOWN"时为条件可选参数。<br>参数含义：该参数用于指定待查询的告警的最大记录数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：1000<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MASALMDETAIL]] · 5G告警详细信息（MASALMDETAIL）

## 使用实例

- 查询系统中，批量告警的汇总信息：
  ```
  %%DSP MASALMDETAIL: ALMTYPE=SUMMARY;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  告警名称  =  HTTP链路故障
    告警ID  =  100311
  故障个数  =  100
  文件路径  =  /opt/container/log/5gcore/omb-pod/cell_omp/log/AlarmDetailRecord/CurrentBatchedHttpLinkDown.csv
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中，HTTP链路告警信息：
  ```
  %%DSP MASALMDETAIL: ALMTYPE=HTTP_LINKDOWN, SGT=2021&02&26, EGT=2021&02&26, MAXRECORD=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
        告警名称  =  HTTP链路故障
          告警ID  =  100155
        故障时间  =  2021-02-26 10:31:45+08:00
         POD名称  =  sbim-pod-5648469cd9-crczm
        进程标识  =  219
        链路集ID  =  1002
          链路ID  =  502
    对端NF实例ID  =  118
  对端NF描述名称  =  PCF_BJ_BJ_TOB_B001
      对端NF服务  =  PnfService
      本端NF类型  =  SMF
      本端IP地址  =  192.168.0.0
      对端IP地址  =  192.168.0.1
      本端端口号  =  0
        对端端口  =  33
        协议类型  =  TCP
        传输协议  =  HTTP
        告警原因  =  reason: link down reason 0x[0]
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MASALMDETAIL.md`
