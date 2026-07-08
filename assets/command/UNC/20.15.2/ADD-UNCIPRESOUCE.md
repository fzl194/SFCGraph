---
id: UNC@20.15.2@MMLCommand@ADD UNCIPRESOUCE
type: MMLCommand
name: ADD UNCIPRESOUCE（增加UNC接口IP地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UNCIPRESOUCE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# ADD UNCIPRESOUCE（增加UNC接口IP地址）

## 功能

**适用NF：SGSN、MME、SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于增加需要上报给网管北向的UNC网元业务和管理接口的IP地址。需要在网管北向上查看UNC网元业务和管理接口的IP地址时，可以通过此命令进行配置。

## 注意事项

- 该命令执行后立即生效。

- 当UNC各接口不存在有效IP地址信息时，将生成IP地址为0.0.0.0的无效默认记录，系统部署完成后，UNC的43个接口将各存在一条无效默认记录，共43条记录；当向UNC的接口添加有效IP地址信息时，对应接口的无效默认记录将被删除；UNC接口的有效记录和默认记录共计可存在最多8192条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UNC网元的接口名称。其中，Mgt为网元和网管的对接接口；DnsQry为SGSN、MME、AMF网元的DNS本端实体与DNS服务器进行通信的接口；Bx为NCG网元与计费账务域交互的文件接口；其他为协议定义的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址的类型。<br>数据来源：本端规划<br>取值范围：<br>- “IPv4（IPv4）”：IPv4<br>- “IPv6（IPv6）”：IPv6<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于表示对应网元接口的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>- IPv4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- IPv4地址必须是A、B或者C类地址。<br>- IPv4地址在系统内必须唯一。<br>- IPv4地址为上报给网管北向UNC网元的所有业务和管理接口地址，业务接口地址获取方式以AMF网元的N2接口为例，先执行LST NGAPLE命令，从查询结果中获取“SCTP本端实体组索引”，再使用该“SCTP本端实体组索引”为查询条件，执行LST SCTPLE命令，从查询结果中获取“本端IPv4地址1”和“本端IPv4地址2”中的有效IPv4地址。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于表示对应网元接口的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、2001:X:X:X:X:X::、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。<br>- 不能配置与外联口IP地址相同的IP地址。<br>- IPv6地址为上报给网管北向UNC网元的所有业务和管理接口地址，业务接口地址获取方式以AMF网元的N2接口为例，先执行LST NGAPLE命令，从查询结果中获取“SCTP本端实体组索引”，再使用该“SCTP本端实体组索引”为查询条件，执行LST SCTPLE命令，从查询结果中获取“本端IPv6地址1”和“本端IPv6地址2”中的有效IPv6地址。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UNCIPRESOUCE]] · UNC接口IP地址（UNCIPRESOUCE）

## 使用实例

- 新增需要上报给网管北向的UNC网元业务或者管理接口的IP地址，其接口为N4，IPv4地址为10.1.3.11，执行以下命令：
  ```
  ADD UNCIPRESOUCE: INTFTYPE="N4", IPTYPE=IPv4, IPV4="10.1.3.11";
  ```
- 新增需要上报给网管北向的UNC网元业务或者管理接口的IP地址，其接口为N4，IPv6地址为2001:0DB8:0:0:0:800:200C:510A，执行以下命令：
  ```
  ADD UNCIPRESOUCE: INTFTYPE="N4", IPTYPE=IPv6, IPV6="2001:0DB8:0:0:0:800:200C:510A";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UNCIPRESOUCE.md`
