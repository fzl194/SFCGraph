---
id: UNC@20.15.2@MMLCommand@FTR ACSFILE
type: MMLCommand
name: FTR ACSFILE（文件传输）
nf: UNC
version: 20.15.2
verb: FTR
object_keyword: ACSFILE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 文件传输管理
status: active
---

# FTR ACSFILE（文件传输）

## 功能

该命令用于使用SFTP协议进行文件传输操作。

本命令只适用于ACS服务，其他微服务请使用FTR FILE命令。

## 注意事项

- SFTP异步传输文件可通过事件日志确认结果。
- 本地文件路径为用户目录下的相对路径或用户设置的路径。
- 该命令仅提供文件传输的通用能力，不提供其他能力（如服务器端文件的类型、大小校验等）。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRANSFERPROTOCOL | 传输协议 | 可选必选说明：必选参数<br>参数含义：该参数用于表示传输协议。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- sftp：SFTP传输协议。<br>默认值：无 |
| COMMANDTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- get：get操作。<br>- put：put操作。<br>默认值：无 |
| IPVERSION | 服务器地址族 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务器地址族。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPv4：IPv4。<br>- IPv6：IPv6。<br>默认值：IPv4 |
| SERVERIPV4ADDRESS | 服务器IPv4地址 | 可选必选说明：条件必选参数，该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示服务器IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SERVERIPV6ADDRESS | 服务器IPv6地址 | 可选必选说明：条件必选参数，该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示服务器IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SERVERPORT | 服务器端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务器端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| USERNAME | 用户名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示用户名。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～253。<br>默认值：无 |
| PASSWORD | 密码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示密码。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～128。仅支持明文输入。<br>默认值：无 |
| LOCALFILENAME | 本地文件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示本地文件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无 |
| REMOTEFILENAME | 服务器端文件名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务器端文件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACSFILE]] · 文件传输（ACSFILE）

## 使用实例

使用SFTP协议进行文件传输操作：

```
FTR ACSFILE:TRANSFERPROTOCOL=sftp,COMMANDTYPE=put,IPVERSION=IPv4,SERVERIPV4ADDRESS="192.168.1.11",SERVERPORT=22,USERNAME="root",PASSWORD="*****",LOCALFILENAME="local.sh",REMOTEFILENAME="/var/sftp/remote.sh";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/文件传输（FTR-ACSFILE）_05338967.md`
