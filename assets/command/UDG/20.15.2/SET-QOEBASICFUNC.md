---
id: UDG@20.15.2@MMLCommand@SET QOEBASICFUNC
type: MMLCommand
name: SET QOEBASICFUNC（设置QoE基本功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: QOEBASICFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 智能板管理
- QoE
- QoE基本功能
status: active
---

# SET QOEBASICFUNC（设置QoE基本功能）

## 功能

**适用NF：PGW-U、UPF**

![](设置QoE基本功能（SET QOEBASICFUNC）_72665978.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，设置不当会导致保障体验类业务功能不可用。

此命令用于设置QoE基本功能相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 只有开启了QOESWITCH开关和INQOESWITCH开关，QoE模型才会加载。
- 只有安装IISA服务后才可配置为融合智能感知模式。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | QOESWITCH | INQOESWITCH | MODE |
| --- | --- | --- | --- |
| 初始值 | DISABLE | ENABLE | SSU |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOESWITCH | QoE分析开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置QoE分析开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能QoE分析。<br>- ENABLE：使能QoE分析。<br>默认值：无<br>配置原则：无 |
| INQOESWITCH | QoE智能分析开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“QOESWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置QoE智能分析开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能QoE智能分析。<br>- ENABLE：使能QoE智能分析。<br>默认值：ENABLE<br>配置原则：无 |
| MODE | 运行模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INQOESWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用来指定体验感知业务的运行模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SSU：使用智能服务单元模式。<br>- IISA：使用融合智能感知模式。<br>默认值：SSU<br>配置原则：只有安装IISA服务后才可配置为融合智能感知模式。 |

## 操作的配置对象

- [QoE基本功能（QOEBASICFUNC）](configobject/UDG/20.15.2/QOEBASICFUNC.md)

## 使用实例

设置QoE基本功能，开启QoE分析开关，开启QoE智能分析开关，执行如下命令：

```
SET QOEBASICFUNC: QOESWITCH=ENABLE, INQOESWITCH=ENABLE,MODE=SSU;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置QoE基本功能（SET-QOEBASICFUNC）_72665978.md`
