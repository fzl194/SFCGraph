# 按照IP地址分配方式查看当前在线会话数（DSP APNSESSIONSTATS）

- [命令功能](#ZH-CN_CONCEPT_0206054802__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0206054802__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0206054802__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0206054802__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0206054802__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0206054802__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0206054802)

**适用NF：PGW-U、UPF**

该命令用来按照IP地址分配方式查询当前在线会话数。

#### [注意事项](#ZH-CN_CONCEPT_0206054802)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_CONCEPT_0206054802)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0206054802)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CATEGORYTYPE | 种类 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IP_ALLOCATION：按照IP地址分配方式查看当前在线会话数。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0206054802)

按照IP地址分配方式查询当前在线会话数：

```
DSP APNSESSIONSTATS: CATEGORYTYPE=IP_ALLOCATION;
```

```

RETCODE = 0  Operation Success.

Ip Address Allocation Method
-------------------------
                                 Name of a Configured APN  =  a
     APN-specific Sessions Using Local Alloc IP Addresses  =  0
   APN-specific Sessions Using External Alloc IP Addresses =  0
    APN-specific Contexts Using LNS-assigned IP Addresses  =  0
(Number of results = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0206054802)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 已配置的apn名 | 已配置的apn名。 |
| 指定apn当前在线的本地地址分配方式会话数 | 指定apn当前在线的本地地址分配方式上下文数。 |
| 指定apn当前在线的外部地址分配方式会话数 | 指定apn当前在线的静态地址分配方式上下文数。 |
| 指定apn当前在线的LNS地址分配方式上下文数 | 指定apn当前在线的LNS地址分配方式上下文数。 |
