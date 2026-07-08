---
id: UNC@20.15.2@MMLCommand@ADD FWAMATCHRULE
type: MMLCommand
name: ADD FWAMATCHRULE（增加FWA用户匹配规则）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: FWAMATCHRULE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- FWA用户匹配规则管理
status: active
---

# ADD FWAMATCHRULE（增加FWA用户匹配规则）

## 功能

该命令用于增加FWA用户匹配规则。SMF根据匹配方式和匹配类型判断当前用户是否是FWA用户。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MATCHTYPE | 匹配类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配是否为FWA用户的类型，当前支持按照PCC Rule和APN进行匹配。<br>数据来源：本端规划<br>取值范围：<br>- MatchTypeRule（RULE匹配）<br>- MatchTypeApn（APN匹配）<br>默认值：无<br>配置原则：<br>大小写不敏感。 |
| MATCHFUNC | 匹配方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定采用全匹配还是只需要包含配置的PCC RULE或者APN的方式判断是否是FWA用户。<br>数据来源：本端规划<br>取值范围：<br>- “MatchFuncFull（全匹配）”：全匹配<br>- “MatchFuncContain（包含匹配）”：包含该字符串即匹配为FWA用户<br>默认值：无<br>配置原则：无 |
| RULE | PCC规则 | 可选必选说明：该参数在"MATCHTYPE"配置为"MatchTypeRule"时为条件必选参数。<br>参数含义：该参数用于指定用于判断是否是FWA用户的PCC规则。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：该参数在"MATCHTYPE"配置为"MatchTypeApn"时为条件必选参数。<br>参数含义：该参数用于指定用于判断是否是FWA用户的APN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FWAMATCHRULE]] · FWA用户匹配规则（FWAMATCHRULE）

## 使用实例

当需要增加基于指定PCC RULE进行全匹配来判断当前用户是否是FWA用户时，进行如下设置。

```
ADD FWAMATCHRULE:MATCHTYPE=MatchTypeRule,MATCHFUNC=MatchFuncFull,RULE="up_870000174";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-FWAMATCHRULE.md`
