---
id: UNC@20.15.2@MMLCommand@RMV MMECHARACT
type: MMLCommand
name: RMV MMECHARACT（删除MME属性配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMECHARACT
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- MME属性
status: active
---

# RMV MMECHARACT（删除MME属性配置信息）

## 功能

**适用网元：MME**

该命令用于删除对端MME的属性信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端MME的信令面IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPv4）”<br>- “IPV6（IPv6）”<br>默认值：无<br>配置原则：<br>- IPv4: 表示对端MME的信令面IP地址为IPv4类型。<br>- IPv6：表示对端MME的信令面IP地址为IPv6类型。 |
| IPV4 | MME IPv4信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端MME的信令面IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4（IPv4）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无<br>配置原则：有效的IPv4地址必须是A、B或者C类地址，且不能为环回地址（127.x.y.z）。 |
| MASKV4 | IPv4掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端MME的信令面IPv4地址的掩码。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4（IPv4）”<br>后生效。<br>数据来源：全网规划<br>取值范围：0.0.0.1~255.255.255.255<br>默认值：无<br>说明：- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | MME IPv6信令面地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定对端MME的信令面IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6（IPv6）”<br>后生效。<br>数据来源：全网规划<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MASKV6 | IPv6子网前缀长度 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6（IPv6）”<br>后生效。<br>数据来源：全网规划<br>取值范围：1~128<br>默认值：无 |

## 操作的配置对象

- [MME属性配置信息（MMECHARACT）](configobject/UNC/20.15.2/MMECHARACT.md)

## 使用实例

删除信令面IP地址为“192.168.168.12”，掩码为“255.255.255.0”的MME的属性信息：

RMV MMECHARACT: IPTYPE=IPV4, IPV4="192.168.168.12", MASKV4="255.255.255.0";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MME属性配置信息（RMV-MMECHARACT）_72345557.md`
