---
id: UDG@20.15.2@MMLCommand@SET INSAGLBCFG
type: MMLCommand
name: SET INSAGLBCFG（设置智能识别全局配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: INSAGLBCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 智能识别全局配置
status: active
---

# SET INSAGLBCFG（设置智能识别全局配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置智能识别全局配置。

## 注意事项

- 参数INFERSWITCH, IPFILTERSWITCH和INFERRATIOS对新流生效，参数POLICYSWITCH,INFERTHRES和INFERTMOUT立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INFERSWITCH | IPFILTERSWITCH | POLICYSWITCH | INFERRATIOS | INFERTHRES | INFERTMOUT |
| --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | DISABLE | 10000 | 600 | 200 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFERSWITCH | 智能识别推理能力开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置智能识别在线推理开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：智能识别在线推理不使能。<br>- ENABLE：智能识别在线推理使能。<br>默认值：无<br>配置原则：无 |
| IPFILTERSWITCH | 可信IP过滤开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INFERSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置智能识别可信IP过滤开关。该参数暂不生效。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：可信IP过滤不使能。<br>- ENABLE：可信IP过滤使能。<br>默认值：无<br>配置原则：无 |
| POLICYSWITCH | 智能识别结果用于策略匹配开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INFERSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置智能识别结果用于策略匹配开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：智能识别结果应用策略匹配不使能。<br>- ENABLE：智能识别结果应用策略匹配使能。<br>默认值：无<br>配置原则：无 |
| INFERRATIOS | 智能识别抽样比率(万分比) | 可选必选说明：条件可选参数<br>前提条件：该参数在“INFERSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定智能识别预处理抽样比。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~10000，单位是万分比。<br>默认值：无<br>配置原则：无 |
| INFERTHRES | 智能识别阈值(千分比) | 可选必选说明：条件可选参数<br>前提条件：该参数在“INFERSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置智能识别推理任务中推理结果有效判断阈值，推理结果的置信度如果大于等于阈值，认为推理结果有效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~1000，单位千分比。<br>默认值：无<br>配置原则：无 |
| INFERTMOUT | 智能识别推理超时时间(毫秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“INFERSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置智能识别推理超时时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围200~5000，单位毫秒。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INSAGLBCFG]] · 智能识别全局配置（INSAGLBCFG）

## 使用实例

设置智能识别推理能力开关为使能，设置可信IP过滤开关为使能，设置智能识别结果用于策略匹配开关为使能，设置智能识别抽样比率为10000，设置智能识别阈值为600，设置智能识别推理超时时间为200：

```
SET INSAGLBCFG:INFERSWITCH=ENABLE, IPFILTERSWITCH=ENABLE, POLICYSWITCH=ENABLE, INFERRATIOS=10000, INFERTHRES=600, INFERTMOUT=200;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-INSAGLBCFG.md`
