---
id: UNC@20.15.2@MMLCommand@RMV SHAREPLMNGP
type: MMLCommand
name: RMV SHAREPLMNGP（删除共享PLMN群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SHAREPLMNGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域MME共享管理
- 共享PLMN群组管理
status: active
---

# RMV SHAREPLMNGP（删除共享PLMN群组）

## 功能

**适用网元：MME**

在 **[MOCN](../../../../../../../../../网络部署/特性部署/UNC特性指南/网络共享功能/WSFD-207003 基于LTE的网络共享（MOCN）_68260814.md)** 组网下的两网融合项目中，基于区域逐步融合，需要配置基于特定区域PLMN的使用策略。该命令用于删除共享PLMN群组。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLMNGPID | PLMN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PLMN群组标识。<br>数据来源：本端规划<br>取值范围：1～31<br>默认值：无 |

## 操作的配置对象

- [共享PLMN群组（SHAREPLMNGP）](configobject/UNC/20.15.2/SHAREPLMNGP.md)

## 使用实例

删除一条： “PLMN群组标识” 为 “1” 的记录。

RMV SHAREPLMNGP: PLMNGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除共享PLMN群组(RMV-SHAREPLMNGP)_19372845.md`
