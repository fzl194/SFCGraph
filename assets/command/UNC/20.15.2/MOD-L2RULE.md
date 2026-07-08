---
id: UNC@20.15.2@MMLCommand@MOD L2RULE
type: MMLCommand
name: MOD L2RULE（修改层二规则）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: L2RULE
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二规则
status: active
---

# MOD L2RULE（修改层二规则）

## 功能

**适用NF：SMF**

该命令用于修改层二规则。

## 注意事项

该命令执行后只对新接入的会话生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULENAME | 层二规则名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| QOSPROPNAME | QoS属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD QOSPROP命令配置生成，且只允许指定QOSTYPE为QOS_L2_PARA的Qos属性记录。 |
| L2FILTERNAME | 层二过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定层二过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD L2FILTER命令配置生成。 |

## 操作的配置对象

- [层二规则（L2RULE）](configobject/UNC/20.15.2/L2RULE.md)

## 使用实例

假如运营商需要修改一个层二规则绑定的Qos属性和层二过滤器，其中Qos属性名称为“qosprop2”，层二过滤器名称为“filter2”：

```
MOD L2RULE: L2RULENAME="rule1", QOSPROPNAME="qosprop2", L2FILTERNAME="filter2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改层二规则（MOD-L2RULE）_70462577.md`
