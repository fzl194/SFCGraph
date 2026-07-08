# 查询会话均衡基线能力值（LST SESSLBCAPABILITY）

- [命令功能](#ZH-CN_CONCEPT_0000201227633936__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201227633936__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201227633936__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201227633936__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201227633936__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201227633936__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201227633936)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看已配置所有CPUCAPABILITY实例的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0000201227633936)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201227633936)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201227633936)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201227633936)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0000201227633936)

参见ADD SESSLBCAPABILITY的参数说明。
