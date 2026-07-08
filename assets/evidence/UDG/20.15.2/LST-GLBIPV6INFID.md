# 查询整机IPv6接口ID配置（LST GLBIPV6INFID）

- [命令功能](#ZH-CN_CONCEPT_0271074284__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0271074284__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0271074284__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0271074284__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0271074284__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0271074284__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0271074284)

**适用NF：PGW-U、UPF**

此命令用于整机查询IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能开关配置信息。

#### [注意事项](#ZH-CN_CONCEPT_0271074284)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0271074284)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0271074284)

无。

#### [使用实例](#ZH-CN_CONCEPT_0271074284)

查询IMSI作为用户的IPv6地址interface ID(IPv6地址的后64位)功能配置：

```
LST GLBIPV6INFID:;
```

```

RETCODE = 0 操作成功。

整机IPv6接口ID配置
--------------------
配置IMSI作为IPv6 Interface ID  =  使能
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0271074284)

参见SET GLBIPV6INFID的参数说明。
