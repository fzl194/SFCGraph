---
id: UNC@20.15.2@MMLCommand@RMV NGPEIPLCY
type: MMLCommand
name: RMV NGPEIPLCY（删除5G PEI策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPEIPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- PEI策略管理
status: active
---

# RMV NGPEIPLCY（删除5G PEI策略）

## 功能

**适用NF：AMF**

该命令用于为指定用户删除PEI控制策略。

## 注意事项

- 该命令执行后立即生效。

- 此命令只能删除指定号段用户的PEI控制策略，不能删除默认的PEI控制策略。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “IMSI_PREFIX（指定IMSI前缀）”：指定IMSI前缀<br>- “IMSI（指定IMSI）”：IMSI<br>默认值：无<br>配置原则：<br>当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定IMSI前缀，取值5～15位十进制数字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定IMSI，取值14~15位十进制数字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPEIPLCY]] · 5G PEI策略（NGPEIPLCY）

## 使用实例

删除IMSI前缀为“123456”的用户的PEI配置策略，执行如下命令：

```
RMV NGPEIPLCY:SUBRANGE=IMSI_PREFIX, IMSIPRE="123456";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGPEIPLCY.md`
