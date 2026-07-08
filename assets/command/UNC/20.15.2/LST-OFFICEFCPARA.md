---
id: UNC@20.15.2@MMLCommand@LST OFFICEFCPARA
type: MMLCommand
name: LST OFFICEFCPARA（查询指定NF的流控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OFFICEFCPARA
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF局向流控参数
status: active
---

# LST OFFICEFCPARA（查询指定NF的流控参数）

## 功能

**适用NF：NRF**

该命令用于查询NRF基于局向IP的单进程流控参数配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDRESSTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端NF的客户端IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPTypeV4（IPTypeV4）<br>- IPTypeV6（IPTypeV6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPV4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV4"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。取值范围：1.0.0.0~255.255.255.254。IPv4地址不能为组播地址（224.x.y.z）和环回地址(127.x.y.z)。IPv4地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPV6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPTypeV6"时为条件可选参数。<br>参数含义：该参数用于指定对端NF的客户端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）、组播地址（FF00::/8）和IPv4映射地址（::FFFF:XXXX:XXXX），若为IPv4兼容地址时，需判断是否符合IPv4地址要求。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [指定NF的流控参数（OFFICEFCPARA）](configobject/UNC/20.15.2/OFFICEFCPARA.md)

## 使用实例

查询所有局向流控参数配置，执行如下命令：

```
LST OFFICEFCPARA:;
%%LST OFFICEFCPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
IP类型    IPV4地址  IPV6地址     流控周期(秒)  服务发现请求(个)  检索请求(个)  注册请求(个)  更新请求(个)  心跳请求(个)  订阅请求(个)  

IPTypeV4  10.2.3.4  ::           1             80                65535         1000          110           65535         65535         
IPTypeV6  0.0.0.0   2001:DB8::1  1             120               65535         1000          100           65535         65535         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定NF的流控参数（LST-OFFICEFCPARA）_86184261.md`
