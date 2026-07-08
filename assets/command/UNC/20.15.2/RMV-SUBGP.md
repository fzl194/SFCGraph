---
id: UNC@20.15.2@MMLCommand@RMV SUBGP
type: MMLCommand
name: RMV SUBGP（删除用户群）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SUBGP
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
- 用户群管理
status: active
---

# RMV SUBGP（删除用户群）

## 功能

**适用网元：SGSN、MME**

该命令用于删除用户群。

## 注意事项

- 该命令执行后立即生效。
- 删除用户群时必须首先删除该用户群下的全部成员记录。可执行[**LST SUBGPMEM**](../用户群成员管理/查询用户群成员(LST SUBGPMEM)_26145564.md)和[**LST MSISDNSUBGPMEM**](../MSISDN用户群成员管理/查询MSISDN用户群成员(LST MSISDNSUBGPMEM)_72225251.md)查看用户群下的成员记录。
- 删除用户群时必须保证区域限制相关表中不存在该用户群的相关记录。可执行[**LST S1ACCAREALST**](../S1模式区域漫游限制参数/查询S1模式接入控制配置（LST S1ACCAREALST）_26305368.md)、[**LST GBACCAREALST**](../Gb模式区域漫游限制参数/查询Gb模式区域漫游限制参数(LST GBACCAREALST)_72225233.md)和[**LST IUACCAREALST**](../Iu模式区域漫游限制参数/查询Iu模式区域漫游限制参数(LST IUACCAREALST)_72225235.md)查看区域限制相关表的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBID | 用户群标识 | 可选必选说明：必选参数<br>参数含义：待删除的指定用户群标识。<br>取值范围：1～100<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SUBGP]] · 用户群（SUBGP）

## 使用实例

删除一条用户群标识为30的用户群管理记录:

RMV SUBGP: SUBID=30;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUBGP.md`
