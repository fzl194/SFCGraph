---
id: UNC@20.15.2@MMLCommand@DEA DMLNK
type: MMLCommand
name: DEA DMLNK（去活Diameter链路）
nf: UNC
version: 20.15.2
verb: DEA
object_keyword: DMLNK
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter链路
status: active
---

# DEA DMLNK（去活Diameter链路）

## 功能

![](去活Diameter链路(DEA DMLNK)_72345877.assets/notice_3.0-zh-cn_2.png)

进行链路去活操作，将导致其他链路的负荷增大，且会产生 [ALM-80591 Diameter链路故障](../../../../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SGSN&MME/ALM-80591 Diameter链路故障_89657084.md) 告警。如果到一个对等端的所有链路都被去活，将导致业务中断。

**适用网元：SGSN、MME**

该命令用于去活Diameter链路。当需要中断一条MME与HSS、EIR、DRA或GMLC之间的链路时，用该命令进行去活。

## 注意事项

- 该命令执行后立即生效。
- 若sgp进程复位，则复位前的去活操作失效。
- 该命令执行后，链路进入“非激活”状态。
- 去活链路会导致链路上不能够进行业务，业务会倒换到其他链路上，从而使其他链路的负荷增大，因此需要在业务量比较少的时候进行去活操作。
- 进行链路去活操作，会产生**ALM-80591 Diameter链路故障**告警。如果到一个对等端的所有链路都被去活，将导致业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备去活的Diameter链路的索引。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMLNK]] · Diameter链路配置（DMLNK）

## 使用实例

去活链路索引为0的Diameter链路：

DEA DMLNK: LINKIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/DEA-DMLNK.md`
