# 查询全局Gi重定向信息（LST GIREDIRECTFUNC）

- [命令功能](#ZH-CN_CONCEPT_0182837765__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837765__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837765__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837765__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837765__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837765__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837765)

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询全局IPv4和IPv6 Gi重定向开关。

#### [注意事项](#ZH-CN_CONCEPT_0182837765)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837765)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837765)

无。

#### [使用实例](#ZH-CN_CONCEPT_0182837765)

查询IPv4和IPv6 Gi重定向全局开关：

```
LST GIREDIRECTFUNC:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
IPV4全局Gi重定向开关  =  使能
IPV6全局Gi重定向开关  =  使能
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837765)

参见SET GIREDIRECTFUNC的参数说明。
