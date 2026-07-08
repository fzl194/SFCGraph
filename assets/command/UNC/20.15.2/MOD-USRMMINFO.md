---
id: UNC@20.15.2@MMLCommand@MOD USRMMINFO
type: MMLCommand
name: MOD USRMMINFO（修改网络名称）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD USRMMINFO（修改网络名称）

## 功能

**适用网元：SGSN、MME**

该命令用于修改运营商网络名称。在UE接入 UNC 时，如果需要给UE下发网络名称， UNC 判断UE在本命令配置的用户范围，则优选下发本命令配置的网络名称。

## 注意事项

- 该命令执行后立即生效。
- 对于4G网络，该命令配置的网络名称在EMM information信元中是否携带由命令[**SET MMFUNC**](../../../移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)中的参数“EMMINFOIEPLY”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无<br>说明：“IMSI_PREFIX（指定IMSI前缀）”<br>和<br>“IMSI_RANGE（指定IMSI范围）”<br>取值对应的记录不能同时存在。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无 |
| BEGIMSI | 起始IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定起始IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：参见<br>“ENDIMSI（终止IMSI）”<br>说明。 |
| ENDIMSI | 终止IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定终止IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1～15位十进制数字<br>默认值：无<br>说明：- 输入的起始IMSI必须小于或者等于终止IMSI。只有输入IMSI长度等于系统规定长度时，起始IMSI才能等于终止IMSI。<br>- 判断起始IMSI和终止IMSI大小的原则是：对于输入IMSI的长度小于系统规定IMSI长度时，将该IMSI补足0到规定长度后进行大小比较。 |
| PLMNPLCY | PLMN匹配策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在给UE下发网络名称时，是否匹配无线侧PLMN，无线侧是多个运营商等场景下，一般需要根据无线侧PLMN给UE下发不同的网络名称，此时配置该参数为YES。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动国家号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定无线侧PLMN的移动网号码。<br>前提条件：该参数在<br>“PLMN匹配策略”<br>参数配置为<br>“YES(是)”<br>后生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>说明：该参数仅对WB-E-UTRAN、NB-IoT用户生效。 |
| FULLNAME | 运营商全称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商全称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Full name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商全称不能输入“NULL”，字母不区分大小写。 |
| SHORTNAME | 运营商简称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商简称。<br>数据来源：整网规划<br>取值范围：0～79位字符串，数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符<br>默认值：无<br>说明：- GMM information/EMM information消息中携带的“Short name for network”信元值来源于该参数。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商简称不能输入“NULL”，字母不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRMMINFO]] · 网络名称（USRMMINFO）

## 使用实例

- 修改IMSI范围为“123456”~“123457”，无线侧PLMN为40101的用户的网络名称配置：“运营商全称”为“bbb”，“运营商简称”为“b”：
  ```
  MOD USRMMINFO: SUBRANGE=IMSI_RANGE, BEGIMSI="123456", ENDIMSI="123457", PLMNPLCY=YES, MCC="401", MNC="01", FULLNAME="bbb", SHORTNAME="b";
  ```
- 修改IMSI范围为“123456”~“123457”用户的网络名称配置：“运营商全称”为“bbb”，“运营商简称”为“b”：
  ```
  MOD USRMMINFO: SUBRANGE=IMSI_RANGE, BEGIMSI="123456", ENDIMSI="123457", FULLNAME="bbb", SHORTNAME="b";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改网络名称(MOD-USRMMINFO)_26305868.md`
