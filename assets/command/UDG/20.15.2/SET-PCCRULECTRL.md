---
id: UDG@20.15.2@MMLCommand@SET PCCRULECTRL
type: MMLCommand
name: SET PCCRULECTRL（设置PCC QoS相关控制参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PCCRULECTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- PCC QoS相关控制
status: active
---

# SET PCCRULECTRL（设置PCC QoS相关控制参数）

## 功能

**适用NF：PGW-U、UPF**

此命令用于控制PCC动态Rule生成的QoS Rule优先级是否按照PCF下发的优先级进行控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 此命令SMF也需要同步支持。对接的SMF与UPF需要统一规划此开关。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | QOSRULEPRIO |
| --- | --- |
| 初始值 | INTERNAL_ALLOCATION |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSRULEPRIO | QoS Rule优先级设置原则 | 可选必选说明：必选参数<br>参数含义：该参数用于配置QoS Rule优先级的设置原则。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- INTERNAL_ALLOCATION：内部分配（默认）。<br>- EQUAL_PCCRULE_PRECEDENCE：等于PCC Rule优先级。<br>默认值：无<br>配置原则：<br>- 当运营商不需要根据PCF下发的优先级分配QoS Rule的优先级时，需要将参数配置为INTERNAL_ALLOCATION。<br>- 当运营商需要根据PCF下发的优先级分配QoS Rule的优先级时，需要将参数配置为EQUAL_PCCRULE_PRECEDENCE。<br>- 当参数为EQUAL_PCCRULE_PRECEDENCE时，所有绑定过QoSprop（通过pccpolicygrp或者通过qos类型的rule绑定）的规则的优先级不能低于255。<br>- 当参数从INTERNAL_ALLOCATION修改为EQUAL_PCCRULE_PRECEDENCE时，所有绑定过QoSprop（通过pccpolicygrp或者通过qos类型的rule绑定）的规则的优先级，如果有高于255的，则不允许修改。 |

## 操作的配置对象

- [PCC QoS相关控制参数（PCCRULECTRL）](configobject/UDG/20.15.2/PCCRULECTRL.md)

## 使用实例

当运营商需要根据PCF下发的优先级分配QoS Rule的优先级时，配置如下：

```
SET PCCRULECTRL: QOSRULEPRIO=EQUAL_PCCRULE_PRECEDENCE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PCC-QoS相关控制参数（SET-PCCRULECTRL）_08342473.md`
