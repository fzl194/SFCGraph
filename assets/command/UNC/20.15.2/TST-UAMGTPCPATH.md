---
id: UNC@20.15.2@MMLCommand@TST UAMGTPCPATH
type: MMLCommand
name: TST UAMGTPCPATH（测试UAM GTP-C路径状态）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: UAMGTPCPATH
command_category: 调测类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# TST UAMGTPCPATH（测试UAM GTP-C路径状态）

## 功能

**适用NF：SGSN、MME、AMF**

该命令已废弃，建议使用TST GTPCPATH或者TST GTPCPATHINFO测试GTP-C路径状态。

该命令用于测试UAM GTP-C路径状态。

## 注意事项

探测IPV4地址时，结果中本对端IPV6显示为：：。探测IPV6地址时，结果中本对端IPV4显示为255.255.255.255。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的GTP版本号。<br>数据来源：本端规划<br>取值范围：GTPV0只适用于MME/SGSN。<br>- GTPV0（GTP V0）<br>- GTPV1（GTP V1）<br>- GTPV2（GTP V2）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPV4）<br>- IPV6（IPV6）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [测试UAM GTP-C路径状态（UAMGTPCPATH）](configobject/UNC/20.15.2/UAMGTPCPATH.md)

## 使用实例

TST UAMGTPCPATH: GTPVER=GTPV2, IPTYPE=IPV4, LOCALIPV4="192.168.138.2", PEERIPV4="10.70.240.1";

```
%%TST UAMGTPCPATH: GTPVER=GTPV2, IPTYPE=IPV4, LOCALIPV4="192.168.138.2", PEERIPV4="10.70.240.1";%%
RETCODE = 0  操作成功

结果如下
------------------------
       GTP版本  =  GTP V2
本端IPv4地址  =  192.168.138.2
本端IPv6地址  =  ::
 对端IPv4地址  =  10.70.240.1
 对端IPv6地址  =  ::
        网元类型  =  AMF
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试UAM-GTP-C路径状态（TST-UAMGTPCPATH）_71436561.md`
