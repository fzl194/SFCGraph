# 查询SSU容器业务相关老化功能配置（LST SSUAGINGCFG）

- [命令功能](#ZH-CN_CONCEPT_0000203928486287__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000203928486287__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000203928486287__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000203928486287__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000203928486287__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000203928486287__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000203928486287)

**适用NF：PGW-U、UPF**

该命令用于查询SSU容器业务相关老化功能配置。

#### [注意事项](#ZH-CN_CONCEPT_0000203928486287)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000203928486287)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000203928486287)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000203928486287)

查询SSU容器业务相关老化功能配置：

```
%%LST SSUAGINGCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Configuring the Aging Function for SSU Container Services
---------------------------------------------------------
Service flow aging time (s)  =  36
   Session Aging Time (min)  =  1440
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000203928486287)

参见SET SSUAGINGCFG的参数说明。
