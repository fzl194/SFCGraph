---
id: UDG@20.15.2@MMLCommand@SYN LBSRVADDR
type: MMLCommand
name: SYN LBSRVADDR（CSLB向VNRS同步服务实例地址）
nf: UDG
version: 20.15.2
verb: SYN
object_keyword: LBSRVADDR
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 路由管理
- 服务实例地址同步
status: active
---

# SYN LBSRVADDR（CSLB向VNRS同步服务实例地址）

## 功能

![](CSLB向VNRS同步服务实例地址（SYN LBSRVADDR）_29627071.assets/notice_3.0-zh-cn.png)

全量模式可能会影响正常服务实例地址下发，请谨慎使用并联系华为技术支持协助操作。

当CSLB和VNRS之间服务实例地址数量不一致的时候，通过这个命令可以将CSLB上的服务实例地址同步到VNRS上。

## 注意事项

- 采用“全量同步”模式同步服务实例地址，可能会造成服务实例地址下发拥塞，导致业务流程失败，建议在VNF的业务低峰期执行，例如凌晨2点。
- 采用“全量同步”模式同步服务实例地址后，最多需要等待10分钟，同步才能完成，之后才能通过**[DSP SRVADDRNUM](../服务实例地址统计/查询服务实例地址数（DSP SRVADDRNUM）_29627069.md)**核查。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVVNFCID | 业务VNFCID | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务VNFC的唯一标识，通过在窗口下执行<br>**[LST NODE](../../../../单体服务公共功能管理/系统管理/基础参数/查询节点信息/查询节点信息（LST NODE）_27372977.md)**<br>获得，所得NODEID即为服务VNFC ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| SYNCMODE | 服务实例地址同步模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CSLB向VNRS同步服务实例地址的模式。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “SINGLEROUTE（单服务实例地址同步）”<br>- “ALLROUTE（全量同步）”<br>默认值：无<br>配置原则：只有当服务实例地址实际存在时，才能使用单点同步服务实例地址功能，服务实例地址可通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询获取。 |
| SRVINSTID | 服务实例ID | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定服务实例地址归属的服务实例ID。服务实例ID可以通过<br>**[DSP LBSRVINST](../../服务实例管理/服务实例/查询LB服务实例（DSP LBSRVINST）_29627060.md)**<br>查询获取。<br>配置原则：该参数在<br>“SYNCMODE（服务实例地址同步模式）”<br>参数配置为<br>“单服务实例地址同步”<br>后生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295。<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定同步服务实例地址的IP地址类型。IP地址类型可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询IPTYPE字段获取。<br>配置原则：该参数在<br>“SYNCMODE（服务实例地址同步模式）”<br>参数配置为<br>“单服务实例地址同步”<br>后生效。<br>数据来源：本端规划<br>取值范围：枚举类型<br>- “IPV4”<br>- “IPV6”<br>默认值：无 |
| DSTIPV4 | 目的IPv4地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定同步的IPv4地址。目的IPv4地址可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询DSTIPV4字段获取。<br>配置原则：该参数在<br>“IPTYPE（IP地址类型）”<br>参数配置为<br>“IPV4”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0-255.255.255.255<br>默认值：无 |
| DSTIPV6 | 目的IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定同步的IPv6地址。目的IPv6地址可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询DSTIPV6字段获取。<br>配置原则：该参数在<br>“IPTYPE（IP地址类型）”<br>参数配置为<br>“IPV6”<br>后生效。<br>数据来源：本端规划<br>取值范围：::-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| IPV4MASK | IPv4掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定服务实例地址IPv4掩码。IPv4掩码可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询IPV4MASK字段获取。<br>配置原则：该参数在<br>“IPTYPE（IP地址类型）”<br>参数配置为<br>“IPV4”<br>后生效。<br>数据来源：本端规划<br>取值范围：0.0.0.0-255.255.255.255<br>默认值：无 |
| IPV6MASK | IPv6掩码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定服务实例地址IPv6掩码。IPv6掩码可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询IPV6MASK字段获取。<br>配置原则：该参数在<br>“IPTYPE（IP地址类型）”<br>参数配置为<br>“IPV6”<br>后生效。<br>数据来源：本端规划<br>取值范围：::-FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于同步服务实例地址的VPN名称。VPN名称可以通过<br>**[DSP SRVIP](../服务实例地址/查询服务IP（DSP SRVIP）_29627067.md)**<br>查询VPNNAME字段获取<br>配置原则：该参数在<br>“SYNCMODE（服务实例地址同步模式）”<br>参数配置为<br>“单服务实例地址同步”<br>后生效。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为0~31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LBSRVADDR]] · CSLB向VNRS同步服务实例地址（LBSRVADDR）

## 使用实例

采用单服务实例地址同步模式，业务服务ID为4，服务实例同步模式选 “单服务实例地址同步” 模式，服务实例ID为1，IP类型选IPV4，服务实例地址通过DSP SRVIP命令查询获取，执行同步服务实例地址命令结果如下：

SYN LBSRVADDR: SRVVNFCID=4, SYNCMODE=SINGLEROUTE, SRVINSTID=1, IPTYPE=IPV4, DSTIPV4="192.168.100.1", IPV4MASK="255.255.255.0", VPNNAME="_public_";

```
%%SYN LBSRVADDR: SRVVNFCID=4, SYNCMODE=SINGLEROUTE, SRVINSTID=1, IPTYPE=IPV4, DSTIPV4="192.168.100.1", IPV4MASK="255.255.255.0", VPNNAME="_public_";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SYN-LBSRVADDR.md`
