---
id: UNC@20.15.2@MMLCommand@ADD CG
type: MMLCommand
name: ADD CG（配置CG）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CG
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG管理
status: active
---

# ADD CG（配置CG）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

ADD CG命令用来添加一条CG配置信息。当用户进行离线计费时，需要配置CG接收离线计费生成的话单。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32。
- 当前版本不支持此命令的REALMNAME参数。
- 配置WALVALUE值进行流控时，存在一定误差，非精准流控。建议配置WALVALUE值为10*Ga逻辑接口数的整数倍。
- 要配置此命令的GAPORT参数，需要先配置SET CONCENPOINT命令的GaConcenMode参数配置为SINGLE_CONNECT并且byte780 bit4置为1，否则GAPORT参数不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | CG IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CG IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：IPV4<br>配置原则：无 |
| IPV4ADDR | CG IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：CG服务器的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | CG IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：CG服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | CG端口号 | 可选必选说明：必选参数<br>参数含义：CG服务器的端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 等级 | 可选必选说明：必选参数<br>参数含义：CG服务器的等级。值越小优先级越高，即0的优先级最高，100的优先级最低。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |
| CDRTYPE | 话单类型 | 可选必选说明：必选参数<br>参数含义：CG服务器的话单类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- R98：表示CG服务器的话单类型是R98。<br>- R99：表示CG服务器的话单类型是R99。<br>- R4：表示CG服务器的话单类型是R4。<br>- R5：表示CG服务器的话单类型是R5。<br>- R6：表示CG服务器的话单类型是R6。<br>- R7：表示CG服务器的话单类型是R7。<br>- R8_SGW：表示CG服务器的话单类型是R8_SGW。<br>- R8_PGW：表示CG服务器的话单类型是R8_PGW。<br>- R9_SGW：表示CG服务器的话单类型是R9_SGW。<br>- R9_PGW：表示CG服务器的话单类型是R9_PGW。<br>- R10_SGW：表示CG服务器的话单类型是R10_SGW。<br>- R10_PGW：表示CG服务器的话单类型是R10_PGW。<br>- R8_ALL：表示CG服务器的话单类型是R8_ALL。<br>- R9_ALL：表示CG服务器的话单类型是R9_ALL。<br>- R10_ALL：表示CG服务器的话单类型是R10_ALL。<br>默认值：无<br>配置原则：无 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UNC）每秒发送给该CG（含port）的最大话单数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：<br>- 缺省为0，表示不控制话单数。<br>- 不配置此参数时值默认为0。 |
| REALMNAME | CG域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| GAPORT | Ga本端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定通过Ga接口与对端建链时的源端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0，10551～10600。<br>默认值：无<br>配置原则：<br>- 在SET CONCENPOINT命令的GaConcenMode参数配置为SINGLE_CONNECT并且byte780 bit4置为1时生效。<br>- 不能配置相同的GaPort。<br>- 配置为0表示不指定源端口号。<br>- 不配置此参数时值默认为0。 |

## 操作的配置对象

- [CG（CG）](configobject/UNC/20.15.2/CG.md)

## 使用实例

增加CG，CG的IP地址为192.168.0.2，CG的端口号为25009，CG的等级为1，话单的类型为R9_PGW：

```
ADD CG:IPVERSION=IPV4, IPV4ADDR="192.168.0.2",PORT=25009,PRIORITY=1,CDRTYPE=R9_PGW;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置CG（ADD-CG）_09896845.md`
