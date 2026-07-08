---
id: UDG@20.15.2@MMLCommand@COL LOG
type: MMLCommand
name: COL LOG（收集日志信息）
nf: UDG
version: 20.15.2
verb: COL
object_keyword: LOG
command_category: 调测类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 收集日志
status: active
---

# COL LOG（收集日志信息）

## 功能

该命令用于收集VNFP/VNFC日志，目前支持收集VNFC日志、AppMgmtFunction和UpgRecord日志。

在系统发生故障时，用户可以执行本命令收集日志用于问题定位。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOGTYPE | 日志类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定收集数据的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- VNFC：收集该网元启动、操作日志，如/var/log/fenix等文件夹下所有日志文件。<br>- AppMgmtFunction：收集业务日志。<br>- All：收集所有支持的日志类型（VNFC，AppMgmtFunction和UpgRecord）。<br>- UpgRecord：收集升级过程记录信息。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 只能填写实际存在的资源单元或资源名称。<br>- 当本命令在VNFP上使用时，需要先使用[**DSP RES**](../../../../单体服务平台功能管理/系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)查到“资源名称”，然后将“资源名称”的取值配置到本参数。<br>- 当本命令在VNFC上使用时，需要先使用[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)查到“RU名称”，然后将“RU名称”的取值配置到本参数。 |
| STARTTIME | 开始时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定收集此开始时间后的日志。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。01/01/2000 00:00:00～31/12/2037 23:59:59。<br>默认值：无<br>配置原则：此时间是绝对时间，不考虑时间偏移。 |
| ENDTIME | 结束时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定收集此结束时间前的日志。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。01/01/2000 00:00:00～31/12/2037 23:59:59。<br>默认值：无<br>配置原则：此时间是绝对时间，不考虑时间偏移。 |
| SERVICETYPE | 传输协议 | 可选必选说明：可选参数<br>参数含义：该参数用于指定service端的传输协议。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- SFTP：使用SFTP协议下载文件。<br>默认值：无<br>配置原则：Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。 |
| IPVERSION | 服务器IP版本 | 可选必选说明：条件必选参数，该参数在<br>“SERVICETYPE”<br>配置为<br>“SFTP”<br>时为必选参数。<br>参数含义：该参数用于指定服务器地址族。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPv4：IPv4地址。<br>- IPv6：IPv6地址。<br>默认值：IPv4 |
| SERVICEIP | 服务器IPv4地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv4”<br>时为必选参数。<br>参数含义：该参数用于指定service端的ip地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。 |
| SERVICEPORT | 服务器端口号 | 可选必选说明：条件必选参数，该参数在<br>“SERVICETYPE”<br>配置为<br>“SFTP”<br>时为必选参数。<br>参数含义：该参数用于指定service端的服务端口。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。 |
| USERNAME | 服务器用户名 | 可选必选说明：条件必选参数，该参数在<br>“SERVICETYPE”<br>配置为<br>“SFTP”<br>时为必选参数。<br>参数含义：该参数用于指定service端的用户名。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。 |
| PASSWORD | 服务器密码 | 可选必选说明：条件必选参数，该参数在<br>“SERVICETYPE”<br>配置为<br>“SFTP”<br>时为必选参数。<br>参数含义：该参数用于指定service端的密码。<br>数据来源：对端协商<br>取值范围：密码类型，输入长度范围为1～127。<br>默认值：无<br>配置原则：<br>- Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。<br>- 该参数取值中不允许包含“?”。 |
| REMOTEPATH | 服务器路径 | 可选必选说明：条件必选参数，该参数在<br>“SERVICETYPE”<br>配置为<br>“SFTP”<br>时为必选参数。<br>参数含义：该参数用于指定要把收集的压缩包拷到server的远端路径。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：Server IP Address、Server Type 、Server Port Number 、Server Path、Server User Name及Server Password只要配了一个，则另5个也必须配。 |
| RUNUM | RU分批个数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定整网元收集时分批打包的RU个数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～5。<br>默认值：无 |
| SERVERIPV6 | 服务器IPv6地址 | 可选必选说明：条件必选参数，该参数在<br>“IPVERSION”<br>配置为<br>“IPv6”<br>时为必选参数。<br>参数含义：该参数用于指定服务器IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LOG]] · 日志导出参数（LOG）

## 使用实例

收集VNODE_CSDB_VNFC_OMU_0001的网元日志，上传到指定FTP服务器上(日志搜集结果存放在命令指定FTP服务器上，路径为：/var/sftp)：

```
COL LOG:RUNAME="VNODE_CSDB_VNFC_OMU_0001",LOGTYPE=VNFC,SERVICETYPE=SFTP,IPVERSION=IPv4,SERVICEIP="10.0.0.1",SERVICEPORT=23,USERNAME="username",PASSWORD="*****",REMOTEPATH="/var/sftp"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/COL-LOG.md`
