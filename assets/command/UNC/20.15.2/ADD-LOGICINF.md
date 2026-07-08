---
id: UNC@20.15.2@MMLCommand@ADD LOGICINF
type: MMLCommand
name: ADD LOGICINF（增加逻辑接口）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOGICINF
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 逻辑接口
status: active
---

# ADD LOGICINF（增加逻辑接口）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于创建指定的逻辑接口。逻辑接口是指能够实现数据交换功能但物理上不存在，需要通过配置建立的接口。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 如果需要输入该命令的可选参数VPN实例名称（即逻辑接口与VPN绑定），则需要提前配置ADD VPNINST命令。如果用户没有对VPN实例进行配置，系统将会下发缺省VPN。
- 逻辑接口配置不支持在主备SMF之间自动同步，需要在主备SMF上分别配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置逻辑接口名称，确保逻辑接口的唯一性。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 字符串形式，用户输入形式例如：giif1/0/0。其中giif为逻辑接口类型；1/0/0中第一个数字为组号，第二个数字为实例类型；第三个数字为逻辑接口号，各逻辑接口类型有各自的配置范围。<br>- 逻辑接口类型：giif，gaif，gyif，gxif，s6bif。<br>- 组号：1。<br>- 实例类型：0。0表示组级类型。<br>- 逻辑接口号： giif：0~1023，gaif：0~4，gyif：0~15，gxif：0~63，s6bif：0~1。 |
| IPVERSION | 逻辑接口的IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于用户指定IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：添加逻辑接口IP的版本为IPv4。<br>- IPV6：添加逻辑接口IP的版本为IPv6。<br>- IPVER_ALL：添加逻辑接口IP的版本为IPv4和IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS1 | 逻辑接口的IPv4地址1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于指示逻辑接口配置主IP。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：<br>- 根据环境的网络规划进行配置，点分十进制格式。除A、B、C类地址合法外，其余都为非法地址。<br>- 该参数使用ADD LOGICIP命令配置生成。 |
| IPV4MASK1 | 逻辑接口的IPv4掩码1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于指示逻辑接口配置主IP掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：逻辑口IP地址的掩码为32位。 |
| IPV4ADDRESS2 | 逻辑接口的IPv4地址2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPVER_ALL”时为可选参数。<br>参数含义：该参数用于指示逻辑接口配置子IP。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：<br>- 根据环境的网络规划进行配置，点分十进制格式。只有在逻辑接口为gxif、gyif和s6bif时使用。除A、B、C类地址合法外，其余都为非法地址。<br>- 该参数使用ADD LOGICIP命令配置生成。<br>- 不配置此参数时值默认为0.0.0.0。 |
| IPV4MASK2 | 逻辑接口的IPv4掩码2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4” 或 “IPVER_ALL”时为可选参数。<br>参数含义：该参数用于指示逻辑接口配置子IP掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：<br>- 逻辑口IP地址的掩码为32位。只有在逻辑接口为gxif、gyif和s6bif时使用。<br>- 不配置此参数时值默认为0.0.0.0。 |
| IPV6ADDRESS1 | 逻辑接口的IPv6地址1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：<br>- 根据环境的网络规划进行配置，冒号分十六进制格式。除单播、任播和组播地址合法外，其余都为非法地址。<br>- 该参数使用ADD LOGICIP命令配置生成。 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”、“IPVER_ALL” 或 “IPV6”时为可选参数。<br>参数含义：该参数用于将逻辑接口与VPN绑定。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。 |
| IPV6PREFIXLEN1 | IPv6前缀长度1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPVER_ALL”时为必选参数。<br>参数含义：该参数用于指示逻辑接口配置的主IPv6前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为128。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS2 | 逻辑接口的IPv6地址2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPVER_ALL”时为可选参数。<br>参数含义：该参数用于指示逻辑接口配置子IPV6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：<br>- 根据环境的网络规划进行配置，冒号分十六进制格式。除单播、任播和组播地址合法外，其余都为非法地址。<br>- 该参数使用ADD LOGICIP命令配置生成。<br>- 不配置此参数时值默认为::。 |
| IPV6PREFIXLEN2 | IPv6前缀长度2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6” 或 “IPVER_ALL”时为可选参数。<br>参数含义：该参数用于指示逻辑接口配置的子IPv6前缀长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为128。<br>默认值：无<br>配置原则：<br>- 逻辑口IPv6前缀长度为128。<br>- 不配置此参数时值默认为0。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOGICINF]] · 逻辑接口（LOGICINF）

## 使用实例

配置逻辑接口，逻辑接口名称为gxif1/0/1，逻辑接口的IPv6地址1为FC12:1233:4567:9821:23:0:2561:2664，VPN实例名称为vpn1，IPv6前缀长度1为128，逻辑接口的Ipv6地址2为FC65:7890:455:0:0:0:0:125，IPv6前缀长度2为128：

```
ADD LOGICINF: NAME="gxif1/0/0", IPVERSION=IPV6, IPV6ADDRESS1="FC12:1233:4567:9821:23:0:2561:2664", VPNINSTANCE="vpn1", IPV6PREFIXLEN1=128, IPV6ADDRESS2="FC65:7890:455:0:0:0:0:125", IPV6PREFIXLEN2=128;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LOGICINF.md`
