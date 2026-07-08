---
id: UNC@20.15.2@MMLCommand@ADD PUBLICAPNNI
type: MMLCommand
name: ADD PUBLICAPNNI（增加公共APN NI配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PUBLICAPNNI
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 128
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 公共APNNI管理
status: active
---

# ADD PUBLICAPNNI（增加公共APN NI配置）

## 功能

**适用网元：SGSN、MME**

该命令用于配置公用APN NI(Access Point Name Network Identifier)信息，公用APN NI信息在激活请求信息纠正功能时使用。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为128。
- 关联配置：[**ADD SMACTCTRL**](../激活过程管理/增加激活过程控制参数（ADD SMACTCTRL）_26305472.md)用于配置激活请求信息纠正功能涉及到的相关参数。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：APN网络标识。<br>数据来源：整网规划<br>取值范围：1～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。<br>说明：各记录APN NI字段不能重复。 |

## 操作的配置对象

- [公共APN NI配置（PUBLICAPNNI）](configobject/UNC/20.15.2/PUBLICAPNNI.md)

## 使用实例

配置一条记录，增加APN NI为“cmwap”的APN网络标识为公用APN：

ADD PUBLICAPNNI: APNNI="cmwap";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加公共APN-NI配置(ADD-PUBLICAPNNI)_26145682.md`
