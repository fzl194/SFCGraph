# 查询EpRpDyn对象的IP配置结果（LST EPRPDYNIP）

- [命令功能](#ZH-CN_CONCEPT_0182837839__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837839__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837839__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837839__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837839__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837839__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837839)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询EpRpDyn对象的本端IP地址和对端IP地址段。

#### [注意事项](#ZH-CN_CONCEPT_0182837839)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837839)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837839)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPDYNNAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格以及特殊字符：“_”、“#”、“$”等。<br>默认值：无<br>配置原则：无 |
| IPVERSION | IP地址版本类型 | 可选必选说明：可选参数<br>参数含义：该参数用来指定IP地址版本类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| LSIPV4DIRECTION | IP方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用来指定IP方向。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_IP：本端IP地址。<br>- FAR_IP：对端IP地址段。<br>默认值：无<br>配置原则：无 |
| LSIPV6DIRECTION | IP方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用来指定IP方向。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- LOCAL_IP：本端IP地址。<br>- FAR_IP：对端IP地址段。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837839)

查询EPRPDYN对象pgw1的所有本端IP地址和对端IP地址段：

```
LST EPRPDYNIP: EPRPDYNNAME="pgw1";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
IP地址版本类型    IPv4地址           IPv4掩码长度    IPv4方向     IPv6地址       IPv6掩码长度    IPv6方向
IPV4              192.168.12.11      32              LOCAL IP     ::              0               LOCAL IP        
IPV4              10.1.1.4           24              FAR IP       ::              0               FAR IP        
(结果个数 = 2)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837839)

参见ADD EPRPDYNIP的参数说明。
