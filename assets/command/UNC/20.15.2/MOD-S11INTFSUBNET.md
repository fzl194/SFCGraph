---
id: UNC@20.15.2@MMLCommand@MOD S11INTFSUBNET
type: MMLCommand
name: MOD S11INTFSUBNET（修改S11接口子网配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: S11INTFSUBNET
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GWIP地址配置
status: active
---

# MOD S11INTFSUBNET（修改S11接口子网配置）

## 功能

**适用网元：MME**

此命令用于修改S11或S11-U接口的子网配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令在版本升级过程中禁止执行。
- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，“本端IPV4地址”或“本端IPV6地址”通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。
- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，“本端IPV4地址”或“本端IPV6地址”通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKIDX | 链路关联索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本对端IP地址关联索引。<br>取值范围：0~65534<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | 远端实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端局向NF实例号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40<br>默认值：无<br>配置原则：无 |
| INTFTYPE | S11接口类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定S11接口类型。<br>取值范围：<br>- “INTFTYPE_S11 (S11接口)”<br>- “INTFTYPE_S11-U (S11-U接口)”<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：指定关联的IP地址类型<br>取值范围：<br>- “IPV4 (IPV4)”<br>- “IPV6 (IPV6)”<br>默认值：IPV4<br>配置原则：无 |
| LOCALIPV4 | 本端IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：本端IPV4地址<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型，0.0.0.0~255.255.255.255。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。 |
| PEERIPV4 | 对端IPV4地址 | 可选必选说明：条件可选参数<br>参数含义：S-GW地址。<br>数据来源：全网规划<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型。0.0.0.0~255.255.255.255。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，表示DNS中配置的S-GW地址。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，表示S-GW分配的S11-U地址。 |
| IPV4MASK | IPV4掩码 | 可选必选说明：条件可选参数<br>参数含义：IPV4掩码<br>前提条件：“IP地址类型”参数需要设置为“IPV4”。<br>取值范围：IPv4地址类型。0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCALIPV6 | 本端IPV6地址 | 可选必选说明：条件可选参数<br>参数含义：本端IPV6地址<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：IPv6地址类型，::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，通过执行**[LST GTPCLE](../../Gtpc本端实体管理/查询GTP-C本地实体(LST GTPCLE)_72345567.md)**命令查询获取。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，通过执行**[LST GTPULE](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)**命令查询获取。 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：S-GW地址。<br>数据来源：全网规划<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- “S11接口类型”参数选为“INTFTYPE_S11(S11接口)”时，表示DNS中配置的S-GW地址。<br>- “S11接口类型”参数选为“INTFTYPE_S11-U(S11-U接口)”时，表示S-GW分配的S11-U地址。 |
| IPV6MASK | IPV6掩码 | 可选必选说明：条件可选参数<br>参数含义：IPV6掩码<br>前提条件：“IP地址类型”参数需要设置为“IPV6”。<br>取值范围：整数类型，取值范围0~128。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S11INTFSUBNET]] · S11接口子网配置（S11INTFSUBNET）

## 使用实例

1. 修改关联索引为0的S11接口子网配置，可以用如下命令：
  ```
  MOD S11INTFSUBNET: LNKIDX=0, NFINSTANCEID="huawei", INTFTYPE=INTFTYPE_S11, IPTYPE=IPV4, LOCALIPV4="192.168.52.1", PEERIPV4="192.168.52.2", IPV4MASK="255.255.255.255";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改S11接口子网配置-(MOD-S11INTFSUBNET)_19337295.md`
