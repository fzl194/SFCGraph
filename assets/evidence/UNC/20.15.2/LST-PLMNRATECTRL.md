# 查询Serving PLMN速率控制配置（LST PLMNRATECTRL）

- [命令功能](#ZH-CN_MMLREF_0264343890__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343890__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343890__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343890__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343890__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343890)

**适用NF：SGW-C、PGW-C**

该命令用于Serving PLMN速率控制开关的查询。

## [注意事项](#ZH-CN_MMLREF_0264343890)

无

#### [操作用户权限](#ZH-CN_MMLREF_0264343890)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343890)

无

## [使用实例](#ZH-CN_MMLREF_0264343890)

Serving PLMN速率控制开关查询：

```
%%LST PLMNRATECTRL:;%%
RETCODE = 0  操作成功

结果如下
--------
Serving PLMN速率控制开关  =  不使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0264343890)

| 输出项名称 | 输出项解释 |
| --- | --- |
| Serving PLMN速率控制开关 | 该参数用于控制开启和关闭Serving PLMN速率控制功能。 |
