---
id: UDG@20.15.2@MMLCommand@SET IPSPOOFALMTHD
type: MMLCommand
name: SET IPSPOOFALMTHD（设置IP Spoofing攻击告警阈值控制）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPSPOOFALMTHD
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务安全防护
- 用户攻击防护
- IP Spoofing攻击防护
- 反嗅探告警
status: active
---

# SET IPSPOOFALMTHD（设置IP Spoofing攻击告警阈值控制）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置是否产生ip spoofing告警以及何时产生告警。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- ip spoofing事件：系统的PDP如果受到ip spoofing攻击，则认为是一个事件，以PDP作为事件单位。
- 当ALARMSWITCH从ENABLE配置为DISABLE时，INITTHRESH和ADDTHRESH将恢复为默认记录。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALARMSWITCH | INITTHRESH | ADDTHRESH |
| --- | --- | --- | --- |
| 初始值 | DISABLE | 1000 | 1000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALARMSWITCH | anti spoofing告警开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置是否打开anti spoofing告警功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：设置ENABLE：使能，打开anti spoofing告警功能；设置DISABLE: 不使能，关闭anti spoofing告警功能。 |
| INITTHRESH | 初始阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于在anti spoofing事件计数大于INITTHRESH值时触发事件告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～65535。<br>默认值：无<br>配置原则：无 |
| ADDTHRESH | 增量阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALARMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于在anti spoofing事件计数减去INITTHRESH等于ADDTHRESH的整数倍时再次触发告警。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为100～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSPOOFALMTHD]] · IP Spoofing攻击告警阈值（IPSPOOFALMTHD）

## 使用实例

假设运营商需要感知ip spoofing是否到达所配置的INITTHRSH为1500，ADDTHRESH为1500时告警：

```
SET IPSPOOFALMTHD:ALARMSWITCH=ENABLE,INITTHRESH=1500,ADDTHRESH=1500;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IPSPOOFALMTHD.md`
