# 查询UE Ping逻辑接口开关（LST UEPINGINF）

- [命令功能](#ZH-CN_CONCEPT_0279568176__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0279568176__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0279568176__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0279568176__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0279568176__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0279568176__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0279568176)

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询UE ping逻辑口的开关状态。

#### [注意事项](#ZH-CN_CONCEPT_0279568176)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0279568176)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0279568176)

无。

#### [使用实例](#ZH-CN_CONCEPT_0279568176)

查询UE ping逻辑口的开关状态：

```
LST UEPINGINF:;
```

```

RETCODE = 0  操作成功。

UE Ping逻辑接口开关
-------------------
Ping开关  =  使能
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0279568176)

参见SET UEPINGINF的参数说明。
