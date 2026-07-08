---
id: UNC@20.15.2@MMLCommand@RMV CHGAPN
type: MMLCommand
name: RMV CHGAPN（删除APN计费属性）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV CHGAPN（删除APN计费属性）

## 功能

**适用网元：SGSN**

该命令用来删除APN计费属性配置表中某条APN的配置。

## 注意事项

该命令执行后立即生效，执行后会影响新激活用户的话单生成策略，但该配置只对之后激活的用户有效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示此参数是指APN网络标识。<br>取值范围：长度不超过62的字符串<br>默认值：无<br>说明：- 按照3GPP协议，APN网络标识不区分大小写。为统一格式起见，APN网络标识的字母部分全部以大写格式保存。<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGAPN]] · APN计费属性（CHGAPN）

## 使用实例

删除APNNI为"huawei1.com"的计费属性配置：

RMV CHGAPN: APNNI="huawei1.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHGAPN.md`
