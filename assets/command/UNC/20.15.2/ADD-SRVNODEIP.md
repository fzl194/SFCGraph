---
id: UNC@20.15.2@MMLCommand@ADD SRVNODEIP
type: MMLCommand
name: ADD SRVNODEIP（增加服务节点IP）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SRVNODEIP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于对接IP地址的虚拟APN映射管理
- 服务节点组的服务节点IP段
status: active
---

# ADD SRVNODEIP（增加服务节点IP）

## 功能

**适用NF：PGW-C、GGSN**

该命令用来增加一个新的服务节点IP。当需要用SGSN IP、SGW IP、PCF IP进行虚拟APN映射时，在不同的场景下需要使用该命令增加SGSN/SGW/PCF的服务节点组绑定的服务节点IP地址段。

## 注意事项

- 该命令执行后立即生效。

- 一个服务节点组最多绑定1000个服务节点IP地址段。
- 地址段不能重叠。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 服务节点组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务节点组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>本参数通过ADD SRVNODEGROUP命令进行配置。 |
| IPSECTIONID | 服务节点IP地址段编号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定服务节点IP地址段的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~2999。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRSTART | 服务节点IPV4地址段的起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于设定服务节点IP地址段的IPv4起始IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。具体取值范围为：1.0.0.1-126.255.255.254，128.1.0.1-191.255.255.254，192.0.1.1-223.255.255.254。<br>默认值：无<br>配置原则：<br>IPV4ADDRSTART一定要小于等于IPV4ADDREND。 |
| IPV4ADDREND | 服务节点IPV4地址段的结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于设定服务节点IP地址段的IPv4结束IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无<br>配置原则：<br>IPV4ADDRSTART一定要小于等于IPV4ADDREND。 |
| IPV6ADDRSTART | 服务节点IPV6地址段的起始地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定服务节点IP地址段的IPv6起始IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分隔十六进制格式。<br>默认值：无<br>配置原则：<br>IPV6ADDRSTART一定要小于等于IPV6ADDREND。 |
| IPV6ADDREND | 服务节点IPV6地址段的结束地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定服务节点IP地址段的IPv6结束IP地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。冒号分隔十六进制格式。<br>默认值：无<br>配置原则：<br>IPV6ADDRSTART一定要小于等于IPV6ADDREND。 |
| IPVERSION | IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址段的IP版本。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：IPv4地址类型<br>- “IPV6（IPV6）”：IPv6地址类型<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SRVNODEIP]] · 服务节点IP（SRVNODEIP）

## 使用实例

在根据SGSN IP进行虚拟APN映射的时候，需要绑定服务节点IP地址时使用如下命令：

```
ADD SRVNODEIP:GROUPNAME="huawei",IPSECTIONID=1,IPVERSION=IPV4,IPV4ADDRSTART="192.168.1.10",IPV4ADDREND="192.168.1.120";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加服务节点IP（ADD-SRVNODEIP）_09654166.md`
