---
id: UDG@20.15.2@MMLCommand@RMV MQCPOLICYNODE
type: MMLCommand
name: RMV MQCPOLICYNODE（删除流策略节点）
nf: UDG
version: 20.15.2
verb: RMV
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

# RMV MQCPOLICYNODE（删除流策略节点）

## 功能

该命令用于取消指定流分类在流策略中的使用。

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

## 操作的配置对象

- [[configobject/UDG/20.15.2/MQCPOLICYNODE]] · 流策略节点（MQCPOLICYNODE）

## 使用实例

取消流分类c1在流策略p1中的应用：

```
RMV MQCPOLICYNODE:POLICYNAME="p1",CLASSIFIERNAME="c1",BEHAVIORNAME="b1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流策略节点（RMV-MQCPOLICYNODE）_00865721.md`
