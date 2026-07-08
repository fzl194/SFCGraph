---
id: UDG@20.15.2@ConfigObject@TLBGLBCONF
type: ConfigObject
name: TLBGLBCONF（TLB全局配置）
nf: UDG
version: 20.15.2
object_name: TLBGLBCONF
object_kind: global_setting
status: active
---

# TLBGLBCONF（TLB全局配置）

## 说明

![](设置TLB全局配置（SET TLBGLBCONF）_69954926.assets/notice_3.0-zh-cn.png)

该命令中TLBGLBSW参数用于设置TLB全局功能开关，开启TLB功能后会改变内部处理TCP SYN包的流程，影响建链性能。

用于设置HTTP服务端TCP链路整系统负载均衡（TLB）的功能开关及相关参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 此命令中的TLBGLBSW开关配置与HTTPSRVLBSW（HTTP服务端负载均衡功能开关）中的LBFUNSWITCH开关不能同时打开，若期望打开TLB开关则请先执行[**LST HTTPSRVLBSW**](../../POD内负载管理/查询HTTP服务端负载重均衡功能（LST HTTPSRVLBSW）_29053331.md)命令确认LBFUNSWITCH配置为OFF。
> - 适用场景：1、当服务端链路在HTTP进程上分布不均匀导致HTTP进程CPU不均匀问题时，可以通过打开TLB开关解决，以避免达到性能瓶颈而不满足服务规格。2、当不同对端IP间的链路流量不均匀，同一对端IP下的链路流量均匀时，需要打开TLB开关后并重建服务端链路以解决HTTP进程CPU不均匀问题。3、当同一对端IP下的链路流量也不均匀时，无法通过开启TLB开关解决HTTP进程CPU不均匀问题。
> - 操作风险：1、打开TLB开关后会引起可靠性的弱化。SBILINK、LBC或SDRC主实例复位期间若TLB开关处于打开状态，将导致无法新建服务端链路，如果此时服务端链路发生异常断链，会导致业务受损。2、TLB五元组策略系统规格为80000，TLBGLBSW开关开启后最多可能占用80000个CSLB策略资源。CSLB在mini模板配置下策略资源规格为100000，normal模板配置下策略资源规格为200000。[**DSP POLICYNUM**](../../../../../CSLB功能管理/业务管理/服务管理/策略/查询策略数量（DSP POLICYNUM）_29627053.md)命令可以查询策略资源的已占用情况，[**DSP DBGSTAT**](../../../../../CSLB功能管理/操作维护/系统调测/公共调测/调试信息/查询调试信息（DSP DBGSTAT）_29627109.md)命令可以查询策略资源的预申请情况。当策略资源占用满时，无法下发CSLB策略，导致系统异常，业务受损。开启TLBGLBSW开关前需要排查系统是否存在“ALM-82420 CSLB负载均衡资源使用率超过阈值”告警，并通过上述命令评估策略资源占用是否有可能超过CSLB策略资源规格，如有此类情况，不允许打开TLBGLBSW开关。无法准确评估时，请联系华为技术支持。
> - 不支持NP场景。当前NP场景下打开TLB开关会导致业务受损。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TLBGLBSW | LBTYPE | RELBDEVTHD | RELBMINLINK | RELBMINITR | TLBRCVSYNTHD | RPTDTSYNTHD | TMPPLYPERIOD | TUPLECHKSW | TUPLECHKPRD | TUPLEAGETHD | TLBTBETHD | TLBHALTTHD | TLBRESTORETHD | SYNSENDDELAY |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | OFF | LINKNUMCTRL | 10 | 5 | 30 | 2000 | 200 | 5 | ON | 30 | 5 | 1000 | 95 | 85 | 20 |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-TLBGLBCONF]] · LST TLBGLBCONF
- [[command/UDG/20.15.2/SET-TLBGLBCONF]] · SET TLBGLBCONF

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询TLB全局配置（LST-TLBGLBCONF）_15834601.md`
- 原始手册：`evidence/UDG/20.15.2/设置TLB全局配置（SET-TLBGLBCONF）_69954926.md`
