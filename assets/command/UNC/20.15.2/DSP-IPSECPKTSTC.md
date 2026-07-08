---
id: UNC@20.15.2@MMLCommand@DSP IPSECPKTSTC
type: MMLCommand
name: DSP IPSECPKTSTC（查询IPsec报文统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPSECPKTSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPsec调测
- IPsec诊断信息
- IPsec报文统计
status: active
---

# DSP IPSECPKTSTC（查询IPsec报文统计信息）

## 功能

该命令用于查询IPsec报文统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECPKTSTC]] · IPsec报文统计信息（IPSECPKTSTC）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-IPSECPKTSTC.md`
