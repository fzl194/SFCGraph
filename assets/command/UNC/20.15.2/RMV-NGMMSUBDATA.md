---
id: UNC@20.15.2@MMLCommand@RMV NGMMSUBDATA
type: MMLCommand
name: RMV NGMMSUBDATA（删除用户移动性管理参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGMMSUBDATA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 签约数据管理
status: active
---

# RMV NGMMSUBDATA（删除用户移动性管理参数）

## 功能

**适用NF：AMF**

该命令用于删除为指定的用户（群）配置的移动性管理相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>对于指定的用户（群），匹配优先级从高到低依次为：“IMSI(指定IMSI)”，“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定应用本地接入和移动性签约数据配置的用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGMMSUBDATA]] · 用户移动性管理参数（NGMMSUBDATA）

## 使用实例

删除IMSI为123031234567890的用户的本地移动性管理签约数据，执行如下命令：

```
RMV NGMMSUBDATA: SUBRANGE=IMSI_PREFIX, IMSIPRE="123031234567890";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户移动性管理参数（RMV-NGMMSUBDATA）_09652660.md`
