---
id: UNC@20.15.2@MMLCommand@LST NGDNSS
type: MMLCommand
name: LST NGDNSS（查询DNS服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGDNSS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- DNS客户端管理
status: active
---

# LST NGDNSS（查询DNS服务器）

## 功能

**适用NF：AMF**

该命令用于查看配置的DNS服务器信息，DNS服务器是网络中专门提供域名解析服务的服务器。

## 注意事项

如果不输入参数，则查询所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4 | IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV4"时为条件可选参数。<br>参数含义：该参数用于表示DNS服务器的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：<br>IPv4地址不能为0.0.0.0。 |
| IPV6 | IPv6地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPV6"时为条件可选参数。<br>参数含义：该参数用于表示DNS服务器的IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：<br>IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。 |
| PRI | DNS服务器优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNS服务器被选择使用的优先级，“服务器优先等级1”的优先级最高。<br>数据来源：本端规划<br>取值范围：<br>- PRI1（服务器优先等级1）<br>- PRI2（服务器优先等级2）<br>- PRI3（服务器优先等级3）<br>- PRI4（服务器优先等级4）<br>- PRI5（服务器优先等级5）<br>- PRI6（服务器优先等级6）<br>默认值：无<br>配置原则：无 |
| NGDNSSNAME | DNS服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示DNS服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGDNSS]] · DNS服务器（NGDNSS）

## 使用实例

查询IPTYPE为IPv4，IP地址为192.168.100.101的记录结果： 2、查询所有记录：

```
%%LST NGDNSS: IPTYPE=IPV4, PRI=PRI1;%%
RETCODE = 0  操作成功

结果如下
--------
     IP地址类型  =  IPv4
       IPv4地址  =  192.168.100.101
       IPv6地址  =  ::
DNS服务器优先级  =  服务器优先等级1
  DNS服务器名称  =  dnsserver1
(结果个数 = 1)

---    END

2、
%%LST NGDNSS:;%%
RETCODE = 0  操作成功

结果如下
--------
IP地址类型  IPv4地址         IPv6地址  DNS服务器优先级  DNS服务器名称  

IPv4        192.168.100.101  ::        服务器优先等级1  dnsserver1     
IPv4        192.168.100.102  ::        服务器优先等级3  dnsserver1     
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGDNSS.md`
