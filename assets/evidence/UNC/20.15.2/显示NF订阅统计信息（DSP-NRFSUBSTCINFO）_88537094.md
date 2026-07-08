# 显示NF订阅统计信息（DSP NRFSUBSTCINFO）

- [命令功能](#ZH-CN_MMLREF_0000001088537094__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088537094__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088537094__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088537094__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088537094__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088537094)

**适用NF：NRF**

该命令用于查询NF在NRF上的订阅统计信息。

## [注意事项](#ZH-CN_MMLREF_0000001088537094)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088537094)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088537094)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示查询订阅记录的查询类型。<br>数据来源：本端规划<br>取值范围：<br>- INSTANCEID（基于被订阅NF的实例标识查询）<br>- SRCIP（基于订阅请求方IP查询）<br>- SRCFQDN（基于订阅请求方FQDN查询）<br>- ALL（所有订阅记录）<br>- INNER（内部订阅记录）<br>默认值：无<br>配置原则：<br>INNER（内部订阅记录）该参数用于SCP和NRF联合部署场景。 |
| INSTANCEID | NF实例标识 | 可选必选说明：该参数在"QRYTYPE"配置为"INSTANCEID"时为条件可选参数。<br>参数含义：该参数表示被订阅NF的实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP类型 | 可选必选说明：该参数在"QRYTYPE"配置为"SRCIP"时为条件可选参数。<br>参数含义：该参数用于表示订阅方的IP类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于表示订阅方的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于表示订阅方的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| FQDN | 域名 | 可选必选说明：该参数在"QRYTYPE"配置为"SRCFQDN"时为条件必选参数。<br>参数含义：该参数用于表示订阅消息通知URI中的FQDN。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001088537094)

- 查询IP地址为10.10.10.10的NF的订阅统计信息，执行如下命令：
  ```
  DSP NRFSUBSTCINFO: QRYTYPE=SRCIP, IPTYPE=IPV4, IPV4="10.10.10.10";
  %%DSP NRFSUBSTCINFO: QRYTYPE=SRCIP, IPTYPE=IPV4, IPV4="10.10.10.10";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
      IP类型  =  IPv4
    IPv4地址  =  10.10.10.10
    IPv6地址  =  ::
  订阅记录数  =  0
        域名  =  topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org
  (结果个数 = 1)

  ---    END
  ```
- 查询域名为topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org的NF的订阅统计信息，执行如下命令：
  ```
  DSP NRFSUBSTCINFO: QRYTYPE=SRCFQDN, FQDN="topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org";
  %%DSP NRFSUBSTCINFO: QRYTYPE=SRCFQDN, FQDN="topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org";%%
  RETCODE = 0  操作成功

  结果如下
  --------
  NF实例标识  =  123e4567-e89b-12d3-a456-426655440000
      IP类型  =  IPv4
    IPv4地址  =  10.10.10.10
    IPv6地址  =  ::
  订阅记录数  =  0
        域名  =  topon.pgw-s5.app-nf001-03a011.nm.nm.node.epc.mnc000.mcc123.3gppnetwork.org
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001088537094)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IP类型 | 该参数用于表示订阅方的IP类型。<br>取值说明：<br>- IPV4（IPv4）<br>- IPV6（IPv6） |
| IPv4地址 | 该参数用于表示订阅方的IPv4地址。 |
| IPv6地址 | 该参数用于表示订阅方的IPv6地址。 |
| 订阅记录数 | 该参数用于表示查询的订阅记录数。 |
| NF实例标识 | 该参数表示被订阅NF的实例标识。 |
| 域名 | 该参数用于表示订阅消息通知URI中的FQDN。 |
