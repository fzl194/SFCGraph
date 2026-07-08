---
id: UNC@20.15.2@MMLCommand@TST GTPCPATHINFO
type: MMLCommand
name: TST GTPCPATHINFO（测试GTP-C路径以及查询非知名端口号范围）
nf: UNC
version: 20.15.2
verb: TST
object_keyword: GTPCPATHINFO
command_category: 调测类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# TST GTPCPATHINFO（测试GTP-C路径以及查询非知名端口号范围）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

- 该命令用于通过发送Echo请求消息的方法测试本端与对端之间的GTP-C路径是否正常。如果路径正常，则返回报文显示路径地址信息；如果路径不正常，则返回报文显示65697或20111错误码。
- 该命令用于查询非知名端口号范围。

## 注意事项

- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令TST GTPCPATH测试。
- 使用该命令连续探测相同地址的GTP-C路径会失败，建议等待2min后重新探测。
- 该命令探测过程中临时会产生一条维护路径，探测结束后删除该维护路径。该命令探测只探测路径是否通断，与该路径上是否存在信令消息无关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 选择类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定命令的选择类型。<br>数据来源：全网规划<br>取值范围：<br>- OP_Tst_GtpcPath（探测GTPC路径）<br>- OP_Query_PortScope（查询非知名端口号范围）<br>默认值：无<br>配置原则：无 |
| GTPVER | GTP版本 | 可选必选说明：该参数在"OPTYPE"配置为"OP_Tst_GtpcPath"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的版本号。<br>数据来源：全网规划<br>取值范围：<br>- GTPv1（GTPv1）<br>- GTPv2（GTPv2）<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：该参数在"OPTYPE"配置为"OP_Tst_GtpcPath"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPTypeV4（IPv4类型）”：IPTypeV4<br>- “IPTypeV6（IPv6类型）”：IPTypeV6<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV4"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>业务地址必须是A、B或者C类地址。 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的本端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPTypeV6"时为条件必选参数。<br>参数含义：该参数用于指定GTP-C路径的对端IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| SRCPORT | 源端口号 | 可选必选说明：该参数在"OPTYPE"配置为"OP_Tst_GtpcPath"时为条件可选参数。<br>参数含义：该参数用于指定GTP-C路径发送Echo请求消息的源端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是2123，14001~14509。<br>默认值：2123<br>配置原则：无 |

## 操作的配置对象

- [GTP-C路径（GTPCPATHINFO）](configobject/UNC/20.15.2/GTPCPATHINFO.md)

## 使用实例

- 测试本端与对端之间的GTP-C路径是否正常，路径版本为GTPv2，IP地址类型为IPTypeV4，本端IP地址为10.2.125.26，对端IP地址为10.2.125.27;
  ```
  %%TST GTPCPATHINFO: OPTYPE=OP_Tst_GtpcPath, GTPVER=GTPv2, IPTYPE=IPTypeV4, LOCALIPV4="10.2.125.26", PEERIPV4="10.2.125.27";%%
  RETCODE = 0  操作成功

  结果如下
  --------
       GTP版本  =  GTPv2
    IP地址类型  =  IPV4类型
  本端IPv4地址  =  10.2.125.26
  对端IPv4地址  =  10.2.125.27
  (结果个数 = 1)

  ---    END
  ```
- 查询非知名端口号范围，起始端口号为14001，结束端口号为14127.
  ```
  %%TST GTPCPATHINFO: OPTYPE=OP_Query_PortScope;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  起始端口号  =  14001
  结束端口号  =  14127
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/测试GTP-C路径以及查询非知名端口号范围（TST-GTPCPATHINFO）_09653181.md`
