# 查询UPF系统开工流程消息的参数（LST UPFSTARTPARA）

- [命令功能](#ZH-CN_CONCEPT_0186526951__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0186526951__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0186526951__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0186526951__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0186526951__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0186526951__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0186526951)

**适用NF：UPF**

该命令用来查看系统开工流程消息的相关属性。

#### [注意事项](#ZH-CN_CONCEPT_0186526951)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0186526951)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0186526951)

无。

#### [使用实例](#ZH-CN_CONCEPT_0186526951)

查询系统开工流程消息的相关属性：

```
LST UPFSTARTPARA:;
```

```

RETCODE = 0  Operation Success.

UPF start procedure message configuration is
--------------------------------------------
Start Procedure Interval  =  80
(Number of results = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0186526951)

参见SET UPFSTARTPARA的参数说明。
