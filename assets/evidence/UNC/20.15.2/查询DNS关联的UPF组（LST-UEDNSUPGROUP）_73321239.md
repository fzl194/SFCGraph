# 查询DNS关联的UPF组（LST UEDNSUPGROUP）

- [命令功能](#ZH-CN_MMLREF_0273321239__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0273321239__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0273321239__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0273321239__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0273321239__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0273321239)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询DNS关联的UPF组。

## [注意事项](#ZH-CN_MMLREF_0273321239)

无

#### [操作用户权限](#ZH-CN_MMLREF_0273321239)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0273321239)

无

## [使用实例](#ZH-CN_MMLREF_0273321239)

查询DNS关联的UPF组：

```
LST UEDNSUPGROUP:;
RETCODE = 0  操作成功

结果如下
--------
UPF组名称 

upfgrp1
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0273321239)

| 输出项名称 | 输出项解释 |
| --- | --- |
| UPF组名称 | 该参数用于指定UPF组名称。 |
