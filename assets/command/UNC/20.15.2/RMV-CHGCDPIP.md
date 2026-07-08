---
id: UNC@20.15.2@MMLCommand@RMV CHGCDPIP
type: MMLCommand
name: RMV CHGCDPIP（删除计费相关的IP配置参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGCDPIP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- CDPIP 配置
status: active
---

# RMV CHGCDPIP（删除计费相关的IP配置参数）

## 功能

**适用网元：SGSN**

该命令用于删除CDP进程上指定的IP地址。

## 注意事项

该命令在版本升级过程中禁止执行。若升级强制执行将导致话单发送不出而被保存在硬盘。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPv4(IPv4地址)”<br>- “IPv6(IPv6地址)”<br>默认值： 无 |
| IPV4ADDR | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CDP的IPv4地址。<br>前提条件：该参数在<br>“IPT”<br>设置为<br>“IPv4(IPv4地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：“0.0.0.0”和“255.255.255.255”是无效的IP地址。<br>配置原则：<br>- IPv4地址不能为0.0.0.0、255.255.255.255和0.x.y.z。<br>- IPv4地址不能为组播地址（如：224.x.y.z）和环回地址(如：127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6ADDR | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定CDP的IPv6地址。<br>前提条件：该参数在<br>“IPT”<br>设置为<br>“IPv6(IPv6地址)”<br>时有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PORTBGN | 起始端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定起始端口号。<br>数据来源：整网规划<br>取值范围：1024～65534<br>默认值：无<br>说明：端口号不可使用下述知名端口：2123(GTPCv1)，2152(GTPUv1)，3784(BFD)，3785(BFD)，4784(BFD)，4500(IKEv2)。 |
| PORTEND | 结束端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定结束端口号。<br>数据来源：整网规划<br>取值范围：1024～65534<br>默认值：无<br>说明：端口号不可使用下述知名端口：2123(GTPCv1)，2152(GTPUv1)，3784(BFD)，3785(BFD)，4784(BFD)，4500(IKEv2)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDPIP]] · 计费相关的IP配置参数（CHGCDPIP）

## 使用实例

删除CDP IP地址，IP地址类型为IPv4地址，IP地址为172.22.5.50，起始端口号3699，结束端口号3700：

RMV CHGCDPIP: IPT=IPv4, IPV4ADDR="172.22.5.50", PORTBGN=3699, PORTEND=3700;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除计费相关的IP配置参数(RMV-CHGCDPIP)_26145360.md`
