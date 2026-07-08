---
id: UNC@20.15.2@MMLCommand@MOD CG
type: MMLCommand
name: MOD CG（修改CG）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CG
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG管理
status: active
---

# MOD CG（修改CG）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

![](修改CG（MOD CG）_09896846.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，修改对端信息可能导致无可用CG，话单无法被正常处理，进而影响计费。

MOD CG命令用来在CG配置表中修改一个CG信息。

## 注意事项

- 该命令执行后立即生效。
- CG配置表中必须要存在对应的以地址和端口标识的CG，用户只能修改CG的等级和WAL值。
- 修改GaPort将导致链路重建。
- 当前版本不支持此命令的REALMNAME。
- 配置WALVALUE值进行流控时，存在一定误差，非精准流控。建议配置WALVALUE值为10*Ga逻辑接口数的整数倍。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | CG IP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定CG IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：IPv4。<br>- IPV6：IPv6。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR | CG IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：CG服务器的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR | CG IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：CG服务器的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PORT | CG端口号 | 可选必选说明：必选参数<br>参数含义：CG服务器的端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |
| PRIORITY | 等级 | 可选必选说明：必选参数<br>参数含义：CG服务器的等级。值越小优先级越高，即0的优先级最高，100的优先级最低。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～100。<br>默认值：无<br>配置原则：无 |
| WALVALUE | wal值 | 可选必选说明：可选参数<br>参数含义：该参数表示整机（UNC）每秒发送给该CG（含port）的最大话单数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：缺省为0，表示不控制话单数。 |
| REALMNAME | CG域名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端域名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| GAPORT | Ga本端端口 | 可选必选说明：可选参数<br>参数含义：该参数用于指定通过Ga接口与对端建链时的源端口号。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0，10551～10600。<br>默认值：无<br>配置原则：<br>- 在SET CONCENPOINT命令的GaConcenMode参数配置为SINGLE_CONNECT并且byte780 bit4置为1时生效。<br>- 不能配置相同的GaPort。<br>- 配置为0表示不指定源端口号。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CG]] · CG（CG）

## 使用实例

修改CG，将IP地址为192.168.0.2，端口号为25009的CG服务器的等级修改为10：

```
MOD CG:IPVERSION=IPV4, IPV4ADDR="192.168.0.2",PORT=25009,PRIORITY=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改CG（MOD-CG）_09896846.md`
