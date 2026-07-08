# 查询对Gy接口的cea消息中的Origin-Host检查开关（LST CEAORIGHOSTCHK）

- [命令功能](#ZH-CN_CONCEPT_0209897241__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897241__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897241__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897241__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897241__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897241__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897241)

**适用NF：PGW-C、SMF**

该命令用于查询Diameter对Gy接口的cea消息中的Origin-Host检查开关。

#### [注意事项](#ZH-CN_CONCEPT_0209897241)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897241)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897241)

无。

#### [使用实例](#ZH-CN_CONCEPT_0209897241)

查询Diameter对Gy接口的cea消息中的Origin-Host检查开关，则可按如下配置：

```
LST CEAORIGHOSTCHK:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
检查Gy的CEA消息中的Origin-Host  =  禁止
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897241)

参见SET CEAORIGHOSTCHK的参数说明。
