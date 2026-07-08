# 查询ISU POD业务CPU过载告警阈值（LST ISUPODCPUTHD）

- [命令功能](#ZH-CN_CONCEPT_0000205083535543__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000205083535543__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000205083535543__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000205083535543__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000205083535543__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000205083535543__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000205083535543)

**适用NF：SGW-U、PGW-U、UPF**

查询ISU POD业务CPU过载告警阈值。

#### [注意事项](#ZH-CN_CONCEPT_0000205083535543)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000205083535543)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000205083535543)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000205083535543)

查询ISU POD业务CPU过载告警阈值：

```
LST ISUPODCPUTHD:;
```

```

RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Alarm Reporting Threshold  =  85
 Alarm Recovery threshold  =  75
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000205083535543)

参见SET ISUPODCPUTHD的参数说明。
