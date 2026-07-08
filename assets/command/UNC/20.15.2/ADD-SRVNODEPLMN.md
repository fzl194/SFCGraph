---
id: UNC@20.15.2@MMLCommand@ADD SRVNODEPLMN
type: MMLCommand
name: ADD SRVNODEPLMN（增加SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SRVNODEPLMN
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取PLMN管理
- 服务节点PLMN
status: active
---

# ADD SRVNODEPLMN（增加SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来配置SGSN/SGW/PGW IP与PLMN标识的映射关系表。在根据SGSN/SGW的IP地址映射PLMN时，需要用到映射表。获取SGSN/SGW/PGW PLMN标识用于判断用户的本地、漫游和拜访属性。

## 注意事项

- 该命令执行后立即生效。

- 多条记录之间的SGSN地址不能重叠。
- 修改配置后，会对用户的本地、漫游和拜访属性的判断结果发生变化，会影响用户的计费和业务控制。对后续接入的用户有效。

- 最多可输入5000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVNODEPLMN | PLMN信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定的SGSN/SGW/PGW IP地址段所对应的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。字符串长度取值范围：5~6。PLMN字符串的格式为MCCMNC，MCC长度为3个字符，MNC长度为2或者3个字符。<br>默认值：无<br>配置原则：无 |
| IPVERSION | ip类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示IP类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODESTARTV4 | Service Node的起始IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于SGSN/SGW/PGW IP地址段的起始IPV4地址，该配置需要和全网规划一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODEENDV4 | Service Node的结束IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于SGSN/SGW/PGW IP地址段的结束IPV4地址，该配置需要和全网规划一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>取值范围：0.0.0.0~255.255.255.255。 |
| SRVNODESTARTV6 | Service Node的起始IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定Serving Node IP地址段的IPv6起始IP地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEENDV6 | Service Node的结束IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于设定Serving Node IP地址段的IPv6结束IP地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| ROAMINGSEL | 漫游选择 | 可选必选说明：可选参数<br>参数含义：该参数用于标识是否使用运营商定制方式判断漫游状态进行UPF选择。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：DISABLE<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SRVNODEPLMN]] · SGSN/SGW/PGW地址段和PLMN标识之间的映射关系（SRVNODEPLMN）

## 使用实例

配置SGSN/SGW/PGW地址段和PLMN标识之间的映射关系实例， PLMN为666666，ip类型为IPV4，Service Node的起始IPv4地址为10.111.111.111，Service Node的结束IPv4地址为：10.111.111.255：

```
ADD SRVNODEPLMN: SRVNODEPLMN="666666", IPVERSION=IPV4, SRVNODESTARTV4="10.111.111.111", SRVNODEENDV4="10.111.111.255", ROAMINGSEL=DISABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SRVNODEPLMN.md`
