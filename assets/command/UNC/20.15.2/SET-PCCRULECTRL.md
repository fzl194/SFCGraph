---
id: UNC@20.15.2@MMLCommand@SET PCCRULECTRL
type: MMLCommand
name: SET PCCRULECTRL（设置PCC规则相关控制）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCCRULECTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- PCC Rule控制
status: active
---

# SET PCCRULECTRL（设置PCC规则相关控制）

## 功能

**适用NF：SMF**

该命令用于设置PCC规则相关控制。使能或关闭QosRule是否使用PccRule优先级。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QOSRULEPRIO |
| --- |
| INTERNAL_ALLOCATION |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSRULEPRIO | QoS Rule设置原则 | 可选必选说明：可选参数<br>参数含义：QOSRULEPRIO_SWITCH的值设置为INTERNAL_ALLOCATION，QosRule的优先级内部分配。QOSRULEPRIO_SWITCH的值设置为INHERIT_PCCRULE_PRECEDENCE，QosRule的优先级继承PCF下发PccRule优先级，并且SMF会限制PCF下发PccRule优先级范围是0~255。<br>数据来源：本端规划<br>取值范围：<br>- “INTERNAL_ALLOCATION（内部分配）”：QosRule不继承PccRule的优先级，QosRule的优先级内部分配。<br>- “INHERIT_PCCRULE_PRECEDENCE（继承PCC Rule优先级）”：QosRule的优先级继承PCF下发PccRule优先级，并且SMF会限制PCF下发PccRule优先级范围是0~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PCCRULECTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCRULECTRL]] · PCC规则相关控制（PCCRULECTRL）

## 使用实例

使能QosRule使用PccRule优先级。

```
SET PCCRULECTRL: QOSRULEPRIO= INHERIT_PCCRULE_PRECEDENCE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置PCC规则相关控制（SET-PCCRULECTRL）_09651839.md`
