---
id: UNC@20.15.2@MMLCommand@MOD MQCPOLICYNODE
type: MMLCommand
name: MOD MQCPOLICYNODE（修改流策略节点）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MQCPOLICYNODE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类策略节点
status: active
---

# MOD MQCPOLICYNODE（修改流策略节点）

## 功能

该命令用于修改在流策略中为流分类指定流行为；当对接口上符合某种规则的流量执行特定的流行为时，需要在接口上应用流策略。在应用流策略之前必须使用该命令在流策略视图下将流分类和流行为进行绑定。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：必选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：必选参数<br>参数含义：指定流分类的名称。类名不允许为系统预定义类的名称default-class。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：指定流行为名称。定义的行为名不允许为系统预定义的流行为be。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| PRECEDENCE | 优先级 | 可选必选说明：可选参数<br>参数含义：指定策略匹配的优先级，流策略中按照优先级处理流分类的动作。取值越小优先级越高，优先被处理。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5100。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MQCPOLICYNODE]] · 流策略节点（MQCPOLICYNODE）

## 使用实例

在流策略p1中修改符合流分类c1的报文采用流行为b1：

```
MOD MQCPOLICYNODE:POLICYNAME="p1",CLASSIFIERNAME="c1",BEHAVIORNAME="b1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改流策略节点（MOD-MQCPOLICYNODE）_50281730.md`
