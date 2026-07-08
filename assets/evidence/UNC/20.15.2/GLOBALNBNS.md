# 设置系统默认NBNS（SET GLOBALNBNS）

- [命令功能](#ZH-CN_MMLREF_0000001176878558__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001176878558__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001176878558__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001176878558__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001176878558)

**适用NF：PGW-C、SMF、GGSN**

该命令用来配置系统的NBNS（NetBIOS Name Server）属性。

## [注意事项](#ZH-CN_MMLREF_0000001176878558)

- 该命令执行后立即生效。

- 若系统中已配置系统的NBNS，执行本命令为修改已配置的系统NBNS。
- 该配置需要和网络规划一致，否则可能会导致通过NetBIOS协议通信的主机无法获取NetBIOS名字到IP地址的解析。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NBNSSWITCH | MNBNSSERVER | BNBNSSERVER | FIRSTMODE | SECONDMODE | THIRDMODE |
| --- | --- | --- | --- | --- | --- |
| DISABLE | 0.0.0.0 | 0.0.0.0 | DHCP | RADIUS | LOCAL |

#### [操作用户权限](#ZH-CN_MMLREF_0000001176878558)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001176878558)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NBNSSWITCH | NBNS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否使能NBNS功能。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |
| MNBNSSERVER | 主NBNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于指定主NBNS服务器IP。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制IPv4地址，仅支持A，B，C类IP。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |
| BNBNSSERVER | 备NBNS服务器IP | 可选必选说明：可选参数<br>参数含义：该参数用于指定备NBNS服务器IP。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制IPv4地址，仅支持A，B，C类IP。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |
| FIRSTMODE | 第一优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第一优先级属性。<br>数据来源：全网规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的NBNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的NBNS属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |
| SECONDMODE | 第二优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第二优先级属性。<br>数据来源：全网规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的NBNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的NBNS属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |
| THIRDMODE | 第三优先级服务器属性 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4第三优先级属性。<br>数据来源：全网规划<br>取值范围：<br>- “LOCAL（local）”：指定本地配置优先。<br>- “RADIUS（radius）”：指定RADIUS服务器返回的NBNS属性优先。<br>- “DHCP（dhcp）”：指定DHCP服务器返回的NBNS属性优先。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALNBNS查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001176878558)

设置系统NBNS属性的主备NBNS IP地址：

```
SET GLOBALNBNS: MNBNSSERVER="10.1.1.1", BNBNSSERVER="10.2.2.2";
```
