---
id: UNC@20.15.2@MMLCommand@SET DFTGBRBEARER
type: MMLCommand
name: SET DFTGBRBEARER（设置缺省GBR承载参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DFTGBRBEARER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- 缺省GBR承载
status: active
---

# SET DFTGBRBEARER（设置缺省GBR承载参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置SMF是否支持创建default-gbr承载（提供最低带宽保障的any to any GBR专有承载），该承载可由PCF/PCRF发起创建，也可以由SMF发起创建。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- SESSIONTERMINSW参数修改后立即生效。
- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：DFTGBRBEARERSW=DISABLE,LOCQOSQCI=4,LOCQOSARP=15,LOCQOSPREEMPCAP=DISABLE,LOCQOSPREEMPVUL=ENABLE,LOCQOSMBRUL=64,LOCQOSMBRDL=64,LOCQOSGBRUL=64,LOCQOSGBRDL=64,SESSIONTERMINSW=DISABLE,ACCTYPE=RATNON5G。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |
| DFTGBRBEARERSW | 缺省GBR承载开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置缺省GBR承载开关，是否支持SMF创建default-gbr承载。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：1. 运营商根据价值用户需求规划。 2. DftGBRBearerSw配置为DISABLE时，其余可选参数恢复为默认配置。 |
| LOCQOSQCI | 缺省GBR承载QCI值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载QCI值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSARP | 缺省GBR承载ARP值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载ARP值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～15。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSPREEMPCAP | 缺省GBR承载Pre-emption-Capability值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Pre-emption-Capability值。Pre-emption Capability即ARP的可抢占能力，代表资源限制时，业务是否可以抢占更低优先级别（Priority Level）的业务。取值范围为ENABLE和DISABLE，ENABLE表示具有抢占能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSPREEMPVUL | 缺省GBR承载Pre-emption-Vulnerability值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Pre-emption-Vulnerability值。Pre-emption-Vulnerability即ARP的被抢占能力，代表资源限制时，业务是否可以被更高优先级别（Priority Level）的业务抢占。取值范围为ENABLE和DISABLE，ENABLE表示允许被抢占。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSMBRUL | 缺省GBR承载UL MBR值（千比特/秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Max-Requested-Bandwidth-UL值(kbit/s)。Max-Requested-Bandwidth-UL定义了上行方向允许的最大比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSMBRDL | 缺省GBR承载DL MBR值(千比特/秒) | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Max-Requested-Bandwidth-DL值(kbit/s)。Max-Requested-Bandwidth-DL定义了下行方向允许的最大比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSGBRUL | 缺省GBR承载UL GBR值（千比特/秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Guaranteed-Bitrate-UL值(kbit/s)。Guaranteed-Bitrate-UL定义了上行方向允许的保障比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| LOCQOSGBRDL | 缺省GBR承载DL GBR值（千比特/秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载Guaranteed-Bitrate-DL值(kbit/s)。Guaranteed-Bitrate-DL定义了下行方向允许的保障比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～20000000，单位是千比特每秒。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| SESSIONTERMINSW | 缺省GBR承载去活时去活PDU会话 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置缺省GBR承载去活时是否去活PDU会话。该参数修改后立即生效。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |
| ACCTYPE | 用户接入类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DFTGBRBEARERSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用以指定缺省GBR承载适用的用户接入类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RATNON5G：非5G接入类型。<br>- RAT5G：5G接入类型。<br>- ALL：所有接入类型。<br>默认值：无<br>配置原则：运营商根据价值用户需求规划。 |

## 操作的配置对象

- [缺省GBR承载参数（DFTGBRBEARER）](configobject/UNC/20.15.2/DFTGBRBEARER.md)

## 使用实例

假如运营商需要配置APN支持PCRF/UNC发起default-gbr承载的创建，UNC发起创建时使用本地配置的QoS参数，则使用该实例：

```
SET DFTGBRBEARER: APN="test1",DFTGBRBEARERSW=ENABLE,LOCQOSQCI=1,LOCQOSARP=2,LOCQOSPREEMPCAP=ENABLE,LOCQOSPREEMPVUL=ENABLE,LOCQOSMBRUL=64,LOCQOSMBRDL=64,LOCQOSGBRUL=60,LOCQOSGBRDL=60,SESSIONTERMINSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置缺省GBR承载参数（SET-DFTGBRBEARER）_09897061.md`
