---
id: UDG@20.15.2@MMLCommand@SET EXPBASICFUNC
type: MMLCommand
name: SET EXPBASICFUNC（设置体验业务上报基本功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: EXPBASICFUNC
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 智能板管理
- vvip
- 体验分析基本功能
status: active
---

# SET EXPBASICFUNC（设置体验业务上报基本功能）

## 功能

**适用NF：PGW-U、UPF**

![](设置体验业务上报基本功能（SET EXPBASICFUNC）_31719867.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，SWITCH开关置为DISABLE后，体验业务基本功能将会失效。

此命令用于设置体验业务基本功能的开关及上报周期等参数。

## 注意事项

- 该命令执行后60s生效。
- 该命令最大记录数为1。
- 如果体验业务功能打开，建议调整智能板上的流老化时间，调整原则参考 SET SSUAGINGCFG命令，其中体验业务的单据采样时间通过EXPSAMPLEPERIOD配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | ANARPTPERIOD | SRVPORT | EXPSAMPLEPERIOD |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 300 | 15000 | 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 体验分析基本功能 | 可选必选说明：必选参数<br>参数含义：该参数是配置体验业务分析功能的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能体验业务基本功能。<br>- ENABLE：使能用户体验业务基本功能。<br>默认值：无<br>配置原则：无 |
| ANARPTPERIOD | 体验业务上报周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定体验业务向对端服务器发送单据的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30~600，单位为秒，建议按10秒的粒度配置。<br>默认值：无<br>配置原则：无 |
| SRVPORT | 体验业务上报的服务器端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：体验业务上报给对端服务器的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：无 |
| EXPSAMPLEPERIOD | 体验单据采集周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数指定UPF体验单据采样周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1~300。<br>默认值：无<br>配置原则：体验单据采集周期（秒）的值要小于等于体验业务上报周期（秒）的值。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EXPBASICFUNC]] · 体验业务基本功能（EXPBASICFUNC）

## 使用实例

设置体验业务上报基本功能，配置上报周期为300秒，指定上报的服务器端号为15000，采集单据周期为30秒，执行如下命令：

```
SET EXPBASICFUNC: SWITCH=ENABLE, ANARPTPERIOD=300, SRVPORT=15000, EXPSAMPLEPERIOD=30;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-EXPBASICFUNC.md`
