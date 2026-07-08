---
id: UNC@20.15.2@MMLCommand@ADD LOCALNRI
type: MMLCommand
name: ADD LOCALNRI（增加本局NRI配置信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCALNRI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- 本局NRI配置
status: active
---

# ADD LOCALNRI（增加本局NRI配置信息）

## 功能

**适用网元：SGSN**

当使用Iu-flex功能时，需要配置SGSN的NRI，该命令用于配置本SGSN的NRI属性。Iu-flex指一个RAN连接同一个功能域（CS或者PS）的多个CN节点的功能。Iu-flex新增的功能包括：RAN节点的消息路由功能；各个CN节点的负载平衡功能；缺省SGSN功能；后向兼容的功能等。系统开启Iu-flex功能，当发生附着或者路由区更新流程时，本SGSN可以根据P-TMSI中的NRI是否在本表中来确定是否为Inter流程。关于Iu-flex功能描述，请参考3GPP协议23.236。

## 注意事项

- 本命令执行后立即生效。
- 在本UNC执行SGSN Pool用户迁移的过程中，请不要执行本命令，否则会导致用户无法平滑地迁移到其它SGSN中。
- NRI值，或NRI起始值与长度构成的取值范围不能超过或者等于2<sup>NRI长度</sup>。
- POOLID、NRI起始值唯一才能确定一条记录。
- 该表最大记录数为32条。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于POOL区标识。<br>数据来源：整网规划<br>取值范围：0～4095<br>默认值：无 |
| NRIVBGN | NRI起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置NRI起始值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>数据来源：整网规划<br>取值范围：0～1023<br>默认值：无<br>说明：- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。<br>- 若POOL表的NRI长度为10，则LOCALNRI表的NRI个数必须大于等于4， NRI起始值小于等于1020。 |
| NRINUM | NRI个数 | 可选必选说明：必选参数<br>参数含义：该参数用于SGSN最少需要配置的NRI的个数。<br>数据来源：整网规划<br>取值范围：1～64<br>默认值：无<br>说明：- “NRI个数”的取值只与[**ADD POOL**](../POOL区配置/增加POOL配置信息(ADD POOL)_72225781.md)命令的“NRI长度”参数有关。详情请见[表1](#ZH-CN_MMLREF_0000001172345699__tab2)。<br>- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。 |
| STATE | NRI状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定NRI的状态。<br>数据来源：整网规划<br>取值范围：<br>- “UNBLOCKED(UNBLOCKED)”<br>- “BLOCKED(BLOCKED)”<br>默认值：<br>“UNBLOCKED(UNBLOCKED)”<br>说明：当NRI处于<br>“UNBLOCKED(UNBLOCKED)”<br>状态时，SGSN在新分配PTMSI时将使用NRI值；当NRI处于<br>“BLOCKED(BLOCKED)”<br>状态时，SGSN在新分配PTMSI时将不使用BLOCKED状态的NRI值，但是可以正确识别该NRI值为本局NRI。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALNRI]] · 本局NRI配置信息（LOCALNRI）

## 使用实例

增加一条POOLID为1，NRI的值为10，NRI个数为1，NRI状态为UNBLOCKED的本局NRI配置信息：

ADD LOCALNRI: POOLID=1, NRIVBGN=10, NRINUM=1, STATE=UNBLOCKED;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加本局NRI配置信息(ADD-LOCALNRI)_72345699.md`
