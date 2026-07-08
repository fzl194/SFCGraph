# 查询全局话单模板（LST GLBCDRFLDTEMP）

- [命令功能](#ZH-CN_CONCEPT_0209896896__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896896__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896896__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896896__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896896__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896896__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896896)

**适用NF：SGW-C、PGW-C、SMF**

该命令用于查询全局话单模板配置。

#### [注意事项](#ZH-CN_CONCEPT_0209896896)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896896)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896896)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896896)

查询全局话单模板：

```
LST GLBCDRFLDTEMP:;
```

```

RETCODE = 0  操作成功

全局话单字段模板
----------------
  G-CDR话单字段模板名  =  gcdr
PGW-CDR话单字段模板名  =  pgwcdr
SGW-CDR话单字段模板名  =  sgwcdr
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896896)

参见SET GLBCDRFLDTEMP的参数说明。
