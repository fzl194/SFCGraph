# 删除Diameter对端地址（RMV DIAMPEERADDR）

- [命令功能](#ZH-CN_CONCEPT_0209897258__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897258__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897258__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897258__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897258__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897258)

**适用NF：PGW-C、SMF**

![](删除Diameter对端地址（RMV DIAMPEERADDR）_09897258.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除DiamPeerAddr会导致正在使用的Diameter链路异常，中断Diameter应用相关的业务。

该命令用于删除Diameter链路的对端地址信息。

当某应用Diameter协议的服务器需要减少Diameter链路的对端地址时，执行此命令。

#### [注意事项](#ZH-CN_CONCEPT_0209897258)

- 该命令执行后立即生效。
- 当未指定地址类型时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 删除Diameter链路的对端地址信息时，必须输入地址所属的主机名称，并且该主机在UNC上已经配置。
- 删除Diameter链路的对端地址时，对应的Diameter链路也会同时删除。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897258)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897258)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 主机名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址信息所属的Diameter主机名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：无 |
| ADDRTYPE | 地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter地址的地址类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- IPv4：地址类型为IPv4。<br>- IPv6：地址类型为IPv6。<br>- SCTP：地址类型为SCTP端点。<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。不支持0.0.0.0和255.255.255.255。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。不支持全F。<br>默认值：无<br>配置原则：无 |
| PORT | 端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ADDRTYPE”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定IP地址的端口号。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1～65534。<br>默认值：无<br>配置原则：无 |
| SCTPENDPOINT | SCTP端点名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRTYPE”配置为“SCTP”时为必选参数。<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897258)

- 当用户需要重新配置Diameter主机“ocs1”的所有对端地址信息，则需要先删除该OCS主机的所有地址：
  ```
  RMV DIAMPEERADDR:HOSTNAME="ocs1";
  ```
- 当用户识别出对端Diameter主机不支持SCTP传输协议，需要删除Diameter主机“ocs1”的SCTP对端地址“end1”信息：
  ```
  RMV DIAMPEERADDR:HOSTNAME="ocs1",ADDRTYPE=SCTP,SCTPENDPOINT="end1";
  ```
