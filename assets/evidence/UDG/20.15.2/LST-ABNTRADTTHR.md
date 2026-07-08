# 查询异常流量检测报文阈值（LST ABNTRADTTHR）

- [命令功能](#ZH-CN_CONCEPT_0182837031__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837031__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837031__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837031__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837031__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837031__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837031)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询异常流量检测报文阈值。

#### [注意事项](#ZH-CN_CONCEPT_0182837031)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837031)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837031)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837031)

查询异常下行异常流量检测报文阈值个数：

```
LST ABNTRADTTHR:;
```

```

RETCODE = 0  Operation Success.

Abnormal Traffic detect threshold
---------------------------------
Abnormal Traffic detect threshold of packet  =  20
(Number of results = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837031)

参见SET ABNTRADTTHR的参数说明。
