---
id: UNC@20.15.2@MMLCommand@MOD SMARTDT
type: MMLCommand
name: MOD SMARTDT（修改基于终端类型的DT限制）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: SMARTDT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 基于终端类型的DT限制
status: active
---

# MOD SMARTDT（修改基于终端类型的DT限制）

## 功能

**适用网元：SGSN**

此命令用于修改基于终端类型的Direct Tunnel限制的配置。

## 注意事项

- 此特性为可选特性，需要加载支持该特性的License，对应的License项为“Smartphone控制基础功能”。
- 当设置了某种终端类型的SMARTDT配置后，对该终端类型，基于Service Request频率的DT限制功能不再生效。基于Service Request频率的DT限制功能，是由SET SMARTCFG命令的DTSW参数控制的。当SGSN启用了基于Service Request频率的DT限制功能时，又需要针对某种终端类型例外，可执行该命令。
- 执行此命令，可能会导致Direct Tunnel相关的性能指标变化。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：待修改的终端类型。<br>数据来源：本端规划<br>取值范围:<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：- “UNKNOWN_TYPE(未知类型)”是指没有对应的IMEILIB或APNNILIB配置的终端类型。除“UNKNOWN_TYPE(未知类型)”以外的终端类型，可通过[**ADD IMEILIB**](../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)或[**ADD APNNILIB**](../终端类型识别/APNNI库管理/增加APNNI库记录（ADD APNNILIB）_26145736.md)命令设置。 |
| DTLIMIT | DT限制开关 | 可选必选说明：可选参数<br>参数含义：待修改的DT限制开关。<br>数据来源：本端规划<br>取值范围:<br>- “OFF(关闭)”<br>- “ON(开启)”<br>默认值：无<br>说明：- 建议值为“OFF(关闭)”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMARTDT]] · 基于终端类型的DT限制（SMARTDT）

## 使用实例

修改终端类型为微软的DT限制记录，设置不进行DT限制：

MOD SMARTDT: UETYPE=WINDOWS, DTLIMIT=OFF;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-SMARTDT.md`
