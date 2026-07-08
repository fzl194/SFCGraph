---
id: UNC@20.15.2@MMLCommand@LST LOCRPTCFG
type: MMLCommand
name: LST LOCRPTCFG（查询位置上报配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCRPTCFG
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-GGSN_S5_S8接口管理
- P-GW属性
status: active
---

# LST LOCRPTCFG（查询位置上报配置信息）

## 功能

**适用网元：SGSN、MME**

该命令用于查询位置上报配置信息。

## 注意事项

- 该命令执行后立即生效。
- 当不输入查询条件时，显示所有记录信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要位置上报配置信息的对端设备GGSN/P-GW范围<br>取值范围：<br>- “ALL_GGSN/P-GW（所有GGSN/P-GW）”<br>- “HOME_GGSN/P-GW（本网GGSN/P-GW）”<br>- “FOREIGN_GGSN/P-GW（外网GGSN/P-GW）”<br>- “SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”<br>默认值： 无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IP地址类型。<br>前提条件：只有在<br>“RANGE”<br>配置为<br>“SPECIFIC_GGSN/P-GW（指定IP的GGSN/P-GW）”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| GWIPV4 | GGSN/P-GW的信令面IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IPv4地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值：无<br>说明：- 有效的IPv4地址不能为0.0.0.0、255.255.255.255和环回地址（127.x.y.z）。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| MASKV4 | 掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端GGSN/P-GW的信令面IPv4地址的掩码<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV4”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0～255.255.255.255<br>默认值： 无<br>说明：- “0.0.0.0”是无效掩码。<br>- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| GWIPV6 | GGSN/P-GW的信令面IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GGSN/P-GW信令面IPv6地址。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：只有在<br>“IPT”<br>配置为<br>“IPV6”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：1～128（数值型）<br>默认值： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCRPTCFG]] · 位置上报配置信息（LOCRPTCFG）

## 使用实例

查询位置上报配置信息:

LST LOCRPTCFG:;

```
%%LST LOCRPTCFG:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
 对端设备范围       IP地址类型  GGSN/P-GW的信令面IPv4地址  掩码             GGSN/P-GW的信令面IPv6地址    子网前缀长度    支持位置上报功能  描述         

 所有GGSN/P-GW      NULL        0.0.0.0                    0.0.0.0          2001:db8:10:19:44:55:10:15    0               否                NULL         
 指定IP的GGSN/P-GW  IPV4        10.141.149.100             255.255.255.255  2001:db8:10:19:44:55:10:18    0               否                GGSN01
 本网GGSN/P-GW      NULL        0.0.0.0                    0.0.0.0          2001:db8:10:19:44:55:10:64    0               否                NULL         
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询位置上报配置信息(LST-LOCRPTCFG)_72225617.md`
