---
id: UNC@20.15.2@MMLCommand@RMV IMSIHLRHSS
type: MMLCommand
name: RMV IMSIHLRHSS（删除IMSI对应的HLR/HSS接口）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMSIHLRHSS
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
- 签约数据管理
- 接口选择
status: active
---

# RMV IMSIHLRHSS（删除IMSI对应的HLR/HSS接口）

## 功能

**适用网元：SGSN、MME**

此命令用于删除IMSI对应的HLR/HSS接口。

## 注意事项

- 此命令执行后立即生效。
- 此命令执行后可能会导致对应IMSI范围的用户无法附着，已经附着的用户不会受影响/被分离。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIRANGE | IMSI范围 | 可选必选说明：必选参数<br>参数含义：待删除的IMSI范围信息。<br>取值范围：<br>- “ALL IMSI(所有IMSI)”：表示该指定IMSI范围为所有IMSI。<br>- “SPECIAL IMSI(指定IMSI)”：表示该指定IMSI范围为指定IMSI。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：待删除的IMSI前缀。<br>前提条件：当<br>“IMSIRANGE(IMSI范围)”<br>设置为<br>“SPECIAL IMSI(指定IMSI)”<br>时生效。<br>取值范围：5～15位数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIHLRHSS]] · IMSI对应的HLR/HSS接口（IMSIHLRHSS）

## 使用实例

删除一条IMSI范围为SPECIAL_IMSI，IMSI前缀为123456的记录：

RMV IMSIHLRHSS: IMSIRANGE=SPECIAL_IMSI, IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-IMSIHLRHSS.md`
