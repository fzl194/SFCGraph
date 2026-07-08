---
id: UNC@20.15.2@MMLCommand@UBL LOCALNRI
type: MMLCommand
name: UBL LOCALNRI（解闭本局NRI配置信息）
nf: UNC
version: 20.15.2
verb: UBL
object_keyword: LOCALNRI
command_category: 调测类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- 本局NRI配置
status: active
---

# UBL LOCALNRI（解闭本局NRI配置信息）

## 功能

**适用网元：SGSN**

此命令用于解闭本局NRI配置信息。本局NRI被解闭塞之后，SGSN在新分配PTMSI时，该本局NRI将可以继续被使用。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL区标识。<br>取值范围：0～4095<br>默认值：无 |
| NRIVBGN | NRI起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRI起始值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>取值范围：0～1023<br>默认值：无<br>说明：- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。<br>- 若POOL表的NRI长度为10，则LOCALNRI表的NRI个数必须大于等于4， NRI起始值小于等于1020。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALNRI]] · 本局NRI配置信息（LOCALNRI）

## 使用实例

解闭一条POOLID为1，NRI的值为10的本局NRI配置信息：

UBL LOCALNRI: POOLID=1, NRIVBGN=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/解闭本局NRI配置信息(UBL-LOCALNRI)_72345701.md`
