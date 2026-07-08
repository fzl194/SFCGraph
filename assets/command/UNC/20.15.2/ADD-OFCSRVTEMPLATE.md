---
id: UNC@20.15.2@MMLCommand@ADD OFCSRVTEMPLATE
type: MMLCommand
name: ADD OFCSRVTEMPLATE（增加离线业务模板）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OFCSRVTEMPLATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 业务级计费
- 业务计费模板
status: active
---

# ADD OFCSRVTEMPLATE（增加离线业务模板）

## 功能

**适用NF：PGW-C、SMF**

该命令用来新增离线业务模板的配置，用于设置离线业务计费相关配置信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 当前版本不支持此命令的TQM、QCTVALUE、BTIVALUE参数。
- 费率切换不中断业务级阈值的统计。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 离线业务模板名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定离线业务模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不允许输入空格。<br>默认值：无<br>配置原则：无 |
| TQM | 时长配额机制 | 可选必选说明：可选参数<br>参数含义：该参数用于指定时长配额机制。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DTP：DTP（Discrete Time Period）计费。<br>- CTP：CTP（Continuous Time Period）计费。<br>- QCT：QCT（Quota Consumption Time）计费。<br>- INHERIT：指定继承离线计费模板中的时长配额机制配置。<br>- OPERATOR_CTP：OPERATOR_CTP计费。<br>默认值：INHERIT<br>配置原则：无 |
| QCTVALUE | QCT时长 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TQM”配置为“QCT”时为必选参数。<br>参数含义：该参数用于指定QCT（Quota Consumption Time）计费方式下的业务空耗时长。当业务空耗时长超时后，话单中对应业务的业务容器不再记录超时时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～200，单位是秒。<br>默认值：无<br>配置原则：该参数配置为0时，表示QCT计费方式不生效，对应业务使用的计费方式为NORMAL计费。 |
| BTIVALUE | BTI时长 | 可选必选说明：条件必选参数<br>前提条件：该参数在“TQM”配置为“DTP”、“CTP” 或 “OPERATOR_CTP”时为必选参数。<br>参数含义：该参数用于指定DTP、CTP、OPERATOR-CAT计费方式下的业务信封时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为60～86400，单位是秒。<br>默认值：无<br>配置原则：无 |
| L7INDICATORSW | L7内容计费开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定离线业务模板对应的业务是否使能7层内容计费。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无 |
| TIMETHRESHOLD | 业务时长阈值（分） | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务时间阈值。当用户进行业务的时长达到设定的时间阈值时，系统将为用户产生一个业务容器。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，单位是分钟。<br>默认值：0<br>配置原则：<br>- 该参数配置为0时，表示时间阈值不生效。<br>- 该命令配置的QCT计费方式生效时，时间阈值不生效。 |
| VOLUMETHRESHOLD | 业务流量阈值（千字节） | 可选必选说明：可选参数<br>参数含义：该参数用于指定业务流量阈值。当用户进行业务所使用的流量达到设定的流量阈值时，系统将为用户产生一个业务容器。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，20～9000000000，单位是千字节。<br>默认值：0<br>配置原则：<br>- 该参数配置为0时，表示流量阈值不生效。<br>- 该命令配置的QCT计费方式生效时，流量阈值不生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OFCSRVTEMPLATE]] · 离线业务模板（OFCSRVTEMPLATE）

## 使用实例

新增名为“offlinetmp”的离线业务模板，配置时长配额机制为QCT计费，QCT时长为100秒，配置业务时长阈值为5分钟，配置业务流量阈值为1024K，并开启L7内容计费：

```
ADD OFCSRVTEMPLATE:TEMPLATENAME="offlinetmp",TQM=QCT,QCTVALUE=100,L7INDICATORSW=ENABLE,TIMETHRESHOLD=5,VOLUMETHRESHOLD=1024;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OFCSRVTEMPLATE.md`
