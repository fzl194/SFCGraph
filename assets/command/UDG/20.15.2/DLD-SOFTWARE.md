---
id: UDG@20.15.2@MMLCommand@DLD SOFTWARE
type: MMLCommand
name: DLD SOFTWARE（下载软件仓软件）
nf: UDG
version: 20.15.2
verb: DLD
object_keyword: SOFTWARE
command_category: 调测类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 系统管理
- 系统维护
- 软件仓软件
status: active
---

# DLD SOFTWARE（下载软件仓软件）

## 功能

该命令用来从指定服务器下载软件包到软件仓中。当VNF已经升级为新版本时，可以在软件仓中增加此版本，若系统中新版本被破坏，可以从软件仓中恢复。

## 注意事项

- 该命令执行后立即生效。
- 指定“TRANSFERPRTL”为“HTTPS”，用于动态上线VNFC后需要给VNFC打补丁时，下载VNFC补丁包。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | 服务器IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务器地址族。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- **IPv4**：IPv4地址。<br>- **IPv6**：IPv6地址。<br>默认值：<br>**IPv4** |
| SERVERIP | 服务器IPv4地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv4”<br>时为必选参数。<br>参数含义：该参数用于指定服务器IP地址，服务器需要提前放置新的软件包。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SERVERIPV6 | 服务器IPv6地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv6”<br>时为必选参数。<br>参数含义：该参数用于指定服务器IPv6地址，服务器需要提前放置新的软件包。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SERVERPORT | 服务器端口号 | 可选必选说明：<br>条件必选参数，该参数在“TRANSFERPRTL”配置为“SFTP”时为必选参数。<br>参数含义：该参数用于指定服务器端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| USERNAME | 用户名 | 可选必选说明：<br>条件必选参数，该参数在“TRANSFERPRTL”配置为“SFTP”时为必选参数。<br>参数含义：该参数用于指定服务器的用户名。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| PASSWORD | 密码 | 可选必选说明：<br>条件必选参数，该参数在“TRANSFERPRTL”配置为“SFTP”时为必选参数。<br>参数含义：该参数用于指定服务器的密码。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～127。<br>默认值：无 |
| PACKAGEDIR | 软件路径 | 可选必选说明：<br>条件必选参数，该参数在“TRANSFERPRTL”配置为“SFTP”时为必选参数。<br>参数含义：该参数用于指定服务器待下载的软件包路径，路径为VNF级，也支持VNF级的zip包文件名路径，支持多个VNFC包一起下载。<br>指定<br>“PACKAGEDIR”<br>为VNF级的软件包路径时，仅支持软件仓不同版本软件包的下载。<br>指定<br>“PACKAGEDIR”<br>为VNF级的zip包路径时，支持软件仓同版本软件包及不同版本软件包的下载。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无 |
| INSTALLVNFD | 安装元模型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否加载元模型。<br>数据来源：对端协商<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：<br>**FALSE** |
| TRANSFERPRTL | 传输协议 | 可选必选说明：可选参数<br>参数含义：该参数用于指定传输协议。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- **SFTP**：使用SFTP协议下载文件。<br>- **HTTPS**：使用HTTPS协议下载文件。<br>默认值：<br>**SFTP** |
| CPUARCHTYPE | CPU架构类型 | 可选必选说明：条件可选参数，<br>该参数在“TRANSFERPRTL”配置为“HTTPS”时为可选参数。<br>参数含义：该参数用于指定CPU架构类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- **X86**：CPU架构类型选择的是X86。<br>- **Any**：CPU架构类型选择的是Any。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SOFTWARE]] · 下载软件仓软件（SOFTWARE）

## 使用实例

- 通过指定ftp服务器路径增加软件仓中软件：
  ```
  DLD SOFTWARE:TRANSFERPRTL=SFTP,IPVERSION=IPv4,SERVERIP="192.168.0.15",SERVERPORT=22,USERNAME="HUAWEI-123",PASSWORD="*****",PACKAGEDIR="/var/sftp/VNF_FENIX/FENIX_base";
  ```
- 通过指定ftp服务器zip包增加软件仓中软件：
  ```
  DLD SOFTWARE:TRANSFERPRTL=SFTP,IPVERSION=IPv4,SERVERIP="192.168.0.15",SERVERPORT=22,USERNAME="HUAWEI-123",PASSWORD="*****",PACKAGEDIR="/var/sftp/VNF.zip";
  ```
- 通过HTTPS协议下载最新网元补丁包：
  ```
  DLD SOFTWARE:TRANSFERPRTL=HTTPS;
  ```
- 通过HTTPS协议指定CPU架构类型下载补丁：
  ```
  DLD SOFTWARE:TRANSFERPRTL=HTTPS, INSTALLVNFD=FALSE, CPUARCHTYPE=Any;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/下载软件仓软件（DLD-SOFTWARE）_59037011.md`
