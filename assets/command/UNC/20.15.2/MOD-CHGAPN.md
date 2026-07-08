---
id: UNC@20.15.2@MMLCommand@MOD CHGAPN
type: MMLCommand
name: MOD CHGAPN（修改APN计费属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CHGAPN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- APN计费属性
status: active
---

# MOD CHGAPN（修改APN计费属性）

## 功能

**适用网元：SGSN**

该命令用于修改基于APN的计费属性信息。

## 注意事项

该命令执行后立即生效，但该配置只对之后激活的用户有效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是指APN网络标识。<br>数据来源：整网规划<br>取值范围：长度不超过62的字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。<br>说明：按照3GPP协议，APN网络标识不区分大小写。为统一格式起见，APN网络标识的字母部分全部以大写格式保存。 |
| CC | 计费属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示指当忽略HLR签约的APN计费属性时，应该对该APN的用户按何种计费方式收费。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL(普通计费)”：表示普通计费属性，按照此种方式计费的用户按照常规的方式支付费用。<br>- “PREPAID(预付费)”：表示预付费计费属性，按照此种方式计费的用户在获取某种服务之前需要预支付一定的费用。<br>- “FLATRATE(包月制)”：表示包月制计费属性，按照此种方式计费的用户在一个月内的收费是固定的。<br>- “HOTBILLING(实时计费)”：表示实时计费属性，按照此种方式计费的用户将在短时间或流量达到某个值时及时生成话单，保证运营商对此类用户及时收费。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGAPN]] · APN计费属性（CHGAPN）

## 使用实例

修改APNNI为"huawei1.com"的用户的计费属性为包月制计费属性：

MOD CHGAPN: APNNI="huawei1.com", CC=FLATRATE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改APN计费属性(MOD-CHGAPN)_72225045.md`
