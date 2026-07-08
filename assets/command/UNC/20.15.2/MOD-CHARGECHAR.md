---
id: UNC@20.15.2@MMLCommand@MOD CHARGECHAR
type: MMLCommand
name: MOD CHARGECHAR（修改对本地用户、漫游用户、拜访用户所采用的计费属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CHARGECHAR
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- 基本计费属性
status: active
---

# MOD CHARGECHAR（修改对本地用户、漫游用户、拜访用户所采用的计费属性）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来修改对本地用户、漫游用户、拜访用户所采用的计费属性。

计费属性指对用户所采用的计费类型，不同计费类型可以有不同的话单生成方式。用户的计费属性可以遵从SGSN/SGW上的属性配置，也可以遵从UNC上的属性配置。本地用户和漫游用户统称本PLMN（Public Land Mobile Network，运营商移动网络标识）的归属用户。UNC支持三种类型的用户：本地用户、漫游用户、拜访用户。

本地用户：指本PLMN网络上签约，未漫游到其他PLMN且在本UNC激活的用户。

漫游用户：指本PLMN网络上签约，漫游到其他PLMN且仍在本UNC激活的用户。

拜访用户：指其他PLMN网络上签约，漫游到本PLMN且使用本UNC激活的用户。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCNAME | 计费属性名称 | 可选必选说明：必选参数<br>参数含义：计费属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| HOME | 本地用户计费属性 | 可选必选说明：可选参数<br>参数含义：HOME是本地配置的本地用户CC，表示本地用户计费类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| ROAM | 漫游用户计费属性 | 可选必选说明：可选参数<br>参数含义：用于配置漫游用户的计费属性。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| VISIT | 拜访用户计费属性 | 可选必选说明：可选参数<br>参数含义：用于配置拜访用户的计费属性。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～6。该参数为十六进制数据类型，仅支持输入0x/X、a-f/A-F 、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000~0xFFFF。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HOMESGSN | 本地用户使用Serving Node计费属性 | 可选必选说明：可选参数<br>参数含义：配置本地用户是否使用签约下发的计费属性。当HOMESGSN配置为ENABLE时，表示本地用户使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：指对本地用户，使用用户激活消息中所携带的SGSN/SGW计费属性。<br>- DISABLE：指对本地用户，使用本地用户的计费属性所配置的属性。 |
| ROAMSGSN | 漫游用户使用Serving Node计费属性 | 可选必选说明：可选参数<br>参数含义：配置漫游用户是否使用签约下发的计费属性。当ROAMSGSN配置为ENABLE时，表示漫游用户使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：指对漫游用户，使用用户激活消息中所携带的SGSN/SGW计费属性。<br>- DISABLE：指对漫游用户，使用漫游用户的计费属性所配置的属性。 |
| VISITSGSN | 拜访用户使用Serving Node计费属性 | 可选必选说明：可选参数<br>参数含义：配置拜访用户是否使用签约下发的计费属性。当VISITSGSN配置为ENABLE时，表示拜访用户使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：指对拜访用户，使用用户激活消息中所携带的SGSN/SGW计费属性。<br>- DISABLE：指对拜访用户，使用拜访用户的计费属性所配置的属性。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHARGECHAR]] · 对本地用户、漫游用户、拜访用户所采用的计费属性（CHARGECHAR）

## 使用实例

修改计费属性（MOD CHARGECHAR），设置CCName为“cc”，Home为“0x0800”，Roam为“0x0100”，Visit为“0x0400”，HomeSgsn配置为ENABLE：

```
MOD CHARGECHAR:CCNAME="cc",HOME="0x0800",ROAM="0x0100",VISIT="0x0400",HOMESGSN=ENABLE,ROAMSGSN=DISABLE,VISITSGSN=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改对本地用户、漫游用户、拜访用户所采用的计费属性（MOD-CHARGECHAR）_09896810.md`
