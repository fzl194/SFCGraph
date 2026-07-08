---
id: UNC@20.15.2@MMLCommand@ADD MSCPARA
type: MMLCommand
name: ADD MSCPARA（增加MSC参数）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MSCPARA
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- Sv接口管理
- MSC参数
status: active
---

# ADD MSCPARA（增加MSC参数）

## 功能

**适用网元：MME**

此命令用于配置MSC IP地址和MSC-Number之间的映射关系。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSC IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4(IPv4)<br>- IPV6(IPv6)<br>默认值：无 |
| IPV4 | MSC IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPv4”<br>后生效。<br>参数含义：该参数用于指定MSC的IPv4地址。<br>数据来源：全网规划<br>取值范围：0.0.0.1～255.255.255.254。<br>默认值：无<br>配置原则：<br>- IPv4地址不能为环回地址（127.x.y.z）。<br>- IPv4地址必须是A、B或者C类地址。 |
| IPV6 | MSC IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在<br>“IP地址类型”<br>参数配置为<br>“IPv6”<br>后生效。<br>参数含义：该参数用于指定MSC的IPv6地址。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：IPv6地址必须是全球单播地址，不能为未指定地址（::）、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MSCNUM | MSC-Number | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSC-Number。<br>数据来源：全网规划<br>取值范围：字符串类型，长度为1～15位的数字。<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于增加配置命令的描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0～32。<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCPARA]] · MSC参数（MSCPARA）

## 使用实例

增加一条MSC参数， “MSC IPv4地址” 为 “10.141.149.100” ， “MSC-Number” 为 “123456789” ：

ADD MSCPARA: IPTYPE=IPV4, IPV4="10.141.149.100", MSCNUM="123456789";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MSCPARA.md`
