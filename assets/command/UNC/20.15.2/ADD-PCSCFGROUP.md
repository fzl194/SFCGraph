---
id: UNC@20.15.2@MMLCommand@ADD PCSCFGROUP
type: MMLCommand
name: ADD PCSCFGROUP（增加P-CSCF组配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PCSCFGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组
status: active
---

# ADD PCSCFGROUP（增加P-CSCF组配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加P-CSCF组配置。在规划IMS网络，配置P-CSCF服务器地址时，需要先执行该命令配置P-CSCF组。当P-CSCF服务器地址由DHCP服务器分配时，用户具体使用DHCP P-CSCF分组中的哪个P-CSCF地址由用户激活时外置DHCP服务器返回的响应消息决定。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPV4（IPV4）”：IPv4地址类型<br>- “IPV6（IPV6）”：IPv6地址类型<br>默认值：IPV4<br>配置原则：无 |
| ALLOCTYPE | P-CSCF获取方式 | 可选必选说明：可选参数<br>参数含义：该参数用于P-CSCF服务器地址分配方式。<br>数据来源：本端规划<br>取值范围：<br>- “LOCAL（本地分配）”：在网络规划p-cscf服务器地址由UNC本地配置的时，配置分组类型为LOCAL。<br>- “DHCP（DHCP分配）”：在网络规划p-cscf服务器地址由DHCP服务器分配时，配置分组类型为DHCP。<br>默认值：LOCAL<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFGROUP]] · P-CSCF组配置（PCSCFGROUP）

## 使用实例

当运营商规划使用IMS网络，需要配置IPV4地址类型的P-CSCF组，举例：

```
ADD PCSCFGROUP: GROUPNAME="mygroup", ALLOCTYPE=LOCAL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PCSCFGROUP.md`
