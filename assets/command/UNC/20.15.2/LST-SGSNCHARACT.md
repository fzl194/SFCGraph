---
id: UNC@20.15.2@MMLCommand@LST SGSNCHARACT
type: MMLCommand
name: LST SGSNCHARACT（查询GnGp SGSN属性配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSNCHARACT
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GnGp-SGSN_S10_S16_S3接口管理
- GnGp SGSN属性
status: active
---

# LST SGSNCHARACT（查询GnGp SGSN属性配置信息）

## 功能

**适用网元：SGSN**

该命令用于查询SGSN的QoS属性信息。

## 注意事项

- 该命令执行后立即生效。
- 当不输入查询条件时，显示所有记录信息。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 对端设备范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端设备的范围。<br>数据来源：整网规划<br>取值范围：<br>“ALL_SGSN(所有SGSN)”<br>、<br>“SPECIAL_SGSN(指定SGSN)”<br>默认值： 无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端SGSN的信令面IP地址类型。<br>前提条件：当对端设备类型为<br>“SPECIAL_SGSN(指定SGSN)”<br>时显示。<br>数据来源：整网规划<br>取值范围：<br>“IPV4”<br>、<br>“IPV6”<br>默认值：无<br>配置原则：<br>- IPV4，表示对端SGSN的信令面IP地址为IPv4类型。<br>- IPV6，表示对端SGSN的信令面IP地址为IPv6类型。 |
| IPV4 | SGSN IPv4信令面地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPv4地址。<br>前提条件：当<br>“IPT(IP地址类型)”<br>为<br>“IPV4”<br>时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.254<br>默认值： 无<br>配置原则：<br>- 有效的IPv4地址不能为环回地址(127.x.y.z)。<br>- 有效的IPv4地址必须是A、B或者C类地址。 |
| MASKV4 | 掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端SGSN的信令面IPv4地址的掩码。<br>前提条件：当<br>“IPT(IP地址类型)”<br>为<br>“IPV4”<br>时显示。<br>数据来源：整网规划<br>取值范围：0.0.0.1～255.255.255.255<br>默认值： 无<br>说明：- 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。 |
| IPV6 | SGSN IPv6信令面地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN配置的信令面IPv6地址。<br>前提条件：当<br>“IPT(IP地址类型)”<br>为<br>“IPV6”<br>时显示。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| MASKV6 | 子网前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子网前缀的长度。<br>前提条件：当<br>“IPT(IP地址类型)”<br>为<br>“IPV6”<br>时显示。<br>数据来源：整网规划<br>取值范围：1～128（数值型）<br>默认值： 无 |

## 操作的配置对象

- [GnGp SGSN属性配置信息（SGSNCHARACT）](configobject/UNC/20.15.2/SGSNCHARACT.md)

## 使用实例

不输入查询条件，查询表中全部SGSN的属性信息：

LST SGSNCHARACT:;

```
%%LST SGSNCHARACT:;%%
RETCODE = 0  操作成功。

所有SGSN查询结果如下
-------------------------
                               对端设备范围  =  所有SGSN
                          SGSN支持的QoS版本  =  R99QOS
                  Gn接口的GTP-C路径版本规则  =  V1
是否支持在SGSN CONTEXT RSP消息中携带RAT信元  =  否
                   是否携带扩展接入限制数据  =  是
                                       描述  =  NULL
仍有后续报告输出
---   END

%%LST SGSNCHARACT:;%%
RETCODE = 0  操作成功。

指定SGSN IPv4查询结果如下
--------------
对端设备范围    IP地址类型    SGSN IPv4信令面地址    掩码               SGSN支持的QoS版本    Gn接口的GTP-C路径版本规则    是否支持在SGSN CONTEXT RSP消息中携带RAT信元    是否携带扩展接入限制数据    描述   

指定SGSN        IPV4          192.168.168.12         255.255.255.255    R99QOS               V1                           否                                             否                          NULL
指定SGSN        IPV4          192.168.168.13         255.255.255.255    R99QOS               V1                           否                                             是                          NULL   
(结果个数 = 3)
共2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GnGp-SGSN属性配置信息(LST-SGSNCHARACT)_26145956.md`
