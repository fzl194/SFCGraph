---
id: UNC@20.15.2@MMLCommand@RMV SCCPSSN
type: MMLCommand
name: RMV SCCPSSN（删除SCCP子系统）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCCPSSN
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP子系统
status: active
---

# RMV SCCPSSN（删除SCCP子系统）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP子系统表中指定的记录。

## 注意事项

- 此命令执行后立即生效。
- 子系统在GT表中不能存在。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SSNX | 子系统索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子系统对应的索引值。<br>取值范围：0~2047<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCCPSSN]] · SCCP子系统（SCCPSSN）

## 使用实例

以下命令删除SCCP子系统表中索引为1的记录：

RMV SCCPSSN: SSNX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCCPSSN.md`
