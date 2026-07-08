---
id: UNC@20.15.2@MMLCommand@RMV CHGCG
type: MMLCommand
name: RMV CHGCG（删除CG配置参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGCG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 计费控制
status: active
---

# RMV CHGCG（删除CG配置参数）

## 功能

![](删除CG配置参数(RMV CHGCG)_26305190.assets/notice_3.0-zh-cn_2.png)

如果删除正在发送话单的CG，可能会引起少量话单丢失。

**适用网元：SGSN**

该命令用于删除CG配置表中某条CG的配置。

## 注意事项

- 该命令执行后立即生效。
- 如果删除正在发送话单的CG，可能会引起少量话单丢失。
- “GTP承载协议（PRO）”、“CG的IP地址（IP）”、“CG接收端口号(SPN)”唯一确定需要删除的CG配置记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPV4地址)”<br>- “IPV6(IPV6地址)”<br>默认值：无 |
| IP | CG的IPV4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IPV4地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV4(IPV4地址)”<br>后生效。<br>取值范围：0.0.0.1~255.255.255.254<br>默认值：无 |
| IPV6 | CG的IPV6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于标识与本端SGSN连接的CG的IPV6地址。<br>前提条件：该参数在<br>“IPT(IP地址类型)”<br>配置为<br>“IPV6(IPV6地址)”<br>后生效。<br>数据来源：全网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PRO | GTP承载协议 | 可选必选说明：必选参数<br>参数含义：该参数用于标识CG支持的GTP'承载协议。<br>取值范围：<br>- “UDP(UDP)”：表示SGSN和CG之间通过UDP/IP进行通讯。<br>- “TCP(TCP)”：表示SGSN和CG之间通过TCP/IP进行通讯。<br>默认值：无 |
| SPN | CG接收端口号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识SGSN消息所要发往的端口号（亦即UDP类型CG的接收端口号）或TCP类型CG的侦听端口号。<br>取值范围：1024~65535<br>默认值：无<br>说明：与对端CG设置保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCG]] · CG配置参数（CHGCG）

## 使用实例

1. 删除IP地址类型为IPV4，CG的IPV4地址为"172.22.5.50"，GTP承载协议为UDP，CG接收端口号为3386的CG配置信息：
  RMV CHGCG: IPT=IPV4, IP="172.22.5.50", PRO=UDP, SPN=3386;
2. 删除IP地址类型为IPV4，CG的IPV4地址为"172.22.5.42"，GTP承载协议为UDP，CG接收端口号为3386的CG配置信息：
  RMV CHGCG: IPT=IPV4, IP="172.22.5.42", PRO=UDP, SPN=3386;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CHGCG.md`
