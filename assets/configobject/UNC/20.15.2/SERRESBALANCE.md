---
id: UNC@20.15.2@ConfigObject@SERRESBALANCE
type: ConfigObject
name: SERRESBALANCE（业务资源均衡操作）
nf: UNC
version: 20.15.2
object_name: SERRESBALANCE
object_kind: action
applicable_nf:
- SGSN
- MME
status: active
---

# SERRESBALANCE（业务资源均衡操作）

## 说明

![](启动业务资源均衡操作(STR SERRESBALANCE)_72345965.assets/notice_3.0-zh-cn_2.png)

资源均衡过程中可能会影响现有业务，建议在业务低峰时执行此命令。

**适用网元：SGSN、MME**

1. 此命令用于手动启动系统内资源均衡。
2. 系统扩容、减容或出现进程或节点故障场景时，可能出现系统资源在进程或节点之间部署不均。
3. RM_TYPE_USER、RM_TYPE_S1ECMCONN、RM_TYPE_S1UCMCONN、RM_TYPE_GTPUPDP、RM_TYPE_GBCELL、RM_TYPE_GBUSER、RM_TYPE_IUUSRCONN、RM_TYPE_NGAPLNK这几类资源在执行此命令后，不能保证进程间完全均衡，各个进程间上下文差值占进程上下文规格的比例小于10%。其他资源在执行此命令后，能保证各个进程间上下文分布均衡。
4. 资源部署不均衡对进程的影响:
    - RM_TYPE_DMLNK(Diameter链路)、RM_TYPE_M3UALNK(M3UA链路)、RM_TYPE_SGSVLRLNK(SGS链路)、RM_TYPE_DNSCONN(DNS本端端点)、RM_TYPE_S1ECMCONN（S1链路）、RM_TYPE_S1UCMCONN（S1连接）、RM_TYPE_IUUSRCONN(IU连接)、RM_TYPE_NGAPLNK（N2链路）这些资源部署在SGP进程上，这些资源部署不均衡可能导致SGP CPU开销不均。
    - RM_TYPE_GBCELL(2G小区)、RM_TYPE_NSE(NSE)、RM_TYPE_GBUSER(GB用户上下文)这些资源部署在GBP进程上，这些资源部署不均衡可能导致GBP CPU开销不均。
    - RM_TYPE_GTPCPATH(GTPC本端端点)、RM_TYPE_GTPUPATH(GTPU本端端点)、RM_TYPE_GTPUPDP(用户面PDP上下文)这些资源部署在UPP进程上，这些资源不均衡可能导致UPP CPU开销不均。
    - RM_TYPE_USER(用户和承载上下文)这个资源部署在SPP进程上，这个资源不均衡可能导致SPP CPU开销不均。

## 操作本对象的命令

- [[command/UNC/20.15.2/STR-SERRESBALANCE]] · STR SERRESBALANCE

## 证据

- 原始手册：`evidence/UNC/20.15.2/启动业务资源均衡操作(STR-SERRESBALANCE)_72345965.md`
