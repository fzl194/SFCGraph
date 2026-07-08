---
id: UNC@20.15.2@MMLCommand@SYN ACSPEERCFG
type: MMLCommand
name: SYN ACSPEERCFG（启动或停止ACS与远端设备的配置同步）
nf: UNC
version: 20.15.2
verb: SYN
object_keyword: ACSPEERCFG
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 对账管理
status: active
---

# SYN ACSPEERCFG（启动或停止ACS与远端设备的配置同步）

## 功能

![](启动或停止ACS与远端设备的配置同步(SYN ACSPEERCFG)_87242094.assets/notice_3.0-zh-cn_2.png)

该命令需要大约5分钟完成，命令执行期间系统的操作维护类命令无法执行，且会导致系统CPU和内存升高，如在话务高峰期需谨慎执行。

该命令用于手动开始或停止ACS服务向其他微服务执行配置同步操作。当其他微服务与ACS服务配置不一致时，可使用该命令进行手动配置同步，将ACS的配置强制同步给其他微服务。

> **说明**
> ACS服务会在每日凌晨3:00向其他微服务进行自动配置同步。当触发配置同步时，可能会导致网元CPU和内存持续较高。

## 注意事项

命令执行期间，配置开始同步后进行配置下发操作，可能会导致上报 “ALM-136978434 向远端下发的配置执行失败” 告警，配置同步成功后该告警自动清除。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| OPERTYPE | 操作类型 | 可选必选说明：必选。<br>参数含义：用于指定配置同步的操作类型。<br>取值范围：枚举类型。<br>- start(启动同步)：开始配置同步。<br>- stop(停止同步)：停止配置同步。<br>默认值：start(启动同步)。 |
| SYNSCOPE | 同步范围 | 可选必选说明：必选<br>参数含义：用于指定需要进行配置同步的微服务范围。<br>取值范围：枚举类型。<br>- all(同步所有)：对所有微服务进行配置同步。<br>- servicename(按服务名同步)：指定服务名称对微服务进行配置同步。<br>- servicename_instanceid(按服务名和实例ID同步)：指定服务名称和实例ID对微服务进行配置同步。<br>默认值：all(同步所有)。 |
| SERVICENAME | 服务名称 | 可选必选说明：当参数“同步范围(SYNSCOPE)”选择“servicename(按服务名同步)”或“servicename_instanceid(按服务名和实例ID同步)”时，该参数必选。<br>参数含义：用于指定需要进行配置同步的微服务名称，操作员可以使用<br>[DSP ACSSYNCINFO](查询ACS的配置同步信息(DSP ACSSYNCINFO)_87082450.md)<br>查询获得该参数。<br>取值范围：长度范围1~256的字符串。<br>默认值：无。 |
| INSTANCEID | 实例ID | 可选必选说明：当参数“同步范围(SYNSCOPE)”选择“servicename_instanceid(按服务名和实例ID同步)”时，该参数必选。<br>参数含义：用于指定需要进行配置同步的微服务实例ID，操作员可以使用<br>[DSP ACSSYNCINFO](查询ACS的配置同步信息(DSP ACSSYNCINFO)_87082450.md)<br>查询获得该参数。<br>取值范围：长度范围1~256的字符串。<br>默认值：无。 |
| SYNMODE | 同步方式 | 可选必选说明：可选。<br>参数含义：用于指定配置同步方式。<br>取值范围：枚举类型。<br>- incremental(增量同步)：进行增量配置同步。<br>- full(全量同步)：进行全量配置同步。<br>默认值：incremental(增量同步)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACSPEERCFG]] · 或停止ACS与远端设备的配置同步（ACSPEERCFG）

## 使用实例

```
SYN ACSPEERCFG: OPERTYPE=start, SYNSCOPE=servicename_instanceid, SERVICENAME="DemoGoServer", INSTANCEID="3537176978061755714", SYNMODE=full;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SYN-ACSPEERCFG.md`
