---
id: UDG@20.15.2@MMLCommand@LST SESSLBCAPABILITY
type: MMLCommand
name: LST SESSLBCAPABILITY（查询会话均衡基线能力值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SESSLBCAPABILITY
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话均衡基线能力
status: active
---

# LST SESSLBCAPABILITY（查询会话均衡基线能力值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看已配置所有CPUCAPABILITY实例的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SESSLBCAPABILITY]] · 会话均衡基线能力值（SESSLBCAPABILITY）

## 使用实例

显示已配置的CPUCAPABILITY实例信息：

```
LST SESSLBCAPABILITY:;
```

```

RETCODE = 0 操作成功。

Cpu Capability
--------------
Cpu Type  Cpu Generator                              Cpu Frequency  Capability  

aarch64   aarch64                                    2600           900         
x86_64    Intel(R) Xeon(R) CPU E5-2658 v4 @ 2.30GHz  2500           900         
x86_64    Intel(R) Xeon(R) Gold 6138T CPU @ 2.00GHz  2000           930         
x86_64    Intel(R) Xeon(R) Gold 6230N CPU @ 2.30GHz  2300           1000        
x86_64    Intel(R) Xeon(R) Gold 6230R CPU @ 2.10GHz  2100           950         
x86_64    v5                                         25             1000        
(Number of results = 6)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SESSLBCAPABILITY.md`
