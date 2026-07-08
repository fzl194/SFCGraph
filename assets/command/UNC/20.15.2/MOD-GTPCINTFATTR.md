---
id: UNC@20.15.2@MMLCommand@MOD GTPCINTFATTR
type: MMLCommand
name: MOD GTPCINTFATTR（修改GTP-C IP地址接口属性）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: GTPCINTFATTR
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C接口类型属性
status: active
---

# MOD GTPCINTFATTR（修改GTP-C IP地址接口属性）

## 功能

**适用网元：SGSN、MME、AMF**

该命令用于修改已存在记录的名称等维护信息。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODTYPE | 修改条件 | 可选必选说明：必选参数<br>参数含义：该参数用于指定修改操作的类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYINTFSUB(根据接口类型和用户范围)” |
| INDEX | 记录索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定已存在记录的名称。<br>前提条件：该参数在"操作条件"参数配置为"BYINDEX(根据记录索引)"后生效。<br>数据来源：本端规划<br>取值范围：0~4294967295<br>默认值：无<br>说明：使用<br>[**LST GTPCINTFATTR**](查询GTP-C IP地址接口属性(LST GTPCINTFATTR)_26145902.md)<br>查询记录的名称。 |
| SUBRANGE | 用户范围 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的用户范围。<br>前提条件：该参数在"修改条件"参数配置为"BYINTFSUB(根据接口类型和用户范围)"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数。<br>参数含义：该参数用于指定运营商ID。<br>前提条件：该参数在“用户范围”设置为“指定运营商”后生效。<br>数据来源：全网规划。<br>取值范围： 0~64,128~254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数。<br>参数含义：这个参数指明IMSI前缀。在查询过程中采用最长匹配原则。<br>前提条件：该参数在“用户范围”设置为“指定IMSI前缀”后生效。<br>数据来源：全网规划。<br>取值范围：1至15位的十进制数字<br>默认值：无 |
| INTFTP | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的接口类型。<br>前提条件：该参数在"用户范围"参数配置为"ALL_USER(所有用户)"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “S10(S10)”<br>- “S11(S11)”<br>- “S3(S3)”<br>- “S4(S4)”<br>- “SV(Sv)”<br>默认值：无 |
| INTFTP2 | 接口类型2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPC IP地址适用的接口类型。<br>前提条件：<br>- 该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>- 该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定描述信息。<br>数据来源：本端规划<br>取值范围：0~31位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCINTFATTR]] · GTP-C IP地址接口属性（GTPCINTFATTR）

## 使用实例

将修改类型为BYINDEX、INDEX为1的记录的DESC修改为"huawei01"

MOD GTPCINTFATTR: MODTYPE=BYINDEX,INDEX=1,DESC="huawei01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-GTPCINTFATTR.md`
