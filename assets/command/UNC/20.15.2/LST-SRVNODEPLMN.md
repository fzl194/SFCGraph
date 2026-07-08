---
id: UNC@20.15.2@MMLCommand@LST SRVNODEPLMN
type: MMLCommand
name: LST SRVNODEPLMN（查询SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SRVNODEPLMN
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
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

# LST SRVNODEPLMN（查询SGSN/SGW/PGW地址段和PLMN标识之间的映射关系）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来查询SGSN/SGW/PGW IP与PLMN标识的映射关系表。查询SGSN/SGW/PGW PLMN标识用于判断用户的本地、漫游和拜访属性。

## 注意事项

- 不输入参数时可以查询所有的SGSN/SGW/PGW地址段和PLMN标识之间的映射关系。
- QueryType等于IPTYPE时，表示基于IP类型查询记录。
- QueryType等于SrvNodePLMN时，表示基于指定的SGSN/SGW/PGW IP地址段所对应的PLMN信息查询记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- “IP（Service Node IP）”：通过IP地址查询IP与PLMN标识的映射关系。<br>- “PLMN（PLMN）”：表示通过PLMN信息查询IP与PLMN标识的映射关系。<br>默认值：无<br>配置原则：无 |
| SRVNODEPLMN | PLMN信息 | 可选必选说明：该参数在"QUERYTYPE"配置为"PLMN"时为条件必选参数。<br>参数含义：该参数用于指定的SGSN/SGW/PGW IP地址段所对应的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~6。字符串长度取值范围：5~6。PLMN字符串的格式为MCCMNC，MCC长度为3个字符，MNC长度为2或者3个字符。<br>默认值：无<br>配置原则：无 |
| IPVERSION | ip类型 | 可选必选说明：该参数在"QUERYTYPE"配置为"IP"时为条件必选参数。<br>参数含义：该参数用于指示IP类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4。<br>- “IPV6（IPV6）”：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRVNODEPIP | Service Node的IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示SGSN/SGW/PGW IPV4地址段IP。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| SRVNODEPIPV6 | Service Node IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指示SGSN/SGW/PGW IPV6地址段IP。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SRVNODEPLMN]] · SGSN/SGW/PGW地址段和PLMN标识之间的映射关系（SRVNODEPLMN）

## 使用实例

当需要查询所有的SGSN/SGW/PGW地址段和PLMN标识之间的映射关系时，使用如下命令：

```
LST SRVNODEPLMN:;RETCODE = 0 操作成功

结果如下
------------------------
IP Address Version Type = IPV4
Service Node的起始IPv4地址 = 10.111.111.111
Service Node的结束IPv4地址 = 10.111.111.255
PLMN = 13210
漫游选择 = DISABLE
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SRVNODEPLMN.md`
