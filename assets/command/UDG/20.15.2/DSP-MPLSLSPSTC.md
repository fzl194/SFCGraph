---
id: UDG@20.15.2@MMLCommand@DSP MPLSLSPSTC
type: MMLCommand
name: DSP MPLSLSPSTC（查询MPLS LSP统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MPLSLSPSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS LSP统计
status: active
---

# DSP MPLSLSPSTC（查询MPLS LSP统计信息）

## 功能

该命令用于查询MPLS LSP统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSPTYPE | MPLS LSP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示MPLS LSP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LDP_LSP：LDP LSP。<br>- BGP_LSP：BGP LSP。<br>- BGP_IPV6_LSP：BGP IPv6 LSP。<br>- L3VPN_IPV6_LSP：L3VPN IPv6 LSP。<br>- LSP：所有的LSP。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MPLSLSPSTC]] · MPLS LSP统计信息（MPLSLSPSTC）

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MPLSLSPSTC.md`
