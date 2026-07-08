# 查询整机操作系统级带宽管理开关（LST GLBOSLELBWMSW）

- [命令功能](#ZH-CN_CONCEPT_0182837502__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837502__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837502__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837502__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837502__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837502__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837502)

**适用NF：PGW-U、UPF**

该命令用来查询整机操作系统级带宽管理开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837502)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837502)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837502)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837502)

查询整机操作系统级带宽管理开关信息：

```
LST GLBOSLELBWMSW:;
```

```

RETCODE = 0 Operation Success.

Global OS Level Bandwidth Managament Switch Information
--------------------------------------------------------------------------------
 Global OS Level Bandwidth Managament Switch = ENABLE
(Number of results = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837502)

参见SET GLBOSLELBWMSW的参数说明。
