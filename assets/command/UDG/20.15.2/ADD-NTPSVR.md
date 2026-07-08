---
id: UDG@20.15.2@MMLCommand@ADD NTPSVR
type: MMLCommand
name: ADD NTPSVR（增加NTP服务器）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: NTPSVR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- NTP服务器管理
status: active
---

# ADD NTPSVR（增加NTP服务器）

## 功能

本命令用于增加一条NTP服务器数据记录。

本命令的使用场景为：日常维护活动中，使用本命令增加NTP服务器。NTP服务器用于提供时钟同步源，各类设备通过外接NTP服务器来同步修正自身的时间，使其自身的时间更准确、精度更高。

在本命令中，以下参数需要与NTP服务器端协商：

- IP地址
- 身份验证标志
- 身份验证密钥号
- 密钥类型
- 密钥串

> **说明**
> 执行命令新增NTP服务器后，同步状态更新需等待约三个同步周期（默认一个同步周期为一分钟）。

> **说明**
> - 最多只能增加四个NTP服务器，增加的NTP服务器名称及IP地址不可重复。
> - 若增加了多个NTP服务器，则系统同时接收所有配置NTP服务器发送的时间信息，并由系统根据NTP协议中规定的选择算法，自动选择其中一个NTP服务器作为时钟同步时钟源。已配置的NTP服务器信息可以使用**[**LST NTPSVR**](查询NTP服务器(LST NTPSVR)_54491178.md)**命令查询、**[**MOD NTPSVR**](修改NTP服务器(MOD NTPSVR)_67551556.md)**命令修改和**[**RMV NTPSVR**](删除NTP服务器(RMV NTPSVR)_54491177.md)**命令删除。
> - 系统从NTP服务器校时年份范围：1990年～2035年。建议配置标准NTP服务器，若配置多个NTP服务器，请确保NTP服务器间时间一致，防止时间紊乱导致计费错乱等问题。
> - 新增NTP服务器时，需要先配置FusionStage的NTP服务器，再使用本命令增加NTP服务器，且NTP服务器配置需要保持一致。
> - 禁止在升级、打补丁、回退过程中、升级观察期内增加NTP服务器。
> - 外网单栈IPV4场景仅支持新增IPV4的NTP服务器；单栈IPV6场景仅支持新增IPV6的NTP服务器。双栈场景可支持IPV4/IPV6的NTP服务器。
> - 当“密钥类型”配置为“SHA1”时，系统会上报“ALM-135906与外部时钟源同步证书不安全”告警。
> - NTPV3协议存在被攻击的风险，可能会导致系统时间被篡改，建议使用NTPV4协议。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SVRNAME | NTP服务器名 | 可选必选说明：必选参数。<br>参数含义：用于具体描述一个NTP服务器，以便于识别。<br>取值范围：长度不超过32个英文字母或数字及其组合（不支持中文字符和特殊字符，仅支持英文字母或数字[A~Za~z0~9]）。<br>默认值：无。<br>配置原则：无。 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数。<br>参数含义：用于指定需要增加的NTP服务器的IP地址类型。根据选择的IP地址类型决定输入的是点分十进制格式的IPV4地址还是冒号分割十六进制格式的IPV6地址。<br>取值范围：<br>- “IPV4(IPV4地址)”：IPV4地址。<br>- “IPV6(IPV6地址)”：IPV6地址。<br>默认值：<br>“IPV4(IPV4地址)”<br>：IPV4地址。<br>配置原则：无。 |
| IPADDRESS | IPV4地址 | 可选必选说明：该参数在<br>“IP地址类型”<br>配置为<br>“IPV4(IPV4地址)”<br>时为条件必选参数。<br>参数含义：指定新增NTP服务器的IPV4地址。<br>取值范围：0.0.0.0~255.255.255.255。<br>默认值：无。<br>配置原则：仅当本命令中的<br>“IP地址类型”<br>参数为<br>“IPV4(IPV4地址)”<br>时该参数有效。 |
| IPADDRESS6 | IPV6地址 | 可选必选说明：该参数在<br>“IP地址类型”<br>配置为<br>“IPV6(IPV6地址)”<br>时为条件必选参数。<br>参数含义：指定新增NTP服务器的IPV6地址。<br>取值范围：0:0:0:0:0:0:0:0~ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff。<br>默认值：无。<br>配置原则：仅当本命令中的<br>“IP地址类型”<br>参数为<br>“IPV6(IPV6地址)”<br>时该参数有效。 |
| PROTOCOLVERSION | NTP协议版本 | 可选必选说明：必选参数。<br>参数含义：指定新增NTP服务器的协议版本。<br>取值范围：<br>- “NTPV4(NTPV4)”：NTPV4。<br>- “NTPV3(NTPV3)”：NTPV3。<br>默认值：<br>“NTPV4(NTPV4)”<br>：NTPV4。<br>配置原则：无。 |
| AUTHFLAG | 身份验证标志 | 可选必选说明：该参数在<br>“NTP协议版本”<br>配置为<br>“NTPV4(NTPV4)”<br>时为条件必选参数。<br>参数含义：<br>- 用于指定该NTP服务器是否启用身份验证功能。<br>- NTP服务器身份校验功能是为增加NTP的可靠性和网络安全性而提供的，用户可以根据需要进行选择。<br>- 身份验证功能需要NTP服务器支持，只有在NTP服务器支持身份验证时客户端才能与NTP服务器正常校时。<br>取值范围：<br>- “NO(否)”：不进行身份验证。<br>- “YES(是)”：进行身份验证。<br>默认值：<br>“NO(否)”<br>。<br>配置原则：无。 |
| KEYID | 身份验证密钥号 | 可选必选说明：该参数在<br>“身份验证标志”<br>配置为<br>“YES(是)”<br>时为条件必选参数。<br>参数含义：从NTP服务器端所获取的身份验证密钥号，用于验证服务器身份。<br>取值范围：1～65533<br>默认值：无。<br>配置原则：密钥号与FusionStage的NTP服务器配置保持一致。 |
| SHASTRING | 密钥类型 | 可选必选说明：该参数在<br>“身份验证标志”<br>配置为<br>“YES(是)”<br>时为条件必选参数。<br>参数含义：从NTP服务器端所获取的身份验证密钥类型，用于验证服务器身份。<br>取值范围：<br>- SHA256(SHA256)<br>- SHA1(SHA1)<br>默认值：SHA256(SHA256)<br>配置原则：密钥类型与FusionStage的NTP服务器配置保持一致。 |
| KEYSTRING | 密钥串 | 可选必选说明：该参数在<br>“身份验证标志”<br>配置为<br>“YES(是)”<br>时为条件必选参数。<br>参数含义：从NTP服务器端所获取的密钥串，用于验证服务器身份。<br>取值范围：长度范围为[40~128]，为十六进制（包含的字母为[A~Fa~f0~9]）。<br>默认值：无。<br>配置原则：<br>- 密钥串不能为空。<br>- 密钥串与FusionStage的NTP服务器配置保持一致。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NTPSVR]] · NTP服务器（NTPSVR）

