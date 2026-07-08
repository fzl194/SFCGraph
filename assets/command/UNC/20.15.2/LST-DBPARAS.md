---
id: UNC@20.15.2@MMLCommand@LST DBPARAS
type: MMLCommand
name: LST DBPARAS（查询配置的DB参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DBPARAS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 数据服务功能管理
- 参数管理
status: active
---

# LST DBPARAS（查询配置的DB参数）

## 功能

该命令用于查询配置的DB参数。

## 注意事项

参数PARANAME取值为SdbCompressSwitch、SdbCompressMsgSize或SdbCompressAlgorithm时，其对应的PARAVALUE取值若通过SET DBPARAS命令完成了配置，则可通过本命令查询具体取值，若未经过配置，其系统初始值仅能通过OPR DBGDATA: DBGTYPE=CELLTYPE, CELLTYPE=*, DEBUGNAME="DDF DSP PLUGIN WHERE DATABASETYPE IS sdb";命令进行查询，其中CELLTYPE的取值为进程类型。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARANAME | 参数名称 | 可选必选说明：可选参数<br>参数含义：参数名称。<br>数据来源：本端规划<br>取值范围：<br>- SdbBatchDuration（打包发送时间间隔（毫秒））<br>- SdbBatchMaxQueueLen（打包发送最大队列长度）<br>- SdbMultiOpMaxSize（单个数据包最大尺寸（字节））<br>- DdbSrvVerifyCycle（业务DDB服务端核查周期）<br>- DdbSfSrvVerifyCycle（平台DDB服务端核查周期）<br>- DdbClientVerifyCycle（业务DDB客户端核查周期）<br>- DdbSfClientVerifyCycle（平台DDB客户端核查周期）<br>- DdbSrvVerifyTimer（业务DDB服务端核查定时器周期（ms））<br>- DdbSfSrvVerifyTimer（平台DDB服务端核查定时器周期（ms））<br>- DdbClientVerifyTimer（业务DDB客户端核查定时器周期（ms））<br>- DdbSfClientVerifyTimer（平台DDB客户端核查定时器周期（ms））<br>- DdbSfSrvAllowWindowPush（平台DDB服务端允许窗口推送）<br>- DdbSrvAllowWindowPush（业务DDB服务端允许窗口推送）<br>- DdbSfSrvWindowSize（平台DDB服务端窗口大小）<br>- DdbSrvWindowSize（业务DDB服务端窗口大小）<br>- SdbMaxScanRate（SDB最大扫描速率）<br>- SdbTableRecordThreshold（SDB表记录阈值）<br>- SdbMaxSubmitLen（SDB表记录最大提交长度（KB））<br>- SdbCompressSwitch（SDB带宽压缩开关）<br>- SdbCompressMsgSize（SDB带宽压缩大小）<br>- SdbCompressAlgorithm（SDB带宽压缩算法）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DBPARAS]] · 配置的DB参数（DBPARAS）

## 使用实例

查询配置的SDB打包参数

```
LST DBPARAS: PARANAME=SdbBatchDuration;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询配置的DB参数（LST-DBPARAS）_44040875.md`
