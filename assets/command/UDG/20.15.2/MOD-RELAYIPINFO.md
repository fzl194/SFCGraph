---
id: UDG@20.15.2@MMLCommand@MOD RELAYIPINFO
type: MMLCommand
name: MOD RELAYIPINFO（修改媒体中继IP信息）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: RELAYIPINFO
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继IP地址信息
status: active
---

# MOD RELAYIPINFO（修改媒体中继IP信息）

## 功能

**适用NF：PGW-U、UPF**

![](修改媒体中继IP信息（MOD RELAYIPINFO）_14541479.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改该配置后，可能会导致媒体中继业务中断。

该命令用于修改媒体中继IP信息。

## 注意事项

- 该命令执行后立即生效。
- 当需要删除媒体中继IP时，可以通过输入0.0.0.0或0::0进行删除。不支持同时删除IPv4地址和IPv6地址。
- 媒体中继的IP地址需要统一规划，不能与终端用户地址重复，不能与已配置的媒体中继IP地址重复。
- 不支持配置VPN和IP地址都相同的记录。
- IPv6地址目前不支持配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RELAYIPNAME | 媒体中继IP地址名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示媒体中继服务IP配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPSERVICETYPE | IP业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IP业务类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GROUPIP：表示填写的IP地址是组级IP。<br>- REDIRECTIP：表示填写的IP地址是重定向IP。<br>默认值：GROUPIP<br>配置原则：无 |
| INSTID | 实例ID | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPSERVICETYPE”配置为“REDIRECTIP”时为必选参数。<br>参数含义：该参数用于表示实例ID。<br>数据来源：本端规划<br>取值范围：对应RelayPodID(0~15)。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示实例的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。不支持255.255.255.255。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示实例的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。不支持全F。<br>默认值：无<br>配置原则：无 |
| VPNINSTANCE | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 绑定VPN时需要确保该VPN已经配置（ADD VPNINST）。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RELAYIPINFO]] · 媒体中继IP信息（RELAYIPINFO）

## 使用实例

修改媒体中继IP信息，媒体中继服务IP配置为test，IP业务类型为组级，将IPv4地址修改为192.168.1.1：

```
MOD RELAYIPINFO: RELAYIPNAME="test", IPSERVICETYPE=GROUPIP, IPV4ADDR="192.168.1.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-RELAYIPINFO.md`
