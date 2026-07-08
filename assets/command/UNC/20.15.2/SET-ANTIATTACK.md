---
id: UNC@20.15.2@MMLCommand@SET ANTIATTACK
type: MMLCommand
name: SET ANTIATTACK（设置防报文攻击上限）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ANTIATTACK
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
- GTP-C接口管理
- GTP-C协议管理
- 防报文攻击配置
status: active
---

# SET ANTIATTACK（设置防报文攻击上限）

## 功能

**适用网元：SGSN、MME**

该命令用来设置防报文攻击的上限值。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 防报文攻击对除路径管理、Error Indication之外的消息做流控，控制开关开启情况下被流控的消息每秒接收信令数不超过上限值。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPSIGMSGFLOWCTRLSWITCH | GTP信令流量控制开关 | 可选必选说明：可选参数<br>参数含义：该参数表示GTP信令流量控制开关。<br>数据来源：整网规划<br>取值范围：<br>- “ON(启用)”<br>- “OFF(关闭)”<br>系统初始设置值：<br>“OFF(关闭)”<br>。 |
| GTPSIGNUMLIMITPERSEC | 每秒接收信令个数上限 | 可选必选说明：条件可选参数<br>参数含义：该参数用于表示每秒接收信令个数上限。<br>数据来源：整网规划<br>前提条件：当<br>“GTP信令流量控制开关”<br>设置为<br>“ON(启用)”<br>时该参数有效。<br>取值范围：300~65535<br>系统初始设置值：<br>“300”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ANTIATTACK]] · 防报文攻击上限（ANTIATTACK）

## 使用实例

将GTP信令流量控制开关打开，每秒接收信令个数上限设置为700：

SET ANTIATTACK: GTPSIGMSGFLOWCTRLSWITCH=ON, GTPSIGNUMLIMITPERSEC=700;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ANTIATTACK.md`
