# 设置TCPIP报文以及应用层、黑名单、白名单防御机制使能（SET SECPOLICYSWITCH）

- [命令功能](#ZH-CN_CONCEPT_0000001550120854__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550120854__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550120854__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550120854__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550120854__1.3.5.1)
- [参考信息](#ZH-CN_CONCEPT_0000001550120854__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550120854)

该命令用于设置非法报文防御机制使能。

#### [注意事项](#ZH-CN_CONCEPT_0000001550120854)

- 该命令执行后立即生效。
- 该命令的设定值可通过LST SECPOLICYSWITCH命令进行查询。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550120854)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550120854)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：必选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：必选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- APP：应用策略。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”、“WhiteList”、“BlackList” 或 “APP”时为必选参数。<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：如果SECPOLICYTYPE选择APP，则本选项为0。 |
| SECPOLICYENABLE | 安全策略使能标记 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”、“WhiteList”、“BlackList” 或 “APP”时为必选参数。<br>参数含义：协议类型。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SUBTCPIPTYPE | TCP/IP防攻击类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。<br>参数含义：TCP/IP防攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABNORMAL：非法报文。<br>- UDPFLOOD：UDP泛洪报文。<br>- TCPSYN：TCPSYN报文。<br>- FRAGMENT：分片报文。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550120854)

设置非法报文防御机制使能：

```
SET SECPOLICYSWITCH: SECPOLICYID=1, SECPOLICYTYPE=Tcpip, SECPOLICYTYPEID=3, SECPOLICYENABLE=FALSE, SUBTCPIPTYPE=TCPSYN;
```

#### [参考信息](#ZH-CN_CONCEPT_0000001550120854)

需要先添加安全策略。
