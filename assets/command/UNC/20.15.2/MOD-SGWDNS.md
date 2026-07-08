---
id: UNC@20.15.2@MMLCommand@MOD SGWDNS
type: MMLCommand
name: MOD SGWDNS（修改S-GW DNS域名策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SGWDNS
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
- S11接口管理
- S-GW域名策略
status: active
---

# MOD SGWDNS（修改S-GW DNS域名策略）

## 功能

**适用网元：SGSN、MME**

当配置了多PLMN共享时，该命令用于修改S-GW中域名的组装策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS域名类型。<br>数据来源：整网规划<br>取值范围：<br>- “RAI(RAI)”<br>- “TAI(TAI)”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |
| RACRANGE | 路由区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区域码范围。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无<br>配置原则：该参数的取值需要大于或等于<br>“RAC”<br>。<br>说明：- 该参数与“RAC”参数构成一个RAC区段，方便客户配置连续的路由区域。<br>- 如果不输入，表示配置单个RAC。<br>- 相同“DNTYPE（域名类型）”和“LAC（位置区域码）”的RAC范围不允许交叉。 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“TAI(TAI)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值 ：无 |
| TACRANGE | 跟踪区域码范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区域码范围。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“TAI(TAI)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无<br>说明：该参数的取值需要大于或等于TAC。<br>说明：- 该参数与“TAC”参数构成一个TAC区段，方便客户配置连续的跟踪区域。<br>- 如果不输入，表示配置单个TAC。<br>- 相同“DNTYPE(域名类型)”的TAC范围不允许交叉。 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PLMN或HPLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PLMN或HPLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：2位或3位的十进制数<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWDNS]] · S-GW DNS域名策略（SGWDNS）

## 使用实例

修改一条域名类型为“TAI”，跟踪区域码为“1”的S-GW DNS域名策略记录，其跟踪区域码范围为“5”，移动国家代码为“461”，移动网号为“121”：

MOD SGWDNS: DNTYPE=TAI, TAC="1", TACRANGE="5", MCC="461", MNC="121";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S-GW-DNS域名策略（MOD-SGWDNS）_72225651.md`
