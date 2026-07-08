---
id: UNC@20.15.2@MMLCommand@MOD ADCPARA
type: MMLCommand
name: MOD ADCPARA（修改ADC参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ADCPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- ADC
- ADC参数
status: active
---

# MOD ADCPARA（修改ADC参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于修改应用的流信息上报开关。流信息的上报功能是指对于需要进行检测上报的应用，在上报应用开始/结束上报时，同时上报当前业务的流信息，便于PCRF/PCF能够获取到应用与流的对应关系，从而可以下发更精确地策略对业务进行控制。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置应用对应的流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD FLOWFILTER命令配置生成。 |
| FLOWINFORPT | 流信息上报标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流信息上报标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不上报流信息。<br>- ENABLE：上报流信息。<br>默认值：无<br>配置原则：<br>- DISABLE：在向PCRF上报应用开始/结束时，不上报流信息。<br>- ENABLE：在向PCRF上报应用开始/结束时，上报流信息。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ADCPARA]] · ADC参数（ADCPARA）

## 使用实例

假设运营商需要将指定应用修改为不上报流信息，指定应用对应的流过滤器名称为testflowfiltername：

```
MOD ADCPARA:FLOWFILTERNAME="testflowfiltername",FLOWINFORPT=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ADCPARA.md`
