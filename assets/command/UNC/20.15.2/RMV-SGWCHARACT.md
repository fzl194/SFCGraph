---
id: UNC@20.15.2@MMLCommand@RMV SGWCHARACT
type: MMLCommand
name: RMV SGWCHARACT（删除S-GW特性对接配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWCHARACT
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GW属性
status: active
---

# RMV SGWCHARACT（删除S-GW特性对接配置）

## 功能

![](删除S-GW特性对接配置(RMV SGWCHARACT)_72345569.assets/notice_3.0-zh-cn_2.png)

该命令将删除指定网段内MME/S4 SGSN与S-GW支持特性的能力交互配置策略。

**适用网元：SGSN、MME**

该命令用于删除MME与S-GW支持特性的能力交互配置策略。

## 注意事项

- 该命令执行后立即生效。
- “ALL(所有S-GW)”为系统的缺省记录，不允许增加，也不允许删除。
- 该命令将删除指定网段内MME与S-GW支持特性的能力交互配置策略。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要特性能力相互通知的对端设备S-GW范围。<br>数据来源：全网规划<br>取值范围：<br>- “SPECIFIED(指定S-GW)”<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IP地址类型。<br>前提条件：该参数在<br>“对端设备范围”<br>参数配置为<br>“SPECIFIED(指定S-GW)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无<br>配置原则：<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| IPV4MSK | IPV4地址掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端S-GW的信令面IPv4地址的掩码。<br>前提条件：该参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值：无<br>配置原则：<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定S-GW信令面IPv6地址。<br>前提条件：该参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| IPV6MSK | IPV6地址前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IPv6地址的子网前缀的长度。<br>前提条件：该参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：本端规划<br>取值范围：0~128<br>默认值：无<br>配置原则：0是无效掩码。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCHARACT]] · S-GW特性对接配置（SGWCHARACT）

## 使用实例

该命令用于删除MME与S-GW支持特性的能力交互配置策略，执行此命令：

RMV SGWCHARACT: RANGE=SPECIFIED, IPT=IPV4, IPV4="10.95.69.96", IPV4MSK="255.255.255.0";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SGWCHARACT.md`
