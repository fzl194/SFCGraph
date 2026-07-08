---
id: UDG@20.15.2@MMLCommand@DSP PATHSTSTRESULT
type: MMLCommand
name: DSP PATHSTSTRESULT（查询批量路径探测结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PATHSTSTRESULT
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
- GTP路径管理
- GTP路径测试
- 批量路径探测结果
status: active
---

# DSP PATHSTSTRESULT（查询批量路径探测结果）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询路径批量探测命令的结果。此命令仅显示异常路径的结果，最多显示100条异常路径记录。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNNAME | vpn名字 | 可选必选说明：可选参数<br>参数含义：指定本端IP地址对应逻辑接口绑定的VPN，即对端网元所在的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |
| SRCIPV4ADDR | 源IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：探测源IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制形式。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：必选参数<br>参数含义：IP地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| SRCIPV6ADDR | 源IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定源IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。点分十进制形式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATHSTSTRESULT]] · 批量路径探测结果（PATHSTSTRESULT）

## 使用实例

查询源IP是192.168.21.4的路径批量探测结果：

```
DSP PATHSTSTRESULT: IPVERSION=IPV4, SRCIPV4ADDR="192.168.21.4";
```

```

RETCODE = 0  Operation Success.

Paths Test Result Info
----------------------
Result  =  
Source IP: 192.168.21.4                            VPN-instance: NULL
Total Paths Number: 3   Detected Paths Number: 3   Abnormal Paths Number: 3
Start Time: 15:51:25  End Time: 15:52:02 
Abnormal Paths Information: 
---------------------------------------
Source IP                               Destination IP
192.168.21.4                            192.168.1.1
192.168.21.4                            192.168.1.2
192.168.21.4                            192.168.1.3
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询批量路径探测结果（DSP-PATHSTSTRESULT）_82837236.md`
