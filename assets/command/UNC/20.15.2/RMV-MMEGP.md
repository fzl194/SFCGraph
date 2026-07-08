---
id: UNC@20.15.2@MMLCommand@RMV MMEGP
type: MMLCommand
name: RMV MMEGP（删除MME群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMEGP
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
- MME群组管理
- MME群组配置
status: active
---

# RMV MMEGP（删除MME群组）

## 功能

**适用网元：MME**

该命令用于删除MME群组。

## 注意事项

- 该命令执行后立即生效。
- 删除MME群组时必须首先删除该MME群组下的所有成员，可执行[**RMV MMEGPMEM**](../MME群组成员配置/删除MME群组成员(RMV MMEGPMEM)_72345221.md)命令进行删除。
- 删除MME群组时必须保证相关表中不存在该MME群组的相关记录，可执行[**LST MMERESELPLCY**](../../MME重选管理/MME重选策略参数/查询MME重选策略(LST MMERESELPLCY)_72345225.md)查看相关表的记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>前提条件：无<br>数据来源：全网规划<br>取值范围：0～63<br>默认值：无 |

## 操作的配置对象

- [MME群组（MMEGP）](configobject/UNC/20.15.2/MMEGP.md)

## 使用实例

删除 “MME群组索引” 的MME群组配置记录

RMV MMEGP: MMEGPIDX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MME群组(RMV-MMEGP)_72345219.md`
