# 查询MPLS LSP统计信息（DSP MPLSLSPSTC）

- [命令功能](#ZH-CN_CONCEPT_0000001550121070__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121070__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121070__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121070__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121070__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550121070__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121070)

该命令用于查询MPLS LSP统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121070)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121070)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121070)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSPTYPE | MPLS LSP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MPLS LSP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LDP_LSP：LDP LSP。<br>- BGP_LSP：BGP LSP。<br>- BGP_IPV6_LSP：BGP IPv6 LSP。<br>- L3VPN_IPV6_LSP：L3VPN IPv6 LSP。<br>- LSP：所有的LSP。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121070)

查询MPLS LSP统计信息：

```
DSP MPLSLSPSTC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
MPLS LSP类型      LSP总计数量        入节点数量     中间节点数量    出节点数量

LDP LSP           13                 5              5               3
BGP LSP           0                  0              0               0
BGP IPv6 LSP      0                  0              0               0
L3VPN IPv6 LSP    0                  0              0               0
所有的LSP         13                 5              5               3
(结果个数 = 5)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550121070)

| 输出项名称 | 输出项解释 |
| --- | --- |
| MPLS LSP类型 | 用于表示MPLS LSP类型。 |
| LSP总计数量 | 用于表示LSP总计数量。 |
| 入节点数量 | 用于表示入节点数量。 |
| 中间节点数量 | 用于表示中间节点数量。 |
| 出节点数量 | 用于表示出节点数量。 |
