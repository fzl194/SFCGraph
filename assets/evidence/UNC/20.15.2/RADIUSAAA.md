# 查询RADIUS AAA测量对象（LST RADIUSAAA）

- [命令功能](#ZH-CN_CONCEPT_0209896767__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896767__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896767__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896767__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896767__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896767__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896767)

**适用NF：PGW-C、SMF**

此命令用于查询RADIUS AAA测量对象。

#### [注意事项](#ZH-CN_CONCEPT_0209896767)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896767)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896767)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896767)

查询RADIUS AAA测量对象：

```
LST RADIUSAAA:;
```

```

RETCODE = 0  操作成功。

RADIUS Server IP地址
--------------------
IP地址  =  192.168.1.12
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896767)

| 输出项名称 | 输出项解释 |
| --- | --- |
| IP地址 | 用于存放RADIUS AAA IP地址。 |
