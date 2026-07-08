---
id: UNC@20.15.2@MMLCommand@ADD MQCBEHAVIOR
type: MMLCommand
name: ADD MQCBEHAVIOR（增加流行为）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MQCBEHAVIOR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类行为
status: active
---

# ADD MQCBEHAVIOR（增加流行为）

## 功能

该命令用于创建流行为；在复杂流分类的QoS策略中，如果需要对某类流执行相同的流行为，则需要用该命令创建流行为并在流行为中配置流动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8192。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：指定流行为名称。定义的行为名不允许为系统预定义的流行为be。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MQCBEHAVIOR]] · 流行为（MQCBEHAVIOR）

## 使用实例

创建流行为b1：

```
ADD MQCBEHAVIOR:BEHAVIORNAME="b1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加流行为（ADD-MQCBEHAVIOR）_50281310.md`
