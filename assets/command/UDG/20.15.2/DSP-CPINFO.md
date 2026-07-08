---
id: UDG@20.15.2@MMLCommand@DSP CPINFO
type: MMLCommand
name: DSP CPINFO（显示CP信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: CPINFO
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- CP节点管理
- CP节点信息
status: active
---

# DSP CPINFO（显示CP信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于动态查询CP的信息。查询结果包括CP Node ID，CP IP地址，系统与CP之间的路径状态。

## 注意事项

- 如果NodeIDType为FQDN类型时，NodeID中包含的不可见字符将替换为星号（*）。
- 热备场景，备网元不会探测路径状态，也不会同步主网元的路径状态，当主网元的路径状态由UP变成DOWN时，备网元的路径状态依旧保持UP，备网元升主后会重新探测。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPIPV4 | CP IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定要查询的CP的IPv4地址，该配置需要和网络规划保持一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPIPV6 | CP IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定要进行查询的CP的IPv6地址，该配置需要和网络规划保持一致。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动态查询CP的信息时输入的查询类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NODEID：查询类型为根据Node ID查询。<br>- IP：查询类型为根据消息源IP地址查询。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“IP”时为必选参数。<br>参数含义：该参数用来指定IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | Node ID类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“QUERYTYPE”配置为“NODEID”时为必选参数。<br>参数含义：该参数用来指定Node ID 类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示Node ID类型为IPv4地址。<br>- IPv6：表示Node ID类型为IPv6地址。<br>- FQDN：表示Node ID类型为FQDN。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV4 | Node ID中的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时， Node ID 的中的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV6 | Node ID中的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于指定，在根据Node ID查询CP信息时， Node ID 中的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEFQDN | Node ID中的FQDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID 中的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CPINFO]] · CP信息（CPINFO）

## 使用实例

显示当前CP信息：

```
DSP CPINFO:;
```

```

RETCODE = 0  操作成功

CP 信息:
---------------
Result  =  
CP IP Address                             CP State       CP Node ID                                                                                                                                                                                                                                                     
192.168.0.10                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.11                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.12                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.13                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.14                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.15                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.16                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.17                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.18                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.19                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.20                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.21                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.22                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.23                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.24                               UP             SMF1                                                                                                                                                                                                                                                           
192.168.0.25                               UP             SMF1                                                                                                                                                                                                                                                           
ALL CPInfo Number = 16
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示CP信息（DSP-CPINFO）_82837261.md`
