---
id: UNC@20.15.2@MMLCommand@RMV USRN2CONN
type: MMLCommand
name: RMV USRN2CONN（删除N2接口AN信令连接）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRN2CONN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# RMV USRN2CONN（删除N2接口AN信令连接）

## 功能

![](删除N2接口AN信令连接（RMV USRN2CONN）_49644931.assets/notice_3.0-zh-cn_2.png)

执行本命令后将会导致指定用户的业务发生中断。

**适用NF：AMF**

该命令用于删除连接态用户的N2接口上的AN信令连接。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅对连接态用户生效。
- 执行该命令后会导致指定用户的业务发生中断，需要用户再次请求业务才能恢复。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRIDTYPE | 用户标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示待删除N2接口AN信令连接的用户的标识类型。<br>数据来源：本端规划<br>取值范围：<br>- “IMSI（IMSI）”：IMSI<br>- “MSISDN（MSISDN）”：MSISDN<br>- “GUTI（5G-GUTI）”：5G-GUTI<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"USRIDTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于表示待删除N2接口AN信令连接的用户的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"USRIDTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于表示待删除N2接口AN信令连接的用户的MSISDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| GUTI | GUTI | 可选必选说明：该参数在"USRIDTYPE"配置为"GUTI"时为条件必选参数。<br>参数含义：该参数用于表示待删除N2接口AN信令连接的用户的5G-GUTI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是19~20。5G-GUTI的组成为[MCC] + [MNC] + [AMF Region ID] + [AMF Set ID] + [AMF Pointer] + [5G-TMSI]，其中MCC为3个十进制数字，MNC为2-3个十进制数字；AMF Region ID、AMF Set ID和AMF Pointer合成AMF Identifier，使用十六进制（0-9，a-f，A-F）表示，占6个字符；5G-TMSI是AMF内的唯一标识，使用十六进制表示，占8个字符。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [N2接口AN信令连接（USRN2CONN）](configobject/UNC/20.15.2/USRN2CONN.md)

## 使用实例

在拨测场景下，为了让IMSI为123451234567890的用户快速回落到空闲态，执行如下命令：

```
RMV USRN2CONN: USRIDTYPE=IMSI, IMSI="123451234567890";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除N2接口AN信令连接（RMV-USRN2CONN）_49644931.md`
