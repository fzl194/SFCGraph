---
id: UNC@20.15.2@MMLCommand@RMV ISSUDIALTEST
type: MMLCommand
name: RMV ISSUDIALTEST（删除拨测用户配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ISSUDIALTEST
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 灰度升级
- 拨测管理
status: active
---

# RMV ISSUDIALTEST（删除拨测用户配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一组拨测用户的配置。

## 注意事项

- 配置删除后，对应的拨测用户会逐步通过先分离再重新接入的方式迁移到老侧USN_VNFC。
- 本命令的起始IMSI/MSISDN必须和[**LST ISSUDIALTEST**](查询拨测用户配置(LST ISSUDIALTEST)_26146122.md)命令查询到的起始IMSI/MSISDN一致。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUSRRANGE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户范围。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- “MSISDN(MSISDN)”<br>- “IMSI(IMSI)”<br>默认值：无 |
| BEGMSISDN | 起始MSISDN | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置拨测用户的起始MSISDN。<br>前提条件：该参数在<br>“用户标识类型”<br>参数配置为<br>“MSISDN(MSISDN)”<br>后生效。<br>数据来源：本端规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>前提条件：该参数在<br>“用户标识类型”<br>参数配置为<br>“IMSI(IMSI)”<br>后生效。<br>数据来源：本端规划<br>取值范围：6～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [拨测用户配置（ISSUDIALTEST）](configobject/UNC/20.15.2/ISSUDIALTEST.md)

## 使用实例

删除一条拨测用户配置，起始IMSI为123001111111111。

RMV ISSUDIALTEST: TSTUSRRANGE=IMSI, BEGIMSI="123001111111111";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除拨测用户配置(RMV-ISSUDIALTEST)_72345721.md`
