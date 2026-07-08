# 查询Diameter参数（LST DIAMETERPARA）

- [命令功能](#ZH-CN_CONCEPT_0209897316__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897316__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897316__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897316__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897316__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897316__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897316)

**适用NF：PGW-C、SMF**

该命令用于查询是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送的配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0209897316)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897316)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897316)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897316)

查询当前是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送功能的配置信息：

```
LST DIAMETERPARA:;
```

```

RETCODE = 0  操作成功。

Diameter参数信息
----------------
基于域名的路由功能开关  =  允许
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897316)

参见SET DIAMETERPARA的参数说明。
