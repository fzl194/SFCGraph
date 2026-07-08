---
id: UNC@20.15.2@MMLCommand@MOD DNSS
type: MMLCommand
name: MOD DNSS（修改DNS服务器）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DNSS
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS服务器管理
status: active
---

# MOD DNSS（修改DNS服务器）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于修改一个DNS域名解析服务器的优先级、名称和承载协议。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | 服务器组ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DNS服务器所属的服务器组。<br>前提条件：该参数必须已经通过<br>[**ADD DNSS**](增加DNS服务器(ADD DNSS)_72345497.md)<br>配置。<br>数据来源：整网规划<br>取值范围：0~37<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无 |
| IP | IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定DNS服务器IP地址。<br>该参数在"IP地址类型"参数配置为"IPV4(IPV4)"后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：DNS服务器IPv6地址<br>该参数在"IP地址类型"参数配置为"IPV6(IPV6)"后生效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PRI | 域名服务器优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS服务器的优先级。<br>数据来源：整网规划<br>取值范围：<br>- “PRI1(优先级1)”<br>- “PRI2(优先级2)”<br>- “PRI3(优先级3)”<br>- “PRI4(优先级4)”<br>- “PRI5(优先级5)”<br>- “PRI6(优先级6)”<br>默认值：无<br>配置原则：优先级从PRI1到PRI6依次递减。配置多个DNS服务器时，优先级高的服务器优先使用。高优先级的服务器故障时，使用次优的服务器。 |
| DNSSNAME | DNS服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS服务器名称。<br>数据来源：整网规划<br>取值范围：0~32个字符<br>默认值：无 |
| PRO | DNS服务器承载协议 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS服务器的承载协议，协议可以是TCP或者UDP。<br>数据来源：整网规划<br>取值范围：<br>- “TCP(TCP传输模式)”：表示仅支持TCP协议。<br>- “UDP_TCP(UDP_TCP传输模式)”：表示既支持UDP又支持TCP协议。<br>- “UDP(UDP传输模式)”：表示仅支持UDP协议。<br>默认值：无<br>配置原则：<br>- “DNS服务器承载协议”建议值为“UDP_TCP(UDP_TCP传输模式)”，即同时创建UDP、TCP两种类型的链路，优先选择UDP链路，当报文较长时（如响应中的IP个数超过28个时），切换为TCP链路。<br>- 系统如果配置了NAPTR类型的查询，该类型查询的响应消息一般比较长。此时建议配置为“TCP(TCP传输模式)”或者“UDP_TCP(UDP_TCP传输模式)”。<br>说明：不同组下面配置相同的服务器时，修改任一组中的该服务器承载协议，其他组中的该服务器承载协议也会被修改。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNSS]] · DNS服务器（DNSS）

## 使用实例

将第一组IP地址为192.168.100.101的DNS服务器优先级修改为2，IPT为承载协议修改为TCP：

MOD DNSS: GRPID=1, IPT=IPV4, IP="192.168.100.101", PRI=PRI2, PRO=TCP;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-DNSS.md`
