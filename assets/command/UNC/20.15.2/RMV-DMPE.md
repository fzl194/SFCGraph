---
id: UNC@20.15.2@MMLCommand@RMV DMPE
type: MMLCommand
name: RMV DMPE（删除Diameter对端实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMPE
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
- Diameter对端实体
status: active
---

# RMV DMPE（删除Diameter对端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于删除Diameter对端实体配置。

## 注意事项

- 该命令执行后立即生效。
- 当DMHOSTRT，DMRT和DMLKS引用该对端实体索引时，不允许删除，在“MML命令行-UNC”窗口上执行命令[**LST DMHOSTRT**](../Diameter主机路由/查询Diameter主机路由(LST DMHOSTRT)_72345873.md)，[**LST DMRT**](../Diameter路由/查询Diameter域路由配置(LST DMRT)_72225969.md)，[**LST DMLKS**](../Diameter链路集/查询Diameter链路集配置(LST DMLKS)_26146280.md)查看对端实体索引是否被引用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERIDX | 对端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter对端实体索引。<br>取值范围：0～639<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMPE]] · Diameter对端实体（DMPE）

## 使用实例

删除索引为2的Diameter对端实体配置：

RMV DMPE: PEERIDX=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Diameter对端实体(RMV-DMPE)_26306096.md`
