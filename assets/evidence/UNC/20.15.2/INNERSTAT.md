# 设置内统配置参数（SET INNERSTAT）

- [命令功能](#ZH-CN_MMLREF_0000001621603484__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001621603484__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001621603484__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001621603484__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001621603484)

![](设置内统配置参数（SET INNERSTAT）_21603484.assets/notice_3.0-zh-cn_2.png)

内统的日志打印周期设置过小会导致CPU和内存使用率升高，设置过大会导致关键统计信息丢失。

**适用NF：AMF**

该命令用于设置内统（内统指系统内部统计）配置参数，支持针对不同优先级的内统修改日志打印周期。

## [注意事项](#ZH-CN_MMLREF_0000001621603484)

- 该命令执行后立即生效。

- 该命令当前版本仅支持配置STATPRIORITY为DEFAULTPRIORITY时的内统的日志打印周期。
- 该命令仅限在华为工程师指导下使用。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STATPRIORITY | STATPERIOD | EXPIRETIME |
| --- | --- | --- |
| DEFAULTPRIORITY | STATPERIODDEFAULT | 0 |
| LOWPRORITY | STATPERIODDEFAULT | 0 |
| HIGHPRORITY | STATPERIODDEFAULT | 0 |

#### [操作用户权限](#ZH-CN_MMLREF_0000001621603484)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001621603484)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATPRIORITY | 内统优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内统优先级。<br>数据来源：本端规划<br>取值范围：<br>- DEFAULTPRIORITY（默认优先级）<br>- LOWPRORITY（低优先级）<br>- HIGHPRORITY（高优先级）<br>默认值：无。<br>配置原则：无 |
| STATPERIOD | 内统的日志打印周期 | 可选必选说明：必选参数<br>参数含义：该参数用于设置内统的日志打印周期。<br>数据来源：本端规划<br>取值范围：<br>- “STATPERIOD0（10秒）”：内统的日志打印周期为10秒。<br>- “STATPERIOD1（30秒）”：内统的日志打印周期为30秒。<br>- “STATPERIOD2（60秒）”：内统的日志打印周期为60秒。<br>- “STATPERIOD3（10分钟）”：内统的日志打印周期为10分钟。<br>- “STATPERIOD4（30分钟）”：内统的日志打印周期为30分钟。<br>- “STATPERIOD5（1小时）”：内统的日志打印周期为1小时。<br>- “STATPERIOD6（2小时）”：内统的日志打印周期为2小时。<br>- “STATPERIOD7（12小时）”：内统的日志打印周期为12小时。<br>- “STATPERIOD8（1秒）”：内统的日志打印周期为1秒。<br>- “STATPERIODDEFAULT（5分钟）”：内统的日志打印周期为5分钟。<br>默认值：无。<br>配置原则：无 |
| EXPIRETIME | 内统的日志打印周期失效时间 | 可选必选说明：可选参数<br>参数含义：该参数用于设置内统的日志打印周期失效时间。当内统的日志打印时间超过失效时间时，内统日志打印周期恢复为5min。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST INNERSTAT查询当前参数配置值。<br>配置原则：<br>该参数是从1970年1月1日(UTC的0点)开始所经过的秒数。<br>该参数取值为0时，内统日志打印周期为5min。 |

## [使用实例](#ZH-CN_MMLREF_0000001621603484)

设置默认优先级的内统的日志打印周期为5min，执行如下命令：

```
SET INNERSTAT: STATPRIORITY=DEFAULTPRIORITY, STATPERIOD=STATPERIODDEFAULT, EXPIRETIME=0;
```
