---
id: UNC@20.15.2@MMLCommand@SET SMARTACTPARA
type: MMLCommand
name: SET SMARTACTPARA（设置激活抑制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMARTACTPARA
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
- 异常信令节省
- 激活抑制参数管理
status: active
---

# SET SMARTACTPARA（设置激活抑制参数）

## 功能

**适用网元：SGSN**

此命令用于设置异常激活抑制参数，包括设置识别异常激活行为的门限，抑制唤醒定时器，假激活的Packing APNNI，分离异常用户的门限。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。
- "WSFD-206006Smartphone异常信令节省"需要加载支持该特性的License，对应的License项为“Smartphone异常信令节省”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ABNORACTTHRESH | 识别异常激活行为的门限（times/h） | 可选必选说明：可选参数<br>参数含义：该参数为识别异常激活行为的门限，即在一个小时内如果PDP激活的次数超过了此参数的值，则认为此用户的激活行为异常。<br>数据来源：本端规划<br>取值范围：2times/h～1000times/h<br>系统初始设置值： 30times/h<br>说明：只有当配置了<br>[**ADD SMARTACT**](../激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)<br>命令后，配置该参数才有效。 |
| WAKEUPTIMER | 抑制唤醒定时器（min） | 可选必选说明：可选参数<br>参数含义：该参数设置抑制唤醒定时器长度。执行抑制措施后，抑制唤醒定时器即启动，在定时器超时后，则执行唤醒措施。<br>数据来源：本端规划<br>取值范围：5min～600min<br>系统初始设置值： 60min<br>配置原则：<br>- 该参数的值和实际唤醒时间有最多14分钟的误差。<br>说明：只有当配置了<br>[**ADD SMARTACT**](../激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)<br>命令后，配置该参数才有效。 |
| PARKINGAPN | Parking APN | 可选必选说明：可选参数<br>参数含义：该参数设置激活抑制策略中假激活使用的Parking APNNI。<br>数据来源：本端规划<br>取值范围：1～62位字符串<br>系统初始设置值：NULL<br>说明：- 只有当[**ADD SMARTACT**](../激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)命令中的“Parking APN假激活功能开关”打开后，配置该参数才有效。<br>- 不支持输入*和其他字符组合。 |
| DETACHSERVREQTHRESH | 分离异常用户的SERVICE REQUEST门限（times/h） | 可选必选说明：可选参数<br>参数含义：该参数为分离异常用户的Service Request门限，即Parking APN抑制状态下，在一个小时内如果用户的Service Request次数超过了此参数的值，则进行网络侧分离。<br>数据来源：本端规划<br>取值范围：2times/h～1000times/h<br>系统初始设置值： 100times/h<br>说明：只有当<br>[**ADD SMARTACT**](../激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)<br>命令中的<br>“Parking APN假激活功能开关”<br>打开后，配置参数才有效。 |
| DETACHACTIVATIONTHRESH | 分离异常用户的激活行为门限（times/h） | 可选必选说明：可选参数<br>参数含义：该参数为主动分离用户的门限，即在一个小时内如果用户的激活次数超过了此参数的值，则进行网络侧分离。<br>数据来源：本端规划<br>取值范围：2times/h～1000times/h<br>系统初始设置值： 100times/h<br>说明：只有当<br>[**ADD SMARTACT**](../激活抑制规则管理/增加激活抑制规则（ADD SMARTACT）_72225421.md)<br>命令中的<br>“主动分离用户功能开关”<br>打开后，配置参数才有效。 |
| WAKEUPSWINSPECIALCAUSE | 特定原因值拒绝激活唤醒开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置<br>“特定原因值拒绝激活唤醒开关”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值： OFF(关)<br>配置原则：<br>- 当该开关开启时，SGSN在唤醒定时器即“抑制唤醒定时器(min)”超时后会执行唤醒用户的措施，即分离用户，分离类型为re-attach required。<br>- 当该开关关闭时，SGSN在唤醒定时器超时后不会执行唤醒用户的措施。 |
| WAKEUPSWINPARKING | Parking APN假激活唤醒开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置<br>“Parking APN假激活唤醒开关”<br>。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值： ON(开)<br>配置原则：<br>- 当该开关开启时，SGSN在唤醒定时器即“抑制唤醒定时器(min)”超时后会执行唤醒用户的措施，即去激活Parking APN的PDP。<br>- 当该开关关闭时，SGSN在唤醒定时器超时后不会执行唤醒用户的措施。 |

## 操作的配置对象

- [激活抑制参数（SMARTACTPARA）](configobject/UNC/20.15.2/SMARTACTPARA.md)

## 使用实例

设置激活抑制参数如下： “识别异常激活行为的门限” 设置为10， “抑制唤醒定时器（min）” 设置为60， “Parking APN” 设置为huawei1， “分离异常用户的SERVICE REQUEST门限（times/h）” 设置为50。

SET SMARTACTPARA: ABNORACTTHRESH=10, WAKEUPTIMER=60, PARKINGAPN="huawei1", DETACHSERVREQTHRESH=50;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置激活抑制参数（SET-SMARTACTPARA）_26305550.md`
