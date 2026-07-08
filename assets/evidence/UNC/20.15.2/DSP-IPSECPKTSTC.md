# 查询IPsec报文统计信息（DSP IPSECPKTSTC）

- [命令功能](#ZH-CN_CONCEPT_0000001600600661__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600600661__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600600661__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600600661__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600600661__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600600661__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600600661)

该命令用于查询IPsec报文统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600600661)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600600661)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600600661)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000001600600661)

查询IPsec报文统计信息：

```
DSP IPSECPKTSTC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
组件ID        IPv6 ESP socket入向总报文数    IPv6 ESP socket入向处理成功报文数    IPv6 ESP socket入向丢弃报文数    IPv6 ESP socket出向总报文数    IPv6 ESP socket出向处理成功报文数    IPv6 ESP socket出向丢弃报文数    IPv6 AH socket入向总报文数    IPv6 AH socket入向处理成功报文数    IPv6 AH socket入向丢弃报文数    IPv6 AH socket出向总报文数    IPv6 AH socket出向处理成功报文数    IPv6 AH socket出向丢弃报文数    IPv4 ESP socket入向总报文数    IPv4 ESP socket入向处理成功报文数    IPv4 ESP socket入向丢弃报文数    IPv4 ESP socket出向总报文数    IPv4 ESP socket出向处理成功报文数    IPv4 ESP socket出向丢弃报文数    IPv4 AH socket入向总报文数    IPv4 AH socket入向处理成功报文数    IPv4 AH socket入向丢弃报文数    IPv4 AH socket出向总报文数    IPv4 AH socket出向处理成功报文数    IPv4 AH socket出向丢弃报文数

0x803f0098    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
0x803f0022    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
0x803f0021    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
(结果个数 = 3)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600600661)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 组件ID | 组件ID。 |
| IPv6 ESP socket入向总报文数 | IPv6 ESP socket入向总报文数。 |
| IPv6 ESP socket入向处理成功报文数 | IPv6 ESP socket入向处理成功报文数。 |
| IPv6 ESP socket入向丢弃报文数 | IPv6 ESP socket入向丢弃报文数。 |
| IPv6 ESP socket出向总报文数 | IPv6 ESP socket出向总报文数。 |
| IPv6 ESP socket出向处理成功报文数 | IPv6 ESP socket出向处理成功报文数。 |
| IPv6 ESP socket出向丢弃报文数 | IPv6 ESP socket出向丢弃报文数。 |
| IPv6 AH socket入向总报文数 | IPv6 AH socket入向总报文数。 |
| IPv6 AH socket入向处理成功报文数 | IPv6 AH socket入向处理成功报文数。 |
| IPv6 AH socket入向丢弃报文数 | IPv6 AH socket入向丢弃报文数。 |
| IPv6 AH socket出向总报文数 | IPv6 AH socket出向总报文数。 |
| IPv6 AH socket出向处理成功报文数 | IPv6 AH socket出向处理成功报文数。 |
| IPv6 AH socket出向丢弃报文数 | IPv6 AH socket出向丢弃报文数。 |
| IPv4 ESP socket入向总报文数 | IPv4 ESP socket入向总报文数。 |
| IPv4 ESP socket入向处理成功报文数 | IPv4 ESP socket入向处理成功报文数。 |
| IPv4 ESP socket入向丢弃报文数 | IPv4 ESP socket入向丢弃报文数。 |
| IPv4 ESP socket出向总报文数 | IPv4 ESP socket出向总报文数。 |
| IPv4 ESP socket出向处理成功报文数 | IPv4 ESP socket出向处理成功报文数。 |
| IPv4 ESP socket出向丢弃报文数 | IPv4 ESP socket出向丢弃报文数。 |
| IPv4 AH socket入向总报文数 | IPv4 AH socket入向总报文数。 |
| IPv4 AH socket入向处理成功报文数 | IPv4 AH socket入向处理成功报文数。 |
| IPv4 AH socket入向丢弃报文数 | IPv4 AH socket入向丢弃报文数。 |
| IPv4 AH socket出向总报文数 | IPv4 AH socket出向总报文数。 |
| IPv4 AH socket出向处理成功报文数 | IPv4 AH socket出向处理成功报文数。 |
| IPv4 AH socket出向丢弃报文数 | IPv4 AH socket出向丢弃报文数。 |
