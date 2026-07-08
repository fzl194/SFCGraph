---
id: UNC@20.15.2@MMLCommand@TST GTPUPATH
type: MMLCommand
name: TST GTPUPATH（测试GTP-U路径）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: GTPUPATH
command_category: 调测类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- GTP-U
- GTP-U路径管理
status: active
---

# TST GTPUPATH（测试GTP-U路径）

## 功能

**适用网元：SGSN**

该命令用于通过发送GTP Echo request消息的方法测试本局与对端GSN之间的GTP-U路径是否正常。

## 注意事项

- 先选择对端的“IP地址类型”，再输入IP地址。
- 探测时使用路径的GTP-U协议版本发送Echo Request消息，如果对端没有响应则探测失败。
- 当系统中的GTP-U路径数目达到满规格时，该命令不可用。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-U路径的协议版本<br>取值范围：<br>- “GTPv0(GTPv0)”<br>- “GTPv1(GTPv1)”<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端GSN的IP地址类型<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPV4地址<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV4地址<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本端GSN IPV6地址<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端GSN IPV6地址<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUPATH]] · GTP-U路径（GTPUPATH）

## 使用实例

测试GTP-U Path:

TST GTPUPATH: GTPVER=GTPv1, IPTYPE=IPV4, LOCIPV4ADDR="192.168.9.20", PEERIPV4ADDR="192.168.14.20";

## 证据

- 原始手册：`evidence/UNC/20.15.2/TST-GTPUPATH.md`
