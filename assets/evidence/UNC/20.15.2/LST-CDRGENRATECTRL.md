# 查询话单产生速率（LST CDRGENRATECTRL）

- [命令功能](#ZH-CN_CONCEPT_0209896709__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209896709__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209896709__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209896709__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209896709__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209896709__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209896709)

**适用NF：SGW-C、PGW-C、SMF**

LST CDRGENRATECTRL命令用来查询计费数据产生速率控制信息。

#### [注意事项](#ZH-CN_CONCEPT_0209896709)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209896709)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209896709)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209896709)

查询系统计费数据产生速率控制信息：

```
LST CDRGENRATECTRL:;
```

```

RETCODE = 0  操作成功。

话单产生速率控制
----------------
CDR产生速率（%）  =  50
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209896709)

参见SET CDRGENRATECTRL的参数说明。
