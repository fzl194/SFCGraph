# 查询是否检查Serving Node携带的CC（LST CHARGECHARCHK）

- [命令功能](#ZH-CN_CONCEPT_0209896803__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896803__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896803__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896803__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896803__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896803__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896803)

**适用NF：PGW-C、SMF**

该命令用来查询是否检查Serving Node携带的charge-characteristic。

#### [注意事项](#ZH-CN_CONCEPT_0209896803)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896803)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896803)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896803)

查询是否检查Serving Node携带的charge-characteristic：

```
LST CHARGECHARCHK:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
检查Serving Node携带的charge-characteristic  =  允许
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896803)

参见SET CHARGECHARCHK的参数说明。
