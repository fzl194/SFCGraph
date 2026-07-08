---
id: UNC@20.15.2@MMLCommand@SET DBPARAS
type: MMLCommand
name: SET DBPARAS（设置DB参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DBPARAS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 数据服务功能管理
- 参数管理
status: active
---

# SET DBPARAS（设置DB参数）

## 功能

该命令用于设置DB参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PARANAME | PARAVALUE |
| --- | --- |
| SdbBatchDuration | 1000 |
| SdbBatchMaxQueueLen | 20 |
| SdbMultiOpMaxSize | 10000 |
| DdbSrvVerifyCycle | 6000 |
| DdbSfSrvVerifyCycle | 6000 |
| DdbClientVerifyCycle | 6000 |
| DdbSfClientVerifyCycle | 6000 |
| DdbSrvVerifyTimer | 200 |
| DdbSfSrvVerifyTimer | 200 |
| DdbClientVerifyTimer | 200 |
| DdbSfClientVerifyTimer | 200 |
| DdbSfSrvAllowWindowPush | true |
| DdbSrvAllowWindowPush | true |
| DdbSfSrvWindowSize | 10 |
| DdbSrvWindowSize | 10 |
| SdbMaxScanRate | 0 |
| SdbTableRecordThreshold | 110 |
| SdbMaxSubmitLen | 96 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARANAME | 参数名称 | 可选必选说明：必选参数<br>参数含义：参数名称。<br>数据来源：本端规划<br>取值范围：<br>- SdbBatchDuration（打包发送时间间隔（毫秒））<br>- SdbBatchMaxQueueLen（打包发送最大队列长度）<br>- SdbMultiOpMaxSize（单个数据包最大尺寸（字节））<br>- DdbSrvVerifyCycle（业务DDB服务端核查周期）<br>- DdbSfSrvVerifyCycle（平台DDB服务端核查周期）<br>- DdbClientVerifyCycle（业务DDB客户端核查周期）<br>- DdbSfClientVerifyCycle（平台DDB客户端核查周期）<br>- DdbSrvVerifyTimer（业务DDB服务端核查定时器周期（ms））<br>- DdbSfSrvVerifyTimer（平台DDB服务端核查定时器周期（ms））<br>- DdbClientVerifyTimer（业务DDB客户端核查定时器周期（ms））<br>- DdbSfClientVerifyTimer（平台DDB客户端核查定时器周期（ms））<br>- DdbSfSrvAllowWindowPush（平台DDB服务端允许窗口推送）<br>- DdbSrvAllowWindowPush（业务DDB服务端允许窗口推送）<br>- DdbSfSrvWindowSize（平台DDB服务端窗口大小）<br>- DdbSrvWindowSize（业务DDB服务端窗口大小）<br>- SdbMaxScanRate（SDB最大扫描速率）<br>- SdbTableRecordThreshold（SDB表记录阈值）<br>- SdbMaxSubmitLen（SDB表记录最大提交长度（KB））<br>- SdbCompressSwitch（SDB带宽压缩开关）<br>- SdbCompressMsgSize（SDB带宽压缩大小）<br>- SdbCompressAlgorithm（SDB带宽压缩算法）<br>默认值：无。<br>配置原则：无 |
| PARAVALUE | 参数值 | 可选必选说明：必选参数<br>参数含义：参数值。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无。<br>配置原则：<br>当参数类型取值为"SdbCompressSwitch"， 取值范围为"0"或"2"。当参数类型取值为"SdbCompressMsgSize"， 取值范围为"0~1048576"。当参数类型取值为"SdbCompressAlgorithm"， 取值范围为"0~2"。 |

## 操作的配置对象

- [配置的DB参数（DBPARAS）](configobject/UNC/20.15.2/DBPARAS.md)

## 使用实例

设置SDB打包参数。

```
SET DBPARAS: PARANAME=SdbBatchDuration, PARAVALUE="111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DB参数（SET-DBPARAS）_97800890.md`
