---
id: UNC@20.15.2@MMLCommand@RMV ESMLC
type: MMLCommand
name: RMV ESMLC（删除E-SMLC配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ESMLC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- E-SMLC配置
status: active
---

# RMV ESMLC（删除E-SMLC配置）

## 功能

**适用网元：MME**

此命令用于删除E-SMLC配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESMLCID | E-SMLC 标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定E-SMLC标识。<br>数据来源：整网规划<br>取值范围：0～255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ESMLC]] · E-SMLC配置（ESMLC）

## 使用实例

删除一条“E-SMLC 标识”为“1”的E-SMLC配置记录：

RMV ESMLC: ESMLCID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ESMLC.md`
