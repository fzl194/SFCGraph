---
id: UNC@20.15.2@MMLCommand@ADD IMEIFORFD
type: MMLCommand
name: ADD IMEIFORFD（增加强制分离策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMEIFORFD
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 强制分离业务IMEI配置
status: active
---

# ADD IMEIFORFD（增加强制分离策略）

## 功能

**适用网元：SGSN**

此命令用于增加强制分离非活动用户时的IMEISV（International Mobile station Equipment Identity and Software Version）匹配规则。分离非活动用户功能由分离非活动用户定时器（ [**SET GBDETACH**](../分离非活动用户/Gb模式分离非活动用户参数/设置Gb分离非活动用户参数(SET GBDETACH)_72345095.md) 或 [**SET IUDETACH**](../分离非活动用户/Iu模式分离非活动用户参数/设置Iu分离非活动用户参数(SET IUDETACH)_26305310.md) ）控制，定时器（NACTTMR）默认时长为360分钟。定时器超时后， UNC 将根据此命令的配置，使用手机所携带的IMEISV与规则的掩码按位进行"与"运算，并和匹配规则比较。如果相同， UNC 将保留该用户；否则 UNC 将强制分离该非活动用户。如果手机不携带IMEISV，则默认不匹配规则， UNC 强制分离该用户。

在业务扩展特性配置中开启“分离非活动用户”功能后，如果运营商需要对某些用户（如VIP用户）不启用分离非活动用户功能，需要执行此命令。

可执行 [**SET GBDETACH**](../分离非活动用户/Gb模式分离非活动用户参数/设置Gb分离非活动用户参数(SET GBDETACH)_72345095.md) 或 [**SET IUDETACH**](../分离非活动用户/Iu模式分离非活动用户参数/设置Iu分离非活动用户参数(SET IUDETACH)_26305310.md) 命令，开启“分离非活动用户”功能。

## 注意事项

- 该表最大记录数为200。
- 该命令执行后立即生效。
- 如果需要匹配IMEI（International Mobile Subscriber Identity）而不是IMEISV，也可以使用此命令。使用任意0~9的数字将IMEI补足到16位，并在掩码的相应位上置0，使补充的该数字位无效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEISV | IMEISV | 可选必选说明：必选参数<br>参数含义：该参数用于设置<br>UNC<br>需要保留的IMEISV字段。<br>数据来源：整网规划<br>取值范围：16位十进制数字<br>默认值：无 |
| MASK | 掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMEISV字段相应的掩码。<br>数据来源：整网规划<br>取值范围：16位二进制数字<br>默认值：无<br>说明：掩码为1时，表示需要匹配IMEISV中的该位数字；掩码为0时，表示忽略IMEISV中该位数字。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEISV匹配规则的记录名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIFORFD]] · 强制分离策略（IMEIFORFD）

## 使用实例

设置一条为123456的匹配规则， UNC 不对此规则下的用户进行强制分离：

ADD IMEIFORFD: IMEISV="1234567890123456", MASK="1111110000000000", DESC="FOR USERGRP1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMEIFORFD.md`
