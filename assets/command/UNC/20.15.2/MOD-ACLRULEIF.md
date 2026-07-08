---
id: UNC@20.15.2@MMLCommand@MOD ACLRULEIF
type: MMLCommand
name: MOD ACLRULEIF（修改接口ACL规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ACLRULEIF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ACL管理
- 接口ACL规则
status: active
---

# MOD ACLRULEIF（修改接口ACL规则）

## 功能

该命令用于修改接口ACL规则，可以修改要过滤报文的接口。

## 注意事项

- 该命令执行后立即生效。
- 修改ACL规则前必须先执行ADD ACLRULEIF创建相应规则。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则属于哪个规则组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是1000～1999。<br>默认值：无 |
| ACLRULENAME | 规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。不支持空格，区分大小写。<br>默认值：无 |
| ACLACTION | 规则行为 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对符合本规则的报文采取的动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Permit：允许符合该规则的访问。<br>- Deny：拒绝符合该规则的访问。<br>默认值：无 |
| ACLIFANY | 所有的接口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则是否匹配所有接口。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| ACLRULEDESCRIPTION | 规则描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 建议取有实际意义的名称，以方便识别。 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定规则要匹配的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：根据需要匹配的接口设置有效的接口名。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACLRULEIF]] · 接口ACL规则（ACLRULEIF）

## 使用实例

用户使用流分类，需要将过滤接口修改为GigabitEthernet 0/0/1上的报文，可以修改接口ACL规则：

```
MOD ACLRULEIF:ACLNAME="1000",ACLRULENAME="rule_5",ACLACTION=Permit,IFNAME="GigabitEthernet0/0/1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改接口ACL规则（MOD-ACLRULEIF）_00865941.md`
