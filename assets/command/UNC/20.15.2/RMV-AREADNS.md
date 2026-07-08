---
id: UNC@20.15.2@MMLCommand@RMV AREADNS
type: MMLCommand
name: RMV AREADNS（删除位置区域DNS域名）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AREADNS
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
- GnGp-SGSN_S10_S16_S3接口管理
- 位置域名管理
status: active
---

# RMV AREADNS（删除位置区域DNS域名）

## 功能

**适用网元：SGSN、MME**

该命令用于删除位置区域DNS域名。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定域名类型。<br>取值范围：<br>- “SGW_RAI（根据路由区（RAI）查找SGW）”<br>- “SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>- “SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>- “MME_TAI（根据跟踪区（TAI）查找MME）”<br>- “GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>- “PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>- “MSC_RAI（根据路由区（RAI）查找MSC）”<br>- “MSC_LAI（根据位置区（LAI）查找MSC）”<br>- “GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>- “SGW_LAI（根据位置区（LAI）查找SGW）”<br>- “SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>- “MME_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MME）”<br>- “SGW_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找SGW）”<br>- “MMEGI_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI）”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>或<br>“MSC_LAI（根据位置区（LAI）查找MSC）”<br>或<br>“SGW_LAI（根据位置区（LAI）查找SGW）”<br>或<br>“SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>或<br>“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>后显示。<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的LAC字段的值。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>后显示。<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的RAC字段的值。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“DNTYPE”<br>参数配置为<br>“SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>或<br>“MME_TAI（根据跟踪区（TAI）查找MME）”<br>或<br>“PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>后显示。<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的TAC字段的值。<br>说明：用户在输入值的时候，可以加上"0x"前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| UUT | UE USAGE TYPE | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE USAGE TYPE。<br>前提条件：<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MME”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找SGW”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREADNS]] · 位置区域DNS域名（AREADNS）

## 使用实例

删除域名类型为根据跟踪区（TAI）查找SGW，跟踪区域码为0x0001：

RMV AREADNS: DNTYPE=SGW_TAI, TAC="0x0001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AREADNS.md`
