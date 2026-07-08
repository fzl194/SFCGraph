---
id: UDG@20.15.2@ConfigObject@NTPSVR
type: ConfigObject
name: NTPSVR（NTP服务器）
nf: UDG
version: 20.15.2
object_name: NTPSVR
object_kind: entity
status: active
---

# NTPSVR（NTP服务器）

## 说明

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

## 操作本对象的命令

- [ADD NTPSVR](command/UDG/20.15.2/ADD-NTPSVR.md)
- [LST NTPSVR](command/UDG/20.15.2/LST-NTPSVR.md)
- [MOD NTPSVR](command/UDG/20.15.2/MOD-NTPSVR.md)
- [RMV NTPSVR](command/UDG/20.15.2/RMV-NTPSVR.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改NTP服务器(MOD-NTPSVR)_67551556.md`
- 原始手册：`evidence/UDG/20.15.2/删除NTP服务器(RMV-NTPSVR)_54491177.md`
- 原始手册：`evidence/UDG/20.15.2/增加NTP服务器(ADD-NTPSVR)_54491176.md`
- 原始手册：`evidence/UDG/20.15.2/查询NTP服务器(LST-NTPSVR)_54491178.md`
