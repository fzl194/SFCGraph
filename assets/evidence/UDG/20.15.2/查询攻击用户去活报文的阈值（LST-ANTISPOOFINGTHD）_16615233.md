# 查询攻击用户去活报文的阈值（LST ANTISPOOFINGTHD）

- [命令功能](#ZH-CN_CONCEPT_0216615233__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0216615233__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0216615233__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0216615233__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0216615233__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0216615233__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0216615233)

**适用NF：UPF**

该参数用于查询攻击用户去活报文的阈值。

#### [注意事项](#ZH-CN_CONCEPT_0216615233)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0216615233)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0216615233)

无。

#### [使用实例](#ZH-CN_CONCEPT_0216615233)

使用LST ANTISPOOFINGTHD命令查询当前配置的ANTISPOOFING对攻击用户使用的阈值：

```
LST ANTISPOOFINGTHD:;
```

```

RETCODE = 0  Operation succeeded

AntiSpoofingThd Value
---------------------
Anti-spoofing Threshold for Subscriber Deactivation  =  100
(Number of results = 1)
```

#### [输出结果说明](#ZH-CN_CONCEPT_0216615233)

参见SET ANTISPOOFINGTHD的参数说明。
