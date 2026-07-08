---
id: UNC@20.15.2@MMLCommand@RMV NONIPSUBCTRL
type: MMLCommand
name: RMV NONIPSUBCTRL（删除Non-IP APNNI配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NONIPSUBCTRL
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- Non-IP APNNI配置
status: active
---

# RMV NONIPSUBCTRL（删除Non-IP APNNI配置）

## 功能

**适用网元：MME**

该命令用于删除Non-IP APNNI配置。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX”<br>时，该参数才有效。<br>数据来源：全网规划<br>取值范围：1～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [Non-IP APNNI配置（NONIPSUBCTRL）](configobject/UNC/20.15.2/NONIPSUBCTRL.md)

## 使用实例

删除一条SUBRANGE为IMSI_PERFIX，IMSI前缀为“123038101”的Non-IP APNNI配置记录：

RMV NONIPSUBCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="123038101";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Non-IP-APNNI配置(RMV-NONIPSUBCTRL)_26305582.md`
