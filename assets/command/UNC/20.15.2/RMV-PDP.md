---
id: UNC@20.15.2@MMLCommand@RMV PDP
type: MMLCommand
name: RMV PDP（删除承载上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PDP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# RMV PDP（删除承载上下文）

## 功能

**适用网元：SGSN、MME**

该命令用于删除指定用户的承载上下文，同时根据输入参数来选择是否触发PDP的去激活流程。

## 注意事项

删除承载上下文并选择触发去激活流程，将导致被删除的承载上正在进行的数传业务终止，请慎重使用该命令。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定国际移动用户标识。<br>取值范围：1～15位的数字<br>默认值：无 |
| BEARID | 承载ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定承载标识。承载标识在一个用户内唯一的标识一条承载。<br>取值范围：5～15<br>默认值：无 |
| DEACT | 是否触发去激活的标志 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否触发去激活流程。<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无<br>说明：- 如果选择“YES(是)”，将会触发去激活流程，删除周边网元的承载信息。<br>- 如果选择“NO(否)”，将无法删除周边网元的承载信息。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PDP]] · 承载上下文（PDP）

## 使用实例

删除IMSI为123077552009900用户的7号承载上下文，不触发去激活流程：

RMV PDP: IMSI="123077552009900", BEARID=7, DEACT=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PDP.md`
