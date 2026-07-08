---
id: UNC@20.15.2@MMLCommand@RMV S1SMARTRULE
type: MMLCommand
name: RMV S1SMARTRULE（删除S1模式信令抑制规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1SMARTRULE
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- 异常信令节省
- S1模式信令抑制规则管理
status: active
---

# RMV S1SMARTRULE（删除S1模式信令抑制规则）

## 功能

**适用网元：MME**

该命令用于删除基于用户终端类型的信令抑制规则。当不需要对某种终端进行信令抑制时，需要执行此命令。

## 注意事项

- 此命令执行后，当此终端类型的用户后续出现信令异常时，将不进行抑制，进行正常的业务流程。对于已经被抑制的用户，需要等到命令[**SET S1SMARTPARA**](../S1模式信令抑制参数管理/设置S1模式信令抑制参数(SET S1SMARTPARA)_72225427.md)设置的抑制时间超时后，才能解除抑制。

## 权限

manage-ug; system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UETYPE | 终端类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户的终端类型。<br>数据来源：本端规划<br>取值范围：<br>- “ANDROID(Android)”<br>- “BLACKBERRY(Black Berry)”<br>- “IOS(iOS)”<br>- “WINDOWS(Windows)”<br>- “CUSTOM_TYPE_1(自定义类型1)”<br>- “CUSTOM_TYPE_2(自定义类型2)”<br>- “CUSTOM_TYPE_3(自定义类型3)”<br>- “CUSTOM_TYPE_4(自定义类型4)”<br>- “CUSTOM_TYPE_5(自定义类型5)”<br>- “CUSTOM_TYPE_6(自定义类型6)”<br>- “CUSTOM_TYPE_7(自定义类型7)”<br>- “CUSTOM_TYPE_8(自定义类型8)”<br>- “CUSTOM_TYPE_9(自定义类型9)”<br>- “CUSTOM_TYPE_10(自定义类型10)”<br>- “CUSTOM_TYPE_11(自定义类型11)”<br>- “CUSTOM_TYPE_12(自定义类型12)”<br>- “UNKNOWN_TYPE(未知类型)”<br>默认值：无<br>说明：“UNKNOWN_TYPE(未知类型)”：未获取到IMEI的终端类型或者没有匹配的<br>[**ADD IMEILIB**](../../终端类型识别/IMEI库管理/增加IMEI库记录（ADD IMEILIB）_26145734.md)<br>配置的终端类型。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1SMARTRULE]] · S1模式信令抑制规则（S1SMARTRULE）

## 使用实例

删除 “终端类型” 为“ANDROID”的S1模式信令抑制规则配置记录：

RMV S1SMARTRULE: UETYPE=ANDROID;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-S1SMARTRULE.md`
