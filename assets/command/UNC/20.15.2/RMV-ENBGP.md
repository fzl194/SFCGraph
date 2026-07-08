---
id: UNC@20.15.2@MMLCommand@RMV ENBGP
type: MMLCommand
name: RMV ENBGP（删除eNodeB群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ENBGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- eNodeB管理
- eNodeB群组管理
status: active
---

# RMV ENBGP（删除eNodeB群组）

## 功能

**适用网元：MME**

此命令用于删除eNodeB群组记录。

## 注意事项

- 此命令执行后立即生效。
- 删除eNodeB群组时必须首先删除该eNodeB群组下的所有成员，可执行[**RMV ENBGPMEM**](../eNodeB群组成员管理/删除eNodeB群组成员(RMV ENBGPMEM)_26305420.md)命令进行删除。
- 删除eNodeB群组时必须保证在EXTRFSP配置表中不存在该eNodeB群组的相关记录。可执行[**LST EXTRFSP**](../../RFSP管理/扩展RFSP策略管理/查询扩展RFSP策略组成员(LST EXTRFSP)_72345135.md)查看相关表的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENBGPID | eNodeB群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>数据来源：本端规划<br>取值范围：1~2048<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ENBGP]] · eNodeB群组（ENBGP）

## 使用实例

删除一个eNodeB群组，eNodeB群组标识为1:

RMV ENBGP: ENBGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ENBGP.md`
