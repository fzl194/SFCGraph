---
id: UNC@20.15.2@MMLCommand@RMV QOSACTRDRPOLICY
type: MMLCommand
name: RMV QOSACTRDRPOLICY（删除流行为下级联流策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSACTRDRPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 级联流策略动作
status: active
---

# RMV QOSACTRDRPOLICY（删除流行为下级联流策略）

## 功能

该命令用于在流行为视图下，删除修改级联流策略。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSACTRDRPOLICY]] · 流行为下级联流策略（QOSACTRDRPOLICY）

## 使用实例

流行为下删除配置级联流策略：

```
RMV QOSACTRDRPOLICY:BEHAVIORNAME="1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSACTRDRPOLICY.md`
