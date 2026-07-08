---
id: UNC@20.15.2@MMLCommand@RMV SERVUSR
type: MMLCommand
name: RMV SERVUSR（模拟设备故障删除用户信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SERVUSR
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
- 网络管理
- MME容灾管理
- 容灾功能调测
status: active
---

# RMV SERVUSR（模拟设备故障删除用户信息）

## 功能

**适用网元：SGSN、MME**

本命令通过本地删除指定用户的所有数据，删除用户的操作不会通知周边网元以及终端。用于调测"MME链式备份特性"，模拟设备故障场景后该指定用户的业务恢复测试。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTP | 删除方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定被删除用户的识别码类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI(指定IMSI)”<br>- “IMEI(指定IMEI)”<br>默认值：无<br>配置原则：指定IMEI删除仅适用于无USIM卡的紧急呼叫用户。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定被删除用户的国际移动用户识别码，由MCC，MNC，MSIN组成，在PLMN中唯一标识用户。<br>前提条件：该参数在<br>“删除方式”<br>设置为<br>“IMSI(指定IMSI)”<br>时有效。<br>数据来源：本端规划<br>取值范围：0~15位数字<br>默认值：无 |
| IMEI | IMEI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户设备的国际移动设备标识。<br>前提条件：该参数在<br>“删除方式”<br>设置为<br>“IMEI(指定IMEI)”<br>时有效。<br>数据来源：本端规划<br>取值范围：0~15位数字<br>默认值：无 |

## 操作的配置对象

- [模拟设备故障删除用户信息（SERVUSR）](configobject/UNC/20.15.2/SERVUSR.md)

## 使用实例

删除IMSI为123071104000955的用户数据：

RMV SERVUSR: RMVTP=IMSI, IMSI="123071104000955";

## 证据

- 原始手册：`evidence/UNC/20.15.2/模拟设备故障删除用户信息(RMV-SERVUSR)_26305928.md`
