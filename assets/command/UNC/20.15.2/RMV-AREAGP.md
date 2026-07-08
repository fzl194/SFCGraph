---
id: UNC@20.15.2@MMLCommand@RMV AREAGP
type: MMLCommand
name: RMV AREAGP（删除区域群）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AREAGP
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
- 移动性管理
- 区域漫游限制管理
- 区域群管理
status: active
---

# RMV AREAGP（删除区域群）

## 功能

**适用网元：SGSN、MME**

此命令用于删除区域群记录。

## 注意事项

- 此命令执行后立即生效。
- 删除区域群时必须首先删除该区域群下的所有成员，可执行[**RMV AREAGPMEM**](../区域群成员管理/删除区域群成员(RMV AREAGPMEM)_26305356.md)。
- 删除区域群时必须保证区域限制相关表中不存在该区域群的相关记录。可执行[**LST S1ACCAREALST**](../S1模式区域漫游限制参数/查询S1模式接入控制配置（LST S1ACCAREALST）_26305368.md)、[**LST GBACCAREALST**](../Gb模式区域漫游限制参数/查询Gb模式区域漫游限制参数(LST GBACCAREALST)_72225233.md)和[**LST IUACCAREALST**](../Iu模式区域漫游限制参数/查询Iu模式区域漫游限制参数(LST IUACCAREALST)_72225235.md)查看区域限制相关表的记录。
- 删除区域群时必须保证对等PLMN中不存在该群组的相关记录，可执行[**LST PEERPLMN**](../../../网络管理/对等PLMN管理/查询对等PLMN配置(LST PEERPLMN)_26146098.md)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREAID | 区域群标识 | 可选必选说明：必选参数<br>参数含义：待删除的区域群标识。<br>数据来源：整网规划<br>取值范围：1~50<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREAGP]] · 区域群（AREAGP）

## 使用实例

删除一条区域群标识为1的区域群记录：

RMV AREAGP: AREAID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除区域群(RMV-AREAGP)_72225223.md`
