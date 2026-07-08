---
id: UNC@20.15.2@MMLCommand@RMV APNNICHARACT
type: MMLCommand
name: RMV APNNICHARACT（删除APNNI属性配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNICHARACT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- APNNI属性
status: active
---

# RMV APNNICHARACT（删除APNNI属性配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于删除在非活动用户分离流程中需要进行特殊处理的APN NI（Network Identifier）属性记录。APN NI（Network Identifier）是APN中的必选部分，用于标识需要接入的外部数据网络的类型。APN NI需要在HLR中进行了签约，激活时才允许使用该APN NI。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，对应签约APN NI的用户在进行非活动用户分离流程中就不再有特殊处理，而是按照系统规定的非活动用户分离流程进行。
- 该命令的删除对其他非签约该APN NI的用户没有影响。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：APN网络标识。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>- APN网络标识不区分大小写。<br>- APNNI在APN中所处的位置，例如：huawei1.com.mnc.mcc.gprs，其中NI= huawei1.com，OI= mnc.mcc.gprs。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNNICHARACT]] · APNNI属性配置信息（APNNICHARACT）

## 使用实例

删除APN NI为 “huawei.com” 的APNNI属性信息：

RMV APNNICHARACT: APNNI="huawei.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除APNNI属性配置信息(RMV-APNNICHARACT)_26145670.md`
