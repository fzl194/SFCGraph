---
id: UNC@20.15.2@MMLCommand@LST HOMEPGWIP
type: MMLCommand
name: LST HOMEPGWIP（查询归属地PGW-C IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HOMEPGWIP
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- 归属地PGW-C IP地址
status: active
---

# LST HOMEPGWIP（查询归属地PGW-C IP地址）

## 功能

**适用NF：SGW-C**

该命令用于Proxy S-GW特性中查询用户指定的归属地PGW-C的IP地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：本端规划<br>取值范围：<br>- IMSI_PRE（IMSI前缀 ）<br>- MSISDN_PRE（MSISDN前缀）<br>默认值：无<br>配置原则：<br>IMSI_PRE和MSISDN_PRE记录的优先级受SET PROXYSGWFUNC命令中的QUERYTYPE参数控制。 |
| PREFIX | 前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PRE"、"MSISDN_PRE"时为条件可选参数。<br>参数含义：该参数用于指定用户号码前缀。当参数SUBRANGE为"IMSI_PRE"时，本参数表示IMSI号码前缀，当参数SUBRANGE为"MSISDN_PRE"时，本参数表示MSISDN号码前缀。使用时按照最长匹配进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。<br>默认值：无<br>配置原则：<br>取值范围为1~15位数字。 |
| IPVERSION | IP地址版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定归属地PGW的IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4（IPV4）”：表示地址类型为IPv4<br>- “IPV6（IPV6）”：表示地址类型为IPv6<br>默认值：无<br>配置原则：无 |
| HOMEIPV4 | IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于指定归属地PGW的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。 |
| HOMEIPV6 | IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于指定归属地PGW的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOMEPGWIP]] · 归属地PGW-C IP地址（HOMEPGWIP）

## 使用实例

查询所有用户归属地PGW-C IP地址，执行如下命令：

```
%%LST HOMEPGWIP:;%%
RETCODE = 0  操作成功

结果如下
--------
      用户范围  =  IMSI前缀
          前缀  =  12303
IP地址版本类型  =  IPV4
      IPv4地址  =  10.0.0.0
      IPv6地址  =  ::
      描述信息  =  desc
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询归属地PGW-C-IP地址（LST-HOMEPGWIP）_06399912.md`
