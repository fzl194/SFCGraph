---
id: UNC@20.15.2@MMLCommand@ADD PROXYSMFACCLIST
type: MMLCommand
name: ADD PROXYSMFACCLIST（增加Proxy SMF接入控制列表）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PROXYSMFACCLIST
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- Proxy SMF接入列表
status: active
---

# ADD PROXYSMFACCLIST（增加Proxy SMF接入控制列表）

## 功能

**适用NF：SMF**

该命令用于Proxy SMF特性中增加接入控制列表记录。

## 注意事项

- 该命令执行后只对新激活用户生效。

- SUBRANGE为ALL_USER的记录为默认记录，不允许添加。

- 最多可输入70001条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SUBRANGE | PREFIX | CTRLTYPE | DESC |
| --- | --- | --- | --- |
| ALL_USER | * | ALLOW | All User |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接入控制的范围。<br>数据来源：本端规划<br>取值范围：<br>- IMSI_PRE（IMSI前缀）<br>- MSISDN_PRE（MSISDN前缀）<br>默认值：无<br>配置原则：<br>当存在多种用户范围的记录时，匹配的优先级由高到低为： IMSI_PRE/MSISDN_PRE，ALL_USER，如果某一用户同时匹配IMSI_PRE以及MSISDN_PRE记录时，最终是否允许接入受SET PROXYSMFFUNC命令中的CTRLTYPE参数控制。 |
| PREFIX | 前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PRE"、"MSISDN_PRE"时为条件必选参数。<br>参数含义：该参数用于指定接入控制的号码前缀，当SUBRANGE为IMSI_PRE时表示IMSI号码前缀，当SUBRANGE为MSISDN_PRE时表示MSISDN号码前缀。使用时按照最长匹配进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>取值范围为1~15位数字。 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否允许用户接入。<br>数据来源：本端规划<br>取值范围：<br>- ALLOW（允许）<br>- REJECT（拒绝）<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Proxy SMF接入控制列表的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PROXYSMFACCLIST]] · Proxy SMF接入控制列表（PROXYSMFACCLIST）

## 使用实例

添加用户范围为IMSI_PRE，前缀为27602，控制类型为ALLOW，描述信息为Vodafone的Proxy SMF接入列表记录，执行如下命令：

```
ADD PROXYSMFACCLIST: SUBRANGE=IMSI_PRE, PREFIX="27602", CTRLTYPE=ALLOW, DESC="Vodafone";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PROXYSMFACCLIST.md`
