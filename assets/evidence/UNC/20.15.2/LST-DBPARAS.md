# 查询配置的DB参数（LST DBPARAS）

- [命令功能](#ZH-CN_MMLREF_0000001144040875__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001144040875__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001144040875__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001144040875__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001144040875__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001144040875)

该命令用于查询配置的DB参数。

## [注意事项](#ZH-CN_MMLREF_0000001144040875)

参数PARANAME取值为SdbCompressSwitch、SdbCompressMsgSize或SdbCompressAlgorithm时，其对应的PARAVALUE取值若通过SET DBPARAS命令完成了配置，则可通过本命令查询具体取值，若未经过配置，其系统初始值仅能通过OPR DBGDATA: DBGTYPE=CELLTYPE, CELLTYPE=*, DEBUGNAME="DDF DSP PLUGIN WHERE DATABASETYPE IS sdb";命令进行查询，其中CELLTYPE的取值为进程类型。

#### [操作用户权限](#ZH-CN_MMLREF_0000001144040875)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001144040875)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARANAME | 参数名称 | 可选必选说明：可选参数<br>参数含义：参数名称。<br>数据来源：本端规划<br>取值范围：<br>- SdbBatchDuration（打包发送时间间隔（毫秒））<br>- SdbBatchMaxQueueLen（打包发送最大队列长度）<br>- SdbMultiOpMaxSize（单个数据包最大尺寸（字节））<br>- DdbSrvVerifyCycle（业务DDB服务端核查周期）<br>- DdbSfSrvVerifyCycle（平台DDB服务端核查周期）<br>- DdbClientVerifyCycle（业务DDB客户端核查周期）<br>- DdbSfClientVerifyCycle（平台DDB客户端核查周期）<br>- DdbSrvVerifyTimer（业务DDB服务端核查定时器周期（ms））<br>- DdbSfSrvVerifyTimer（平台DDB服务端核查定时器周期（ms））<br>- DdbClientVerifyTimer（业务DDB客户端核查定时器周期（ms））<br>- DdbSfClientVerifyTimer（平台DDB客户端核查定时器周期（ms））<br>- DdbSfSrvAllowWindowPush（平台DDB服务端允许窗口推送）<br>- DdbSrvAllowWindowPush（业务DDB服务端允许窗口推送）<br>- DdbSfSrvWindowSize（平台DDB服务端窗口大小）<br>- DdbSrvWindowSize（业务DDB服务端窗口大小）<br>- SdbMaxScanRate（SDB最大扫描速率）<br>- SdbTableRecordThreshold（SDB表记录阈值）<br>- SdbMaxSubmitLen（SDB表记录最大提交长度（KB））<br>- SdbCompressSwitch（SDB带宽压缩开关）<br>- SdbCompressMsgSize（SDB带宽压缩大小）<br>- SdbCompressAlgorithm（SDB带宽压缩算法）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001144040875)

查询配置的SDB打包参数

```
LST DBPARAS: PARANAME=SdbBatchDuration;
```

## [输出结果说明](#ZH-CN_MMLREF_0000001144040875)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 参数名称 | 参数名称。 |
| 参数值 | 参数值。 |