## 关联任务

- [[UDG@20.15.2@Task@0-00248]]

## 使用实例

1. 增加一个NTP服务器， “NTP服务器名” 为 “server3” ，选择 **"IP地址类型"** 为 “IPV4(IPV4地址)” , “IPV4地址” 为 “192.168.156.12” ， “NTP协议版本” 为 “NTPV4” ， “身份验证标志” 为 “YES” ， “身份验证密钥号” 为 “32323” ， “密钥类型” 为 “SHA256” ， “密钥串” 为 “aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa” ：
  ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV4, AUTHFLAG=YES, KEYID=32323, SHASTRING=SHA256, KEYSTRING="*****";
  ```
  %%ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV4, AUTHFLAG=YES, KEYID=32323, SHASTRING=SHA256, KEYSTRING="*****";%% 
  RETCODE = 0  操作成功  
  ---    END
  ```
2. 增加一个NTP服务器， “NTP服务器名” 为 “server3” ，选择 **"IP地址类型"** 为 “IPV4(IPV4地址)” , “IPV4地址” 为 “192.168.156.12” ， “NTP协议版本” 为 “NTPV4” ， “身份验证标志” 为 “NO” ：
  ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV4, AUTHFLAG=NO;

  ```
  %%ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV4, AUTHFLAG=NO;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```
3. 增加一个NTP服务器， “NTP服务器名” 为 “server3” ，选择 **"IP地址类型"** 为 “IPV4(IPV4地址)” , “IPV4地址” 为 “192.168.156.12” ， “NTP协议版本” 为 “NTPV3” ：
  ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV3;

  ```
  %%ADD NTPSVR: SVRNAME="server3", IPTYPE=IPV4, IPADDRESS="192.168.156.12", PROTOCOLVERSION=NTPV3;%% 
  RETCODE = 0  操作成功  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-NTPSVR.md`
