---
id: UNC@20.15.2@MMLCommand@ADD IPSELPLCY
type: MMLCommand
name: ADD IPSELPLCY（增加IP地址选择策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPSELPLCY
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- IP地址选择策略
status: active
---

# ADD IPSELPLCY（增加IP地址选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于增加S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口的IP地址选择策略。

在IPv6改造过程中，可以针对整系统和用户粒度进行IP地址策略控制。

其中GU接口是指Gn/Gp接口，LTE接口是指S10、S11、S5/S8、S3、S4、Sv接口。

## 注意事项

- 此命令可配置的最大记录数为32。
- 该命令执行后立即生效。
- 该命令中LTE接口和GU接口需要独立配置，如果没有配置LTE接口，则S10、S11、S5/S8、S3、S4、S5、Sv接口按IPv4策略来选。如果没有配置GU接口，则Gn/Gp接口按IPv4策略来选。
- 当软参BYTE_EX_B26 BIT3–BIT4打开（设置为“1”，“2”，“3”）时，该命令不控制N26接口的IP地址选择策略，仅由此软参控制。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLRANGE | 控制范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定命令生效的范围。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(缺省策略)”<br>- “SPECIFY(指定IMSI)”<br>默认值：无<br>配置原则：<br>- “DEFAULT(缺省策略)”，即为S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口指定IP地址选择策略。<br>- “SPECIFY(指定IMSI)”是用户粒度的，主要在设备IPv6改造过程中，指定部分用户进行IPv6试验，而不影响原有用户使用IPv4。<br>说明：指定IMSI的配置记录优先级大于缺省配置记录。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>前提条件：该参数在<br>“CTRLRANGE(控制范围)”<br>设置为<br>“SPECIFY(指定IMSI)”<br>有效。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字<br>默认值：无 |
| IPPLCY | LTE接口本网IP地址选择策略 | 可选必选说明：必选参数<br>参数含义：该参数表示S10、S11、Sv、S3、S4、S5接口IP地址策略。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(仅使用IPv4地址)”<br>- “IPV6(仅使用IPv6地址)”<br>- “IPV6PRE(优先使用IPv6地址)”<br>默认值：无<br>配置原则：<br>- 在设备IPv6改造过程中，指定一些本网用户进行IPv6试验，则可使用“IPV6(仅使用IPv6地址)”。<br>- 在IPv4网络中，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，配置成“IPV6PRE(优先使用IPv6地址)”；IPv6网络改造完成后，配置成“IPV6(仅使用IPv6地址)”。<br>- 当软参BYTE_EX_B26 BIT3–BIT4打开（设置为“1”，“2”，“3”）时，该参数不控制N26接口的IP地址选择策略，仅由此软参控制。 |
| REMOTEIPPLCY | LTE接口漫游IP地址选择策略 | 可选必选说明：必选参数<br>参数含义：该参数表示S8接口IP地址选择策略。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(仅使用IPv4地址)”<br>- “IPV6(仅使用IPv6地址)”<br>- “IPV6PRE(优先使用IPv6地址)”<br>默认值：无<br>配置原则：<br>- 在设备IPv6改造过程中，指定一些漫游用户进行IPv6试验，则可使用“IPV6(仅使用IPv6地址)”。<br>- 在IPv4网络中，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，如果本网和外网之间IPv6改造没有完成，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，如果本网和外网之间IPv6改造完成，配置成“IPV6PRE(优先使用IPv6地址)”；IPv6网络改造完成后，配置成“IPV6(仅使用IPv6地址)”。<br>- 当软参BYTE_EX_B26 BIT3–BIT4打开（设置为“1”，“2”，“3”）时，该参数不控制N26接口的IP地址选择策略，仅由此软参控制。 |
| GUIPPLCY | GU接口本网IP地址选择策略 | 可选必选说明：必选参数<br>参数含义：该参数表示Gn接口IP地址选择策略。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(仅使用IPv4地址)”<br>- “IPV6(仅使用IPv6地址)”<br>- “IPV6PRE(优先使用IPv6地址)”<br>默认值：无<br>配置原则：<br>- 在设备IPv6改造过程中，指定一些本网用户进行IPv6试验，则可使用“IPV6(仅使用IPv6地址)”。<br>- 在IPv4网络中，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，配置成“IPV6PRE(优先使用IPv6地址)”；IPv6网络改造完成后，配置成“IPV6(仅使用IPv6地址)”。 |
| GUREMOTEIPPLCY | GU接口漫游IP地址选择策略 | 可选必选说明：必选参数<br>参数含义：该参数表示Gp接口IP地址选择策略。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(仅使用IPv4地址)”<br>- “IPV6(仅使用IPv6地址)”<br>- “IPV6PRE(优先使用IPv6地址)”<br>默认值：无<br>配置原则：<br>- 在设备IPv6改造过程中，指定一些漫游用户进行IPv6试验，则可使用“IPV6(仅使用IPv6地址)”。<br>- 在IPv4网络中，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，如果本网和外网之间IPv6改造没有完成，配置成“IPV4(仅使用IPv4地址)”；在IPv4向IPv6改造过程中，如果本网和外网之间IPv6改造完成，配置成“IPV6PRE(优先使用IPv6地址)”；IPv6网络改造完成后，配置成“IPV6(仅使用IPv6地址)”。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述对象属性、配置原因、背景，以便在查询时能够清晰地区分大量配置数据。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：noname |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPSELPLCY]] · IP地址选择策略（IPSELPLCY）

## 使用实例

1. 增加记录，控制范围为“DEFAULT”，LTE接口本网IP地址选择策略为“IPV4”，LTE接口漫游IP地址选择策略为“IPV4”，GU接口本网IP地址选择策略为“IPV4”，GU接口漫游IP地址选择策略为“IPV4”：
  ```
   ADD IPSELPLCY: CTRLRANGE=DEFAULT,IPPLCY=IPV4,REMOTEIPPLCY=IPV4,GUIPPLCY=IPV4,GUREMOTEIPPLCY=IPV4;
  ```
2. 增加记录，控制范围为“SPECIFY”，IMSI为"123031501000001"，LTE接口本网IP地址选择策略为“IPV6”，LTE接口漫游IP地址选择策略为“IPV4”，GU接口本网IP地址选择策略为“IPV6”，GU接口漫游IP地址选择策略为“IPV4”：
  ```
   ADD IPSELPLCY: CTRLRANGE=SPECIFY, IMSI="123031501000001",IPPLCY=IPV6,REMOTEIPPLCY=IPV4,GUIPPLCY=IPV6,GUREMOTEIPPLCY=IPV4;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IPSELPLCY.md`
