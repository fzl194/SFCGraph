---
id: UNC@20.15.2@MMLCommand@RMV MQCBEHAVIOR
type: MMLCommand
name: RMV MQCBEHAVIOR（删除流行为）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MQCBEHAVIOR
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类行为
status: active
---

# RMV MQCBEHAVIOR（删除流行为）

## 功能

该命令用于删除一个已经定义的流行为。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：指定流行为名称。定义的行为名不允许为系统预定义的流行为be。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MQCBEHAVIOR]] · 流行为（MQCBEHAVIOR）

## 使用实例

删除流行为b1：

```
RMV MQCBEHAVIOR:BEHAVIORNAME="b1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MQCBEHAVIOR.md`
