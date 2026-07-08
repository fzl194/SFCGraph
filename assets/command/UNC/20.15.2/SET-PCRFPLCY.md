---
id: UNC@20.15.2@MMLCommand@SET PCRFPLCY
type: MMLCommand
name: SET PCRFPLCY（设置PCRF策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCRFPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- PCRF策略管理
status: active
---

# SET PCRFPLCY（设置PCRF策略）

## 功能

**适用网元：MME**

该命令用于在PCRF签约NI和RFSP时，开启动态NI功能或灵活选频功能并设置相关策略。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DYNRFSPSW | 灵活选频功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否开启灵活选频功能。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：NO（否）。<br>配置原则：该功能需要和SGW/PGW/PCRF配合使用。 |
| DFTRFSP | 默认RFSP | 可选必选说明：条件可选参数。<br>参数含义：该参数用于设置PCRF签约的RFSP被清除后，MME给基站下发的RFSP。<br>前提条件：该参数在“灵活选频功能开关”参数配置为“YES”后生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~256。<br>默认值：0<br>配置原则：<br>- HSS签约数据或者<br>[ADD RFSP](../../移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/增加RFSP配置(ADD RFSP)_26305350.md)<br>配置的RFSP决策结果优先该参数配置。<br>- 取0时，该参数是无效值。<br>- 1~128为运营商自定义值。<br>- 129~256为协议(3GPP TS 36.300)指定值，其中256表示的优先级从高到低为：E-UTRAN，UTRAN，GERAN。255表示的优先级从高到低为：UTRAN，GERAN，E-UTRAN。254表示的优先级从高到低为：GERAN，UTRAN，E-UTRAN。 |
| PEERRFSPPLCY | 是否使用对等口RFSP | 可选必选说明：条件可选参数。<br>参数含义：该参数用于设置新侧MME从N26/S10接口收到老侧AMF/MME在PCF/PCRF上签约的RFSP之后，是否使用该数据。<br>前提条件：该参数在“灵活选频功能开关”参数配置为“YES”后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：NO（否）。<br>配置原则：<br>当5G系统规划的RFSP和4G系统规划的不一致时，不能开启。<br>说明：使用场景：当PGW和PCRF对接不采用Gx接口时，用户无法获取PCRF上的RFSP策略，但是AMF可以通过N15接口获取PCF上签约的RFSP策略，如果客户45G规划的RFSP通用，且希望MME上也使用PCF签约的RFSP时，可打开该开关。 |
| DYNNISW | 是否开启动态NI功能 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否开启动态NI功能。此功能对应基于PCRF的动态UE Logo下发功能。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：NO（否）。<br>配置原则：该功能需要和SGW/PGW/PCRF配合使用。 |
| FULLNAME | 运营商全称 | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定移动网络运营商的全称。<br>前提条件：该参数在“是否开启动态NI功能”参数配置为“YES”后生效。<br>数据来源：全网规划<br>取值范围：0～79位字符串。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无。<br>说明：- PCRF取消动态NI时，当配置本参数时，优先使用该参数填充EMM information消息中携带的“Full name for network”信元值；当未配置本参数时，信元取值优先级如下：ADD AREAMMINFO>ADD USRMMINFO>ADD MVNO或ADD MNO。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商全称不能输入“NULL”。 |
| SHORTNAME | 运营商简称 | 可选必选说明：条件可选参数。<br>参数含义：该参数用于指定移动网络运营商的全称。<br>前提条件：该参数在“是否开启动态NI功能”参数配置为“YES”后生效。<br>数据来源：全网规划<br>取值范围：0～79位字符串。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。<br>默认值：无。<br>说明：- 当配置了本参数，PCRF取消动态NI时，优先使用该参数填充EMM information消息中携带的“Short name for network”信元值；当未配置本参数时，信元取值优先级如下：ADD AREAMMINFO>ADD USRMMINFO>ADD MVNO或ADD MNO。<br>- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。<br>- 运营商简称不能输入“NULL”。 |
| PEERNIPLCY | 是否使用对等口NI | 可选必选说明：条件可选参数。<br>参数含义：该参数用于设置新侧MME从N26/S10接口收到老侧AMF/MME在PCF/PCRF上签约的NI之后，是否使用该数据。<br>前提条件：该参数在“是否开启动态NI功能”参数配置为“YES”后生效。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”<br>- “YES（是）”<br>默认值：NO（否）。<br>配置原则：<br>- 当5G系统规划的NI和4G系统规划的不一致时，不能开启。<br>- 当NI策略不是基于整系统配置时（如：基于区域等），不能开启。<br>说明：使用场景：当PGW和PCRF对接不采用Gx接口时，用户无法获取PCRF上的NI策略，但是AMF可以通过N15接口获取PCF上签约的NI策略，如果客户45G规划的NI通用，且希望MME上也使用PCF签约的NI时，可打开该开关。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFPLCY]] · PCRF策略（PCRFPLCY）

## 使用实例

设置PCRF策略，开启灵活选频功能，默认RFSP设置为1，开启动态NI功能，运营商全称为aaa，运营商简称为a执行如下命令：

SET PCRFPLCY: DYNRFSPSW=YES, DFTRFSP=1, PEERRFSPPLCY=YES, DYNNISW=YES, FULLNAME="aaa", SHORTNAME="a", PEERNIPLCY=NO;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PCRFPLCY.md`
