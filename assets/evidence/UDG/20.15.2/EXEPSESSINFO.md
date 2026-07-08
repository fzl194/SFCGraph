# 显示异常用户（DSP EXEPSESSINFO）

- [命令功能](#ZH-CN_CONCEPT_0000207268465266__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000207268465266__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000207268465266__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000207268465266__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000207268465266__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000207268465266__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000207268465266)

**适用NF：UPF、PGW-U、SGW-U**

该命令通过查询异常用户，来获取异常用户的信息。

#### [注意事项](#ZH-CN_CONCEPT_0000207268465266)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000207268465266)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000207268465266)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCENE | 异常用户场景 | 可选必选说明：必选参数<br>参数含义：异常用户场景。<br>数据来源：本端规划<br>取值范围：<br>- DATAFWD：数据转发异常用户场景。<br>默认值：无<br>配置原则：无 |
| DATAFWD | 数据转发异常用户场景 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SCENE”配置为“DATAFWD”时为必选参数。<br>参数含义：数据转发异常用户场景。<br>数据来源：本端规划<br>取值范围：<br>- ABNPKTATT：异常报文攻击用户。<br>- ABNDNS：异常DNS访问用户。<br>默认值：无<br>配置原则：无 |
| MESSAGETYPE | 异常报文类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DATAFWD”配置为“ABNPKTATT”时为必选参数。<br>参数含义：异常报文类型。<br>数据来源：本端规划<br>取值范围：<br>- IPHDR：IP类型非v4或v6。<br>- UDPHDR：用户UDP协议的IPv4报文实际的长度小于(IPv4头长度+UDP头长度)。<br>- TCPHDR：用户TCP协议的IPv4报文实际的长度小于(IPv4头长度+TCP头长度)。<br>- IPLEN：报文长度（从IP头开始计算）小于IP头中的total length的值。<br>- DSTIP：上行目的地址非法(地址是0/环回)。<br>- ANTISPOOFING：报文anti-spoofing检查不过丢包。<br>- CHECKSUM：报文checksum检查错误丢包。<br>- TTL：上行用户IPv4/IPv6报文TTL小于等于1。<br>- V6EXTHDRLEN：IPv6报文的扩展头错误。<br>- EXCPFRAG：用户分片报文过多，分片资源耗尽丢包。<br>- DDOS：上行IPv4或者IPv6报文DDOS攻击丢包。<br>- FLOODATT：上行或者下行大流量攻击丢包。<br>- MUTICAST：上行目的地址为组播广播。<br>- FRAGMNODE：分片母节点耗尽丢包。<br>默认值：无<br>配置原则：无 |
| DNSIPTYPE | 异常DNS地址类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DATAFWD”配置为“ABNDNS”时为可选参数。<br>参数含义：异常DNS地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| DNSIPV4 | DNSIPV4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNSIPTYPE”配置为“IPv4”时为必选参数。<br>参数含义：DNSIPV4地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |
| DNSIPV6 | DNSIPV6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DNSIPTYPE”配置为“IPv6”时为必选参数。<br>参数含义：DNSIPV6地址。<br>数据来源：本端规划<br>取值范围：NA。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000207268465266)

- 查询DDOS异常攻击报文用户的信息：
  ```
  DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNPKTATT, MESSAGETYPE=DDOS;
  ```
  ```

  %%DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNPKTATT, MESSAGETYPE=IPHDR;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Abnormal user information  =  
  ATT reason = The IP header of the packet is incorrect
  Record user number = 0
  PodName = ssgpod-0
  (结果个数 = 1)

  ---    END
  ```
- 查询异常DNS访问用户的信息：
  ```
  DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNDNS;
  ```
  ```

  %%DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNDNS;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Abnormal user information  =  
  PodName = ssgpod-0
  	DnsIpAddr[10.1.2.3]
  	    imsi(26456789012342):
  	        msIp[10.1.2.4],severIp[10.1.2.3],msPort[22222],serverPort[53],l4Protocol[17],upDnsNum[22],downDnsNum[10]

  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000207268465266)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 异常用户信息 | 异常用户信息。 |
