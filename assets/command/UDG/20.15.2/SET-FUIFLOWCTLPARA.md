---
id: UDG@20.15.2@MMLCommand@SET FUIFLOWCTLPARA
type: MMLCommand
name: SET FUIFLOWCTLPARA（设置欠费重定向流控参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: FUIFLOWCTLPARA
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
- 重定向控制
- FUI重定向控制
- FUI流控参数
status: active
---

# SET FUIFLOWCTLPARA（设置欠费重定向流控参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置因重定向放通的欠费DNS或临时流量转正无配额放行流量的控制是否使能，以及配置流控的参数和周期。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 命令用于一旦因欠费重定向放行的欠费DNS或临时流量转正无配额放行流量超过设置的阈值，设置检测或控制，可防止用户恶意欺诈。为避免欠费重定向流控参数配置不合理，建议先配置CHECK，观测相关话统判断是否合理后再开启为CONTROL，或联系华为工程师一起进行评估。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | DNS | TEMPVOLUME | TRAFFIC | PERIOD |
| --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | 1 | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNS | 欠费重定向DNS无配额流控开关 | 可选必选说明：必选参数<br>参数含义：当用户欠费执行重定向动作时，欠费DNS需要放行，此部分流量无法被统计计费，控制此部分流量的速率。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| TEMPVOLUME | 欠费重定向临时流量无配额流控开关 | 可选必选说明：必选参数<br>参数含义：开启了七层内容计费，在解析匹配七层规则前，报文记临时流量，匹配到具体规则后，临时流量关联匹配到费率，如果此时命中的URR已欠费，这部分流量无法计费将被丢弃。此参数控制此部分流量的速率。一旦用户无法计费的流量超过速率，禁止用户使用临时流量，费率不确认的报文则被丢弃。TCP建链握手消息流量会统计，但不受控制。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| TRAFFIC | 单用户流量阈值（字节） | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNS”配置为“ENABLE”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“TEMPVOLUME”配置为“ENABLE”时为必选参数。<br>参数含义：配置每用户每周期能通过的无法计费的流量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是字节。1~65535。<br>默认值：无<br>配置原则：无 |
| PERIOD | 流控周期（秒） | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNS”配置为“ENABLE”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“TEMPVOLUME”配置为“ENABLE”时为必选参数。<br>参数含义：配置Traffic的生效周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～60，单位是秒。1~60。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [欠费重定向流控参数（FUIFLOWCTLPARA）](configobject/UDG/20.15.2/FUIFLOWCTLPARA.md)

## 使用实例

如设置开启对因重定向放通的欠费DNS和临时流量转正无配额放行流量的流控，流控参数5000Byte，周期1秒，命令如下：

```
SET FUIFLOWCTLPARA: DNS=ENABLE, TEMPVOLUME=ENABLE, TRAFFIC=5000, PERIOD=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置欠费重定向流控参数（SET-FUIFLOWCTLPARA）_82837545.md`
