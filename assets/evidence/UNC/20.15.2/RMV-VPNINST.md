# 删除VPN实例（RMV VPNINST）

- [命令功能](#ZH-CN_MMLREF_0209651424__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651424__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651424__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651424__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651424)

![](删除VPN实例（RMV VPNINST）_09651424.assets/notice_3.0-zh-cn_2.png)

此操作会去中断业务，请确认与该VPN相关的配置已经删除，比如逻辑接口、IPSQMSHAPING、跟踪重定向等配置。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除指定的VPN实例。

## [注意事项](#ZH-CN_MMLREF_0209651424)

- 该命令执行后立即生效。

- “_public_”是公网缺省VPN的实例名，不允许用户删除。
- 删除的VPN实例必须为已经创建的VPN实例名称。
- 执行RMV VPNINST前，需要执行LST LOGICINF、LST PCRF、LST OCS、LST DRA、LST RDSSVR、LST SCTPASSOC、LST ADDRPOOL、LST BLACKLIST、LST APN、LST DHCPSERVERGRP命令检查要被删除的VPN实例是否被某个对象绑定。当要被删除的VPN实例被其中一个对象绑定时，VPN实例不能被删除。

#### [操作用户权限](#ZH-CN_MMLREF_0209651424)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651424)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651424)

删除VPNInst业务配置，VPN实例名称为vpn1：

```
RMV VPNINST:VPNINSTANCE="vpn1";
```
