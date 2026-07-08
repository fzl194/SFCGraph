---
id: UNC@20.15.2@MMLCommand@SET SMARTCFG
type: MMLCommand
name: SET SMARTCFG（设置智能用户功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMARTCFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- Smartphone管理
- Smartphone控制基础功能
status: active
---

# SET SMARTCFG（设置智能用户功能）

## 功能

**适用网元：SGSN**

此命令可以设置SMART用户功能，包括是否开启智能用户识别功能、设置识别SMART用户的Service Request门限、SMART用户是否禁止启用Direct Tunnel功能和SMART用户是否禁止启用去活非活动PDP功能。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- "WSFD-206005Smartphone控制基础功能"为可选特性，需要加载支持该特性的License，对应的License项为“Smartphone控制基础功能”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMARTSW | 是否启用SMART用户识别功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否启用SMART用户识别功能。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“NO(否)” |
| SERVREQTHRESHOLD | 识别SMART用户的SERVICE REQUEST门限（times/h） | 可选必选说明：可选参数<br>参数含义：该参数用于设置识别SMART用户的ServiceRequest门限，通过此设置来识别Smartphone用户。<br>数据来源：本端规划<br>取值范围：2times/h~1000times/h<br>系统初始设置值：10times/h<br>说明：- 系统开工的缺省值是10times/h。<br>- 只有当“SMARTSW”设置为“YES(是)”时，配置该参数才有效。 |
| DTSW | SMART用户是否禁止启用DT功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SMART用户是否禁止启用Direct Tunnel功能。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“NO(否)”<br>说明：- 只有当“SMARTSW”设置为“YES(是)”时，配置该参数才有效。<br>- 当执行了[**ADD SMARTDT**](../基于终端类型的DT限制/增加基于终端类型的DT限制(ADD SMARTDT)_26145738.md)配置后，对[**ADD SMARTDT**](../基于终端类型的DT限制/增加基于终端类型的DT限制(ADD SMARTDT)_26145738.md)命令指定的终端类型，“SMARTSW”设置的基于Service Request频率的DT限制功能不再生效。<br>- 此参数设置为“YES(是)”时，可能会导致Direct Tunnel相关的性能指标变化。 |
| DEAPDPSW | SMART用户是否禁止启用去活非活动PDP功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否禁止启用去活非活动PDP功能。<br>数据来源：本端规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“NO(否)”<br>说明：- 只有当“SMARTSW”设置为“YES(是)”时，配置该参数才有效。<br>- 去激活非活动PDP功能由[**ADD CHGBEHA**](../../../../计费管理/计费行为参数配置/增加计费行为参数(ADD CHGBEHA)_26145366.md)命令中的“ BA”参数控制是否启用。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMARTCFG]] · 智能用户功能（SMARTCFG）

## 使用实例

设置智能用户功能如下: “是否启用SMART用户识别功能” 设置为 “是” ， “识别SMART用户的SERVICE REQUEST门限（times/h）” 设置为 “60” ， “SMART用户是否禁止启用DT功能” 设置为 “否” ， “SMART用户是否禁止启用去活非活动PDP功能” 设置为 “是” 。

SET SMARTCFG: SMARTSW=YES, SERVREQTHRESHOLD=60, DTSW=NO, DEAPDPSW=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置智能用户功能（SET-SMARTCFG）_26145750.md`
