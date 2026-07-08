---
id: UNC@20.15.2@MMLCommand@RMV SMFDIALTEST
type: MMLCommand
name: RMV SMFDIALTEST（删除SMF拨测用户配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFDIALTEST
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
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

# RMV SMFDIALTEST（删除SMF拨测用户配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于删除一组拨测用户的配置。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 本命令的起始IMSI/MSISDN必须和LST SMFDIALTEST命令查询到的起始IMSI/MSISDN一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TSTUSRRANGE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置拨测用户类型。<br>数据来源：本端规划<br>取值范围：<br>- MSISDN（MSISDN）<br>- IMSI（IMSI）<br>默认值：无<br>配置原则：无 |
| BEGINMSISDN | 起始MSISDN | 可选必选说明：该参数在"TSTUSRRANGE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“MSISDN(MSISDN)”后生效。 |
| BEGINIMSI | 起始IMSI | 可选必选说明：该参数在"TSTUSRRANGE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于配置拨测用户的起始IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：<br>该参数在“用户标识类型”参数配置为“IMSI(IMSI)”后生效。 |

## 操作的配置对象

- [SMF拨测用户配置（SMFDIALTEST）](configobject/UNC/20.15.2/SMFDIALTEST.md)

## 使用实例

删除一条拨测用户配置，起始IMSI为460001111111111。

```
RMV SMFDIALTEST: TSTUSRRANGE=IMSI, BEGINIMSI="460001111111111";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMF拨测用户配置（RMV-SMFDIALTEST）_70462613.md`
