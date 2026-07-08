---
id: UDG@20.15.2@MMLCommand@LST CPACCESSLIST
type: MMLCommand
name: LST CPACCESSLIST（查询CP白名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CPACCESSLIST
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- CP节点管理
- CP白名单配置
status: active
---

# LST CPACCESSLIST（查询CP白名单）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询符合条件的CP白名单配置。

## 注意事项

- 该命令执行后立即生效。
- 如果没有指定WHITELISTTYPE，则显示所有的CP白名单记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELISTTYPE | 白名单参数类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CP白名单的参数类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- NODEID：白名单参数类型为Node ID。<br>- IP：白名单参数类型为IP地址。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“WHITELISTTYPE”配置为“IP”时为必选参数。<br>参数含义：该参数用例指定IP类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| CPNODEIDTYPE | CP Node ID类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“WHITELISTTYPE”配置为“NODEID”时为必选参数。<br>参数含义：该参数用来指定Node ID类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPv4：表示Node ID类型为IPv4地址。<br>- IPv6：表示Node ID类型为IPv6地址。<br>- FQDN：表示Node ID类型为FQDN。<br>默认值：无<br>配置原则：无 |
| CPIPV4 | CP IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定要进行白名单控制的CP的IPv4地址段的地址，该配置需要和网络规划保持一致。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPIPV6 | CP IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定要进行白名单控制的CP的IPv6地址段的地址，该配置需要和网络规划一致。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPIPV4MASK | CP IPv4掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数指定白名单控制的CP的IPv4地址段的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |
| CPIPV6MASK | CP IPv6掩码长度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用来指定白名单控制的CP的IPv6地址段的掩码长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV4 | CP Node ID中的IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于指定允许建立偶联的CP的Node ID中的IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDIPV6 | CP Node ID中的IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。<br>参数含义：该参数用户设定允许建立偶联的CP的Node ID中的IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| CPNODEIDFQDN | CP Node ID的FQDN | 可选必选说明：条件必选参数<br>前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。<br>参数含义：该参数用户设定允许建立偶联的CP的Node ID中的FQDN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CP白名单（CPACCESSLIST）](configobject/UDG/20.15.2/CPACCESSLIST.md)

## 使用实例

显示CP白名单列表：

```
LST CPACCESSLIST:;
```

```

RETCODE = 0 操作成功.

结果如下
-----------
         CP IPv4地址 = 10.36.0.2
     CP IPv4掩码长度 = 27
         CP IPv6地址 = ::
     CP IPv6掩码长度 = 0
CP Node ID的IPv4地址 = 0.0.0.0
CP Node ID的IPv6地址 = ::
    CP Node ID的FQDN = 0x0
          配置域名称 = NULL
 (结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP白名单（LST-CPACCESSLIST）_86530487.md`
