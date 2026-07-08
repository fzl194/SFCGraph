---
id: UDG@20.15.2@MMLCommand@SET QOSACTFILTER
type: MMLCommand
name: SET QOSACTFILTER（设置流行为规则）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: QOSACTFILTER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为规则
status: active
---

# SET QOSACTFILTER（设置流行为规则）

## 功能

该命令用来设置流行为中满足规则的所有报文对应的过滤规则。缺省情况下，允许满足规则的所有报文通过。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| FILTER |
| --- |
| permit |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 需要先使用ADD MQCBEHAVIOR命令添加流行为。 |
| FILTER | 行为状态 | 可选必选说明：必选参数<br>参数含义：该参数用于指定动作为permit还是deny。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：满足规则的所有报文通过。<br>- deny：满足规则的所有报文不通过。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/QOSACTFILTER]] · 流行为规则（QOSACTFILTER）

## 使用实例

设置流行为b5的动作为满足规则的所有报文都不通过：

```
SET QOSACTFILTER:BEHAVIORNAME="b5",FILTER=deny;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置流行为规则（SET-QOSACTFILTER）_49802526.md`
