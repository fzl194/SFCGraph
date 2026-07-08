# 查询全局CG组（LST GLBCGGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209896862__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896862__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896862__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896862__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896862__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896862__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896862)

**适用NF：SGW-C、PGW-C、SMF**

本条命令用于查询全局CG组。

#### [注意事项](#ZH-CN_CONCEPT_0209896862)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896862)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896862)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896862)

查询全局CG组：

```
LST GLBCGGROUP:;
```

```

RETCODE = 0  操作成功

全局CG组
--------
CG组ID  =  1
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896862)

参见SET GLBCGGROUP的参数说明。
