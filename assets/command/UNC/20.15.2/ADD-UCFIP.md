---
id: UNC@20.15.2@MMLCommand@ADD UCFIP
type: MMLCommand
name: ADD UCFIP（配置UCF报表本地IP资源池）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UCFIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF本地IP
status: active
---

# ADD UCFIP（配置UCF报表本地IP资源池）

## 功能

该命令用于添加UCF报表本地IP资源池。

## 注意事项

- 该命令执行后立即生效。

- 执行命令前请确认UCF服务处于上线状态。
- 每种报表的端口范围最多可配置64个。
- 不同协议类型UCFIP只能配置一条记录，并且FTP协议和SFTP协议的UCFIP不能同时配置。
- 使用非FTP协议时，配置的端口范围需要与UCFEXEC服务实例数保持一致。
- 当前版本不支持参数“协议类型”取值为“UDP(UDP)”。
- 当UCF本端IP和其他服务相同时，端口不能冲突，若存在冲突，请检查网设规划。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识记录索引号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF报表使用的协议类型。<br>数据来源：全网规划<br>取值范围：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- FTP（FTP）<br>- UDP（UDP）<br>默认值：无<br>配置原则：<br>FTP协议为非安全协议不建议使用。如果使用FTP协议，则配置的IP地址不能与其它服务配置的IP地址相同。 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址的类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定UCF本端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。<br>IP地址不能和UCF报表服务器地址在同一网段。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定UCF本端的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PORTSTART | 起始端口号 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"TCP"、"SFTP"、"UDP"时为条件必选参数。<br>参数含义：该参数用于指定UCF报表地址的起始端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1025~65534。<br>默认值：无<br>配置原则：无 |
| PORTEND | 结束端口号 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"TCP"、"SFTP"、"UDP"时为条件必选参数。<br>参数含义：该参数用于指定UCF报表地址的结束端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1025~65534。<br>默认值：无<br>配置原则：<br>结束端口号需大于或等于起始端口号，结束端口号与起始端口号之差不能大于等于64。 |
| VPNNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报表传输使用的VPN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：_public_<br>配置原则：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于标识报表IP资源池的描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UCF报表本地IP资源池（UCFIP）](configobject/UNC/20.15.2/UCFIP.md)

## 使用实例

运营商A为UCF配置简单组网下，添加TCP单据上报的本地IP资源池：

```
ADD UCFIP: INDEX=1, PROTOCOLTYPE=TCP, IPTYPE=IPv4, IPV4="10.185.23.253", PORTSTART=6000, PORTEND=6002;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置UCF报表本地IP资源池（ADD-UCFIP）_51253792.md`
