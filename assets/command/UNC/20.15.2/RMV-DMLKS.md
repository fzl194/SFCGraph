---
id: UNC@20.15.2@MMLCommand@RMV DMLKS
type: MMLCommand
name: RMV DMLKS（删除Diameter链路集配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMLKS
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
- Diameter链路集
status: active
---

# RMV DMLKS（删除Diameter链路集配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一条Diameter链路集。

## 注意事项

- 该命令执行后立即生效。
- 当Diameter链路表中引用了该链路集的索引时，不允许删除。可通过[**LST DMLNK**](../Diameter链路/查询Diameter链路配置(LST DMLNK)_26146276.md)命令查看Diameter链路表中是否存在对该链路集的索引的引用，通过[**RMV DMLNK**](../Diameter链路/删除Diameter链路配置(RMV DMLNK)_26306086.md)删除相关链路后，才允许删除该链路集。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LINKSIDX | Diameter链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的Diameter链路集的索引。<br>取值范围：0～639<br>默认值：无<br>说明：可以通过<br>[**LST DMLKS**](查询Diameter链路集配置(LST DMLKS)_26146280.md)<br>命令查看已有配置，确认所要删除的Diameter链路集的索引。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLKS]] · Diameter链路集配置（DMLKS）

## 使用实例

删除Diameter链路集索引为0的链路集。

RMV DMLKS: LINKSIDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter链路集配置(RMV-DMLKS)_26306090.md`
