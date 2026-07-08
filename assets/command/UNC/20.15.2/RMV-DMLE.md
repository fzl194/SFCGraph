---
id: UNC@20.15.2@MMLCommand@RMV DMLE
type: MMLCommand
name: RMV DMLE（删除Diameter本端实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMLE
command_category: 配置类
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
- Diameter本地实体
status: active
---

# RMV DMLE（删除Diameter本端实体）

## 功能

![](删除Diameter本端实体(RMV DMLE)_26146282.assets/notice_3.0-zh-cn_2.png)

删除Diameter本端实体，可能导致用户接入失败。

**适用网元：SGSN、MME**

该命令用于删除Diameter本地实体信息。

## 注意事项

- 该命令执行后立即生效。
- 当Diameter链路集表（[**LST DMLKS**](../Diameter链路集/查询Diameter链路集配置(LST DMLKS)_26146280.md)）、归属网络信息表（[**LST HNOINFO**](../../../网络管理/归属网络运营商管理/归属网络信息管理/查询归属网络信息(LST HNOINFO)_72225733.md)）或IMSI号段属性配置表（[**LST IMSICHAR**](../../../网络管理/归属网络运营商管理/IMSI号段属性配置表/查询IMSI号段属性配置(LST IMSICHAR)_26146052.md)）中存在此本地实体相关的记录时，不允许删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的本地实体索引。<br>取值范围：0～31<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLE]] · Diameter本端实体（DMLE）

## 使用实例

将索引为0的本地实体删除：

RMV DMLE: LOINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter本端实体(RMV-DMLE)_26146282.md`
