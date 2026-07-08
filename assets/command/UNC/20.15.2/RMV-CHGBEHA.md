---
id: UNC@20.15.2@MMLCommand@RMV CHGBEHA
type: MMLCommand
name: RMV CHGBEHA（删除计费行为参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGBEHA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费行为参数配置
status: active
---

# RMV CHGBEHA（删除计费行为参数）

## 功能

**适用网元：SGSN**

该命令用于删除计费行为参数。计费行为是指当对某些用户实施计费时必须遵循的计费方式。

## 注意事项

该命令执行后立即生效。命令执行后影响新激活用户配置的计费行为策略。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CB | 计费行为 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是计费行为的编号。<br>取值范围：<br>- “B1(B1)”<br>- “B2(B2)”<br>- “B3(B3)”<br>- “B4(B4)”<br>- “B5(B5)”<br>- “B6(B6)”<br>- “B7(B7)”<br>- “B8(B8)”<br>- “B9(B9)”<br>- “B10(B10)”<br>- “B11(B11)”<br>- “B12(B12)”<br>默认值：无<br>说明：不同记录的CB的取值不能重复。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGBEHA]] · 计费行为参数（CHGBEHA）

## 使用实例

删除计费行为B1，配置格式为：

RMV CHGBEHA: CB=B1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除计费行为参数(RMV-CHGBEHA)_72225047.md`
