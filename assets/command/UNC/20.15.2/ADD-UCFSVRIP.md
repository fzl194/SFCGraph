---
id: UNC@20.15.2@MMLCommand@ADD UCFSVRIP
type: MMLCommand
name: ADD UCFSVRIP（添加UCF报表服务器的接入点IP地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UCFSVRIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- UCF管理
- UCF服务器IP
status: active
---

# ADD UCFSVRIP（添加UCF报表服务器的接入点IP地址）

## 功能

![](添加UCF报表服务器的接入点IP地址（ADD UCFSVRIP）_51253793.assets/notice_3.0-zh-cn_2.png)

FTP协议为不安全协议，参数协议类型选择时请谨慎使用。

该命令用于配置报表服务器的接入点IP地址等信息。

## 注意事项

- 该命令执行后立即生效。

- 执行命令前请确认UCF服务处于上线状态。
- SFTP协议类型的记录最多可配置32条。
- FTP协议类型的记录最多可配置10条。
- 每个报表服务器最多可配置10个接入点IP地址。
- 当前版本不支持参数“服务器认证方式”取值为“PUBLICKEY(公钥认证)”。

- 最多可输入60条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLTYPE | 协议类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议类型。<br>数据来源：全网规划<br>取值范围：<br>- TCP（TCP）<br>- SFTP（SFTP）<br>- FTP（FTP）<br>- UDP（UDP）<br>默认值：无<br>配置原则：无 |
| ACCESSNAME | 接入点名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF服务器的接入点名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |
| UCFSVRNAME | UCF服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF服务器名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF服务器的IP类型。<br>数据来源：全网规划<br>取值范围：<br>- IPv4（IPv4）<br>- IPv6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | UCF服务器IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定UCF服务器的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。<br>IPv4地址不能和UCF本地IP地址资源池中的IPv4地址在同一网段。 |
| IPV6 | UCF服务器IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定UCF服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>IPv6地址不能和UCF本地IP地址资源池中的IPv6地址在同一网段。 |
| SVRPORT | UCF服务器端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UCF服务器端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~65534。<br>默认值：无<br>配置原则：无 |
| USER | 服务器用户名 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"SFTP"、"FTP"时为条件必选参数。<br>参数含义：该参数用于指定服务器用户名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |
| PWD | 服务器密码 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"SFTP"、"FTP"时为条件必选参数。<br>参数含义：该参数用于指定服务器密码。<br>数据来源：全网规划<br>取值范围：Pwd，取值范围是1~432。<br>默认值：无<br>配置原则：无 |
| AUTHMODE | 服务器认证方式 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"SFTP"、"FTP"时为条件必选参数。<br>参数含义：该参数用于指定服务器认证方式。<br>数据来源：本端规划<br>取值范围：<br>- “NOAUTH（无认证）”：在密钥协商阶段服务器认证方式不使用公钥认证，使用用户名密码认证。<br>- “PUBLICKEY（公钥认证）”：在密钥协商阶段服务器认证方式为密钥认证。<br>默认值：无<br>配置原则：无 |
| SVRPATH | 服务器上传路径 | 可选必选说明：该参数在"PROTOCOLTYPE"配置为"SFTP"、"FTP"时为条件必选参数。<br>参数含义：该参数用于指定服务器上传路径。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~512。<br>默认值：无<br>配置原则：<br>配置服务器上传路径时，请填写完整的FTP用户路径或只填写子目录名称。例：FTP用户路径是/home/ftpuser/test，可填写完整路径/home/ftpuser/test，或填写子目录名称test。<br>服务器上传路径不能包含特殊字符\|;&$<>，且不能包含点点（..）。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UCFSVRIP]] · UCF报表服务器的接入点IP地址（UCFSVRIP）

## 使用实例

运营商使用如下命令为1号报表服务器（UCFSVR1）配置1号接入点（ACCESS1）的IP地址等信息：

```
ADD UCFSVRIP: ACCESSNAME="ACCESS1", UCFSVRNAME="UCFSVR1", IPTYPE=IPv4, IPV4="10.180.211.254", SVRPORT=10500, PROTOCOLTYPE=TCP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UCFSVRIP.md`
