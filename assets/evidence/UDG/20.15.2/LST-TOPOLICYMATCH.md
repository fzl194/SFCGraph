# 查询TCP优化策略匹配规则（LST TOPOLICYMATCH）

- [命令功能](#ZH-CN_CONCEPT_0000204493415787__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000204493415787__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000204493415787__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000204493415787__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000204493415787__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000204493415787__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000204493415787)

**适用NF：PGW-U、UPF**

该命令用于查询TCP优化策略匹配规则。

#### [注意事项](#ZH-CN_CONCEPT_0000204493415787)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000204493415787)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000204493415787)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000204493415787)

运营商需要查询所有的TCP优化策略匹配规则：

```
LST TOPOLICYMATCH:;
```

```

RETCODE = 0  操作成功

TCP优化策略匹配规则
----------------
小区组名称          IMSI组名称        RAT类型    策略ID
TestCellGroupName   TestIMSIGroupName  NR         1
TestCellGroupName   TestIMSIGroupName  EUTRAN     2
(结果个数 = 2)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000204493415787)

参见ADD TOPOLICYMATCH的参数说明。
