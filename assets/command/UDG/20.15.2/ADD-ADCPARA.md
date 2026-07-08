---
id: UDG@20.15.2@MMLCommand@ADD ADCPARA
type: MMLCommand
name: ADD ADCPARA（增加ADC参数）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ADCPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 8000
category_path:
- 用户面服务管理
- 业务控制策略
- ADC
- ADC参数
status: active
---

# ADD ADCPARA（增加ADC参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置应用的流信息上报开关。流信息的上报功能是指对于需要进行检测上报的应用，在上报应用开始/结束上报时，同时上报当前业务的流信息，便于PCRF/PCF能够获取到应用与流的对应关系，从而可以下发更精确地策略对业务进行控制。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器/流过滤器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置应用对应的流过滤器或流过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FLOWFILTER或ADD FLOWFILTERGRP命令配置生成。 |
| FLOWINFORPT | 流信息上报标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流信息上报标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不上报流信息。<br>- ENABLE：上报流信息。<br>默认值：DISABLE<br>配置原则：<br>- DISABLE：在向PCRF上报应用开始/结束时，不上报流信息。<br>- ENABLE：在向PCRF上报应用开始/结束时，上报流信息。 |
| KEYFLOWDETECTSW | 关键流检测开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置识别关键业务流的开关是否开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：DISABLE<br>配置原则：无 |
| KEYFLOWTIME | 关键流时长（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYFLOWDETECTSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于指定识别关键业务流的最低持续时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～60。<br>默认值：5<br>配置原则：无 |
| KEYFLOWSPEED | 关键流速率（二进制千比特每秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“KEYFLOWDETECTSW”配置为“ENABLE”时为可选参数。<br>参数含义：1、该参数用于指定关键业务流的最低传输速率。 2、参数单位是二进制千比特每秒，即Kibps，1Kibps等于1024bps。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2048。<br>默认值：50<br>配置原则：无 |
| ADCHYSTIMER | 应用级上报迟滞时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于配置ADC功能应用级上报迟滞时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3600。<br>默认值：0<br>配置原则：当单用户一个应用的Start和Stop消息上报过于频繁时，建议调大此参数。 当希望一个应用的Start和Stop消息上报尽量精确时，建议调小此参数。 该参数配置为0时，认为应用级延迟上报功能关闭。 |
| REDIRECTNAME | 重定向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD REDIRECT命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ADCPARA]] · ADC参数（ADCPARA）

## 关联任务

- [[UDG@20.15.2@Task@0-00031]]

## 使用实例

- 假设运营商需要为ADC应用添加流过滤器来匹配和检测出运营商需要的应用但不开启流信息上报功能时，指定流过滤器名称为testflowfiltername：
  ```
  ADD ADCPARA:FLOWFILTERNAME="testflowfiltername", KEYFLOWDETECTSW=DISABLE, ADCHYSTIMER=0;
  ```
- 假设运营商需要为ADC应用添加流过滤器并且开启流信息上报功能时，指定应用对应的流过滤器名称为testflowfiltername：
  ```
  ADD ADCPARA:FLOWFILTERNAME="testflowfiltername",FLOWINFORPT=ENABLE, KEYFLOWDETECTSW=ENABLE, KEYFLOWTIME=5, KEYFLOWSPEED=50, ADCHYSTIMER=0;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ADCPARA.md`
