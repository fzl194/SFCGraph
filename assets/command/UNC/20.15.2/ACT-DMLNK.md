---
id: UNC@20.15.2@MMLCommand@ACT DMLNK
type: MMLCommand
name: ACT DMLNK（激活Diameter链路）
nf: UNC
version: 20.15.2
verb: ACT
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

# ACT DMLNK（激活Diameter链路）

## 功能

![](激活Diameter链路(ACT DMLNK)_26306088.assets/notice_3.0-zh-cn_2.png)

链路处于正常态时，不允许执行该操作，否则将导致部分业务损失。

**适用网元：SGSN、MME**

该命令用于激活Diameter链路。当需要恢复被 [**DEA DMLNK**](去活Diameter链路(DEA DMLNK)_72345877.md) 命令去活的MME与HSS、EIR、DRA或GMLC之间的链路的通信时，用此命令进行激活。

## 注意事项

- 该命令执行后立即生效。
- 链路处于激活态时，不允许执行该操作，否则将导致部分业务损失。
- 链路只有通过[**DEA DMLNK**](去活Diameter链路(DEA DMLNK)_72345877.md)命令去活后处于非激活态时，才需要进行激活操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKIDX | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备激活的Diameter链路的索引。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [Diameter链路配置（DMLNK）](configobject/UNC/20.15.2/DMLNK.md)

## 使用实例

激活链路索引为0的Diameter链路：

ACT DMLNK: LINKIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/激活Diameter链路(ACT-DMLNK)_26306088.md`
