---
id: UDG@20.15.2@MMLCommand@MOD ACLRULEBAS4
type: MMLCommand
name: MOD ACLRULEBAS4（修改基本ACL规则）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ACLRULEBAS4
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 基本ACL规则
status: active
---

# MOD ACLRULEBAS4（修改基本ACL规则）

## 功能

该命令用于修改基本ACL规则的配置，可以修改规则中的IP地址等匹配项。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令前，需要提前配置ADD ACLRULEBAS4命令添加ACL规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是2000～2999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |
| ACLACTION | 规则行为 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对符合本规则的报文采取的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Permit：允许符合该规则的访问。<br>- Deny：拒绝符合该规则的访问。<br>默认值：无 |
| ACLFRAGTYPE | 报文分片类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则所的报文分片类型，共有分片报文中的首片、分片报文中的非首片、非分片报文三种报文类型。如果不输入该参数，则表示不校验报文的分片信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FragmentSubseq：检查分片报文中的非首片。<br>- Fragment：检查报文是否为分片报文。<br>- NonFragment：检查非分片报文。<br>- NonSubseq：检查分片报文中的首分片，或非分片报文。<br>- FragmentSpeFirst：检查分片报文中的首片。<br>- Unconfiged：清除分片配置。<br>默认值：无 |
| ACLSOURCEIP | 源IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则要匹配的源IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：根据需要匹配的IP报文的源地址范围来设置该参数。 |
| ACLSRCWILD | 源IP地址反掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则要匹配的源IPv4地址反掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：根据需要匹配的IP报文的源地址范围来设置该参数。 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则匹配要生效的VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。字符之间不支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 使用LST L3VPNINST命令查看可用VPN。<br>- 当前修改ACL规则时不支持配置VPN。 |
| ACLRULEDESCRIPTION | 规则描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 建议取有实际意义的名称，以方便识别。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACLRULEBAS4]] · 基本ACL规则（ACLRULEBAS4）

## 使用实例

需要修改需要过滤的IP地址为10.1.1.2，可以修改基本ACL规则的配置：

```
MOD ACLRULEBAS4:ACLNAME="2000",ACLRULENAME="rule_5",ACLACTION=Deny,ACLSOURCEIP="10.1.1.2",ACLSRCWILD="0.0.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-ACLRULEBAS4.md`
