# 查询CP白名单开关（LST CPACCESSLISTFUNC）

- [命令功能](#ZH-CN_CONCEPT_0186530397__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186530397__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186530397__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186530397__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186530397__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186530397__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186530397)

**适用NF：SGW-U、PGW-U、UPF**

此命令用于查询CP白名单功能的开关。

#### [注意事项](#ZH-CN_CONCEPT_0186530397)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186530397)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186530397)

无。

#### [使用实例](#ZH-CN_CONCEPT_0186530397)

查询系统是否支持CP白名单功能：

```
LST CPACCESSLISTFUNC:;
```

```

RETCODE = 0 操作成功.

CP白名单开关配置
-----------
开关标识 = 不使能
(结果个数 = 1)
--- END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0186530397)

参见SET CPACCESSLISTFUNC的参数说明。
