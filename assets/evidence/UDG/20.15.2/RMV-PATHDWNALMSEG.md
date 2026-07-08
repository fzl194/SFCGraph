# 删除单条路径断告警抑制参数的分段配置（RMV PATHDWNALMSEG）

- [命令功能](#ZH-CN_CONCEPT_0182837869__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837869__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837869__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837869__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837869__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837869)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定eNodeB/gNodeB地址段内的单条路径断告警抑制的配置。

#### [注意事项](#ZH-CN_CONCEPT_0182837869)

- 该命令执行后立即生效。
- 执行该删除操作，将不会产生指定eNodeB/gNodeB地址段内的单条路径断告警抑制的现象。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837869)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837869)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| V4STARTIP | IPv4类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V4ENDIP | IPv4类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：指定IPv4类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| V6STARTIP | IPv6类型的eNodeB地址段起始地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的起始地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| V6ENDIP | IPv6类型的eNodeB地址段终止地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ENBIPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：指定IPv6类型的eNodeB地址段的终止地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| ENBIPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于设置地址版本类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：表示地址类型为IPv4。<br>- IPV6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837869)

不需要配置单条路径断告警抑制参数的分段配置时,，删除单条路径断指定eNodeB/gNodeB地址段的告警抑制参数配置：

```
RMV PATHDWNALMSEG: ENBIPVERSION=IPV4, V4STARTIP="10.1.1.1", V4ENDIP="10.1.1.1";
```
