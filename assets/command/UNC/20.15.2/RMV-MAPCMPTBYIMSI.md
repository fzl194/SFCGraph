---
id: UNC@20.15.2@MMLCommand@RMV MAPCMPTBYIMSI
type: MMLCommand
name: RMV MAPCMPTBYIMSI（删除MAP协议接口兼容性IMSI号段配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MAPCMPTBYIMSI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- MAP应用协议
- MAP功能配置
status: active
---

# RMV MAPCMPTBYIMSI（删除MAP协议接口兼容性IMSI号段配置）

## 功能

**适用网元：SGSN**

该命令用于删除MAP协议接口兼容性IMSI号段配置。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MAP兼容性参数策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串。<br>默认值：无 |

## 操作的配置对象

- [MAP协议接口兼容性IMSI号段配置（MAPCMPTBYIMSI）](configobject/UNC/20.15.2/MAPCMPTBYIMSI.md)

## 使用实例

配置方式：删除 “用户范围” 为 “IMSI_PREFIX(指定IMSI前缀)” ， “IMSI前缀” 为“123456789”的配置记录

RMV MAPCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MAP协议接口兼容性IMSI号段配置(RMV-MAPCMPTBYIMSI)_26145468.md`
