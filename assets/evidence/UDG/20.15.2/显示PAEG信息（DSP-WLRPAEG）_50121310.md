# 显示PAEG信息（DSP WLRPAEG）

- [命令功能](#ZH-CN_CONCEPT_0000001550121310__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121310__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121310__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121310__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121310__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550121310__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121310)

该命令用于显示PAEG信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121310)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121310)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121310)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121310)

显示PAEG信息：

```
DSP WLRPAEG:ADDRESSFAMILY=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
用户ID     Peer地址        地址族            PAEG IID    PAE GROUPID    TB high    TB low    TP    版本号
1000       10.1.1.100       IPv4单播          1           2              0          64        0     1
1000       10.1.1.100       IPv4单播          1           2              0          65        0     1
1000       10.1.1.100       IPv4单播          1           2              0          66        0     1
(结果个数 = 3)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550121310)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户ID | 用来表示用户ID。 |
| Peer地址 | 用于表示PEER地址。 |
| 地址族 | 用于表示地址族。 |
| PAEG IID | 用于表示PAEG IID。 |
| PAE GROUPID | 用于表示PAE GROUPID。 |
| TB high | 用于表示TB high。 |
| TB low | 用于表示TB low。 |
| TP | 用于表示TP。 |
| 版本号 | 用于表示版本号。 |
