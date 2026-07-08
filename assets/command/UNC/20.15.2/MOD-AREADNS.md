---
id: UNC@20.15.2@MMLCommand@MOD AREADNS
type: MMLCommand
name: MOD AREADNS（修改位置区域DNS域名）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD AREADNS（修改位置区域DNS域名）

## 功能

**适用网元：SGSN、MME**

该命令用于修改位置区域DNS域名。

## 注意事项

该命令执行后立即生效。

区域名称的构成字符对大小写字母敏感。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定域名类型。<br>数据来源：全网规划<br>取值范围：<br>- “SGW_RAI（根据路由区（RAI）查找SGW）”<br>- “SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>- “SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>- “MME_TAI（根据跟踪区（TAI）查找MME）”<br>- “GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>- “PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>- “MSC_RAI（根据路由区（RAI）查找MSC）”<br>- “MSC_LAI（根据位置区（LAI）查找MSC）”<br>- “GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>- “SGW_LAI（根据位置区（LAI）查找SGW）”<br>- “SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>- “MME_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MME）”<br>- “SGW_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找SGW）”<br>- “MMEGI_TAI_UUT（根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI）”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>或<br>“MSC_LAI（根据位置区（LAI）查找MSC）”<br>或<br>“SGW_LAI（根据位置区（LAI）查找SGW）”<br>或<br>“SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>或<br>“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的LAC字段的值。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| LACRANGE | 位置区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定位置区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“MSC_LAI（根据位置区（LAI）查找MSC）”<br>或<br>“SGW_LAI（根据位置区（LAI）查找SGW）”<br>或<br>“SGSN_LAI（根据位置区（LAI）查找SGSN）”<br>或<br>“GGSN/PGW_LAI（根据位置区（LAI）查找GGSN/PGW）”<br>后显示。<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“位置区域码”的值。<br>- 新修改的位置区域码范围不能与其他已经存在的位置区域码范围出现重叠。<br>- 如果该参数不输入，表示将该配置记录修改为单个LAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的RAC字段的值。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| RACRANGE | 路由区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定路由区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_RAI（根据路由区（RAI）查找SGW）”<br>或<br>“SGSN_RAI（根据路由区（RAI）查找SGSN）”<br>或<br>“GGSN/PGW_RAI（根据路由区（RAI）查找GGSN/PGW）”<br>或<br>“MSC_RAI（根据路由区（RAI）查找MSC）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“路由区域码”的值。<br>- 新修改的路由区域码范围不能与其他已经存在的路由区域码范围出现重叠。<br>- 如果该参数不输入，表示将该配置记录修改为单个RAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>或<br>“MME_TAI（根据跟踪区（TAI）查找MME）”<br>或<br>“PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：该参数的值必须为已经在<br>[**ADD AREADNS**](增加位置区域DNS域名(ADD AREADNS)_72345559.md)<br>命令中配置的TAC字段的值。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>前提条件：该参数在<br>“域名类型”<br>参数配置为<br>“SGW_TAI（根据跟踪区（TAI）查找SGW）”<br>或<br>“MME_TAI（根据跟踪区（TAI）查找MME）”<br>或<br>“PGW_TAI（根据跟踪区（TAI）查找PGW）”<br>后显示。<br>数据来源：全网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>配置原则：<br>- 该参数的值必须大于等于“跟踪区域码”的值。<br>- 新修改的跟踪区域码范围不能与其他已经存在的跟踪区域码范围出现重叠。<br>- 如果该参数不输入，表示将该配置记录修改为单个TAC。<br>说明：用户在输入值的时候，可以加上<br>“0x”<br>前缀，也可以不加此前缀，都会被处理为16进制的数字。 |
| ZONESW | 定制区域标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于控制是否为位置区域定制标识。<br>数据来源：全网规划<br>取值范围：“NO（否）”“YES（是）”<br>默认值：无<br>配置原则：<br>- NO:将集合内的RAI/LAI/TAI映射到归一的RAI/LAI/TAI（即起始RAI/LAI/TAI），再根据通过归一的RAI/LAI/TAI来定制DNS域名。例如：位于RAI_1~RAI_10的用户请求以APN1激活时，统一将APN1定制为RAI_1+APN1进行DNS解析。<br>- YES:将集合内的RAI/LAI/TAI映射到区域名称(ZONENAME)，再根据区域名称来定制DNS域名。例如：位于RAI_1~RAI_10的用户请求以APN1激活时，统一将APN1定制为APN1.ZONE1.APNOI进行DNS解析。 |
| ZONENAME | 区域名称 | 可选必选说明：条件必选参数<br>参数含义：该参数标识位置区域，用于定制DNS域名，简化DNS Server或Hostfile的数据配置。<br>前提条件：该参数在<br>“定制区域标识”<br>参数配置为<br>“YES（是）”<br>后显示。<br>数据来源：全网规划<br>取值范围：1~32位字符串<br>默认值：无<br>配置原则：<br>区域名称的构成字符只能是字母A～Z或a～z、数字0～9、符号“-”和“.”，并且“-”和“.”不能是区域名称的开头和结尾，大小写不敏感。 |
| UUT | UE USAGE TYPE | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定UE USAGE TYPE。<br>前提条件：<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MME”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找SGW”<br>后生效。<br>- 该参数在<br>“域名类型”<br>参数配置为<br>“根据跟踪区（TAI）和UE USAGE TYPE查找MMEGI”<br>后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~255<br>默认值：无 |
| ZONELOC | 区域名称位置 | 可选必选说明：条件可选参数<br>参数含义：该参数用于标识区域名称在DNS域名中的位置。<br>前提条件：该参数在<br>“定制区域标识”<br>参数配置为<br>“YES（是）”<br>后显示。<br>数据来源：全网规划<br>取值范围：<br>- “APNNI_ZONE_APNOI（APNNI_ZONE_APNOI）”<br>- “ZONE_APNNI_APNOI（ZONE_APNNI_APNOI）”<br>默认值：无<br>配置原则：<br>- APNNI_ZONE_APNOI：区域名称位于DNS域名的中间位置。定制后的域名格式为：APNNI.ZONE.APNOI。<br>- ZONE_APNNI_APNOI：区域名称位于DNS域名的开始位置。定制后的域名格式为：ZONE.APNNI.APNOI。 |

## 操作的配置对象

- [位置区域DNS域名（AREADNS）](configobject/UNC/20.15.2/AREADNS.md)

## 使用实例

将与S-GW对应的 “0x01” 位置区下 “0x01” 到 “0x05” 路由区，修改为 “0x01” 到 “0x09” 路由区：

MOD AREADNS: DNTYPE=SGW_RAI, LAC="0x01", RAC="0x01", RACRANGE="0x09";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改位置区域DNS域名(MOD-AREADNS)_72225639.md`
