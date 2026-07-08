# 查询GTPP本端信息（LST GTPPLOCINFO）

- [命令功能](#ZH-CN_CONCEPT_0209896858__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896858__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896858__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896858__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896858__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896858__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896858)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询GTPP本端信息。

#### [注意事项](#ZH-CN_CONCEPT_0209896858)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896858)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896858)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896858)

查询GTPP本端信息：

```
LST GTPPLOCINFO:;
```

```

RETCODE = 0  操作成功

GTPP本端主机信息
----------------
    本端主机名  =  test
      本端域名  =  test
业务上下文标识  =  abc
    本端接口名  =  gaif1/0/1
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896858)

参见ADD GTPPLOCINFO的参数说明。
