# 恢复IKE安全联盟（RTR IKESA）

- [命令功能](#ZH-CN_MMLREF_0000001180592514__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001180592514__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001180592514__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001180592514__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001180592514)

![](恢复IKE安全联盟（RTR IKESA）_80592514.assets/notice_3.0-zh-cn.png)

恢复IKE安全联盟后，IKE安全联盟会重新协商，会导致业务短时间中断。

该命令用于恢复IKE安全联盟。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001180592514)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001180592514)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：清除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。 all：指定IP版本的所有安全联盟。 connId：指定IP版本的连接ID。 remAddr：指定IP版本的远端地址。<br>- “All（所有）”：所有<br>- “ConnId（连接ID）”：连接ID<br>- “RemAddr（远端地址）”：远端地址<br>默认值：无<br>配置原则：<br>必选参数。 |
| CONNECTIONID | 连接ID | 可选必选说明：该参数在"RESETTYPE"配置为"ConnId"时为条件必选参数。<br>参数含义：连接ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 远端地址IP版本 | 可选必选说明：可选参数<br>参数含义：IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。IPv4或IPv6。<br>- “IPv4（远端地址格式为IPv4）”：远端地址格式为IPv4<br>- “IPv6（远端地址格式为IPv6）”：远端地址格式为IPv6<br>默认值：IPv4<br>配置原则：<br>必选参数。 |
| REMOTEADDR | 远端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| REMOTEADDR6 | 远端地址IPv6 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：IPv6远端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。字符串类型，输入长度范围为0～63。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“all”、“connId” 或 “remAddr”时为可选参数。 |

## [使用实例](#ZH-CN_MMLREF_0000001180592514)

恢复Connection ID为1，IP协议版本为IPv4，的IKE SA：

```
RTR IKESA:RESETTYPE=ConnId,CONNECTIONID=1,IPVERSION=IPv4;
```
