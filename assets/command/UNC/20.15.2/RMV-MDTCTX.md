---
id: UNC@20.15.2@MMLCommand@RMV MDTCTX
type: MMLCommand
name: RMV MDTCTX（删除MDT上下文）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MDTCTX
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
- MDT管理
status: active
---

# RMV MDTCTX（删除MDT上下文）

## 功能

![](删除MDT上下文(RMV MDTCTX)_26305646.assets/notice_3.0-zh-cn_2.png)

MDT任务正常运行时，删除本地的MDT配置参数会导致该任务异常。正常场景下请慎用本功能。

**适用网元：MME**

用于在异常场景下本地残留MDT配置参数时需要删除用户在MME上的MDT信息的情况下使用。

## 注意事项

- 该命令执行后立即生效。
- MDT任务正常运行时，删除本地的MDT配置参数会导致该任务异常。正常场景下请慎用本功能。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVOPTION | 删除方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定被删除用户的识别码类型。<br>取值范围：枚举类型。<br>- “BYIMSI(指定IMSI)。”<br>默认值：<br>“BYIMSI(指定IMSI)。” |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定被删除用户的国际移动用户识别码，由MCC，MNC，MSIN组成，在PLMN中唯一标识用户。<br>前提条件：该参数在<br>“删除方式”<br>设置为<br>“BYIMSI(指定IMSI)”<br>时有效。<br>取值范围：0~15位十进制数字。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MDTCTX]] · MDT上下文（MDTCTX）

## 使用实例

删除IMSI号为123032201000001的用户的MDT上下文的相关信息

RMV MDTCTX: RMVOPTION=BYIMSI, IMSI="123032201000001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MDTCTX.md`
