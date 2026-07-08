# 查询在线计费欠费返回码（LST CCLIMITRC）

- [命令功能](#ZH-CN_CONCEPT_0209896951__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896951__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896951__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896951__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896951__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896951__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896951)

**适用NF：PGW-C、SMF**

该命令用于查询在线计费欠费结果码。

#### [注意事项](#ZH-CN_CONCEPT_0209896951)

当前版本不支持此命令。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896951)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896951)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896951)

查询在线计费欠费结果码：

```
LST CCLIMITRC:;
```

```

RETCODE = 0  操作成功。

在线计费欠费返回码
------------------
   MSCC层返回码一  =  4012
   MSCC层返回码二  =  NULL
   MSCC层返回码三  =  NULL
   MSCC层返回码四  =  NULL
   MSCC层返回码五  =  NULL
Command层返回码一  =  4012
Command层返回码二  =  NULL
Command层返回码三  =  NULL
Command层返回码四  =  NULL
Command层返回码五  =  NULL
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896951)

参见SET CCLIMITRC的参数说明。
