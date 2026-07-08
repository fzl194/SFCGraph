---
id: UNC@20.15.2@MMLCommand@RMV IPV6DNSH
type: MMLCommand
name: RMV IPV6DNSH（删除IPV6 DNS Hostfile记录）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPV6DNSH
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
- DNS
- DNS Hostfile管理
status: active
---

# RMV IPV6DNSH（删除IPV6 DNS Hostfile记录）

## 功能

**适用网元：SGSN、MME**

该命令用于删除网元接口所对应的IP地址信息。

## 注意事项

- 该命令执行后立即生效。
- 如果一个主机名对应的所有IP地址都被删除，以Hostfile方式进行DNS查询时，该主机名将不能被解析。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置主机名。<br>取值范围：1～255位字符串<br>默认值：无<br>配置原则：参见命令<br>[**ADD IPV6DNSH**](增加IPV6 DNS Hostfile记录(ADD IPV6DNSH)_26145886.md)<br>。 |
| ADDRSECTION | 地址区间号 | 可选必选说明：可选参数<br>参数含义：该参数用来划分IP地址区间。对同一个域名最多可以配置64个IP地址，使用此参数可以将64个IP地址划分为8个IP地址区间，每个区间最多8个IP地址，这样可以分8次来配置64个IP地址。<br>取值范围：<br>- “SECTION1(SECTION1)”<br>- “SECTION2(SECTION2)”<br>- “SECTION3(SECTION3)”<br>- “SECTION4(SECTION4)”<br>- “SECTION5(SECTION5)”<br>- “SECTION6(SECTION6)”<br>- “SECTION7(SECTION7)”<br>- “SECTION8(SECTION8)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6DNSH]] · IPV6 DNS Hostfile记录（IPV6DNSH）

## 使用实例

网络改造过程中，某个网元不再使用，删除该 “主机名” 为 “HUAWEI4.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG” 的HOSTFILE记录：

RMV IPV6DNSH: HOSTNAME="HUAWEI4.COM.GTP.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IPV6-DNS-Hostfile记录(RMV-IPV6DNSH)_72225565.md`
