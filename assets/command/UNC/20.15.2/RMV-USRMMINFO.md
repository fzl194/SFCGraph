---
id: UNC@20.15.2@MMLCommand@RMV USRMMINFO
type: MMLCommand
name: RMV USRMMINFO（删除网络名称）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRMMINFO
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
- 网络管理
- 归属网络运营商管理
- 网络名称管理
status: active
---

# RMV USRMMINFO（删除网络名称）

## 功能

**适用网元：SGSN、MME**

该命令用于删除指定号段用户运营商网络名称。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI，通过该IMSI确定需删除的<br>“IMSI_RANGE(指定IMSI范围)”<br>记录。该IMSI可为待删除<br>“IMSI_RANGE(指定IMSI范围)”<br>内的任意IMSI。<br>前提条件：只有<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，该参数才有效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |
| PLMNPLCY | PLMN匹配策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在给UE下发网络名称时，是否匹配无线侧PLMN，无线侧是多个运营商等场景下，一般需要根据无线侧PLMN给UE下发不同的网络名称，此时配置该参数为YES。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：<br>“NO(否)” |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动国家号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动网号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRMMINFO]] · 网络名称（USRMMINFO）

## 使用实例

- 删除IMSI为“123456”，无线侧PLMN为40101的用户网络名称配置：
  ```
  RMV USRMMINFO: SUBRANGE=IMSI_RANGE, IMSI="123456", PLMNPLCY=YES, MCC="401", MNC="01";
  ```
- 删除IMSI为“123456”用户的网络名称配置：
  ```
  RMV USRMMINFO: SUBRANGE=IMSI_RANGE, IMSI="123456", PLMNPLCY=NO;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-USRMMINFO.md`
