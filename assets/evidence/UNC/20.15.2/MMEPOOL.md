# 查询MME POOL（LST MMEPOOL）

- [命令功能](#ZH-CN_MMLREF_0231453516__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0231453516__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0231453516__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0231453516__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0231453516__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0231453516)

**适用NF：SGW-C、PGW-C**

该命令用于查询MME POOL。

## [注意事项](#ZH-CN_MMLREF_0231453516)

无

#### [操作用户权限](#ZH-CN_MMLREF_0231453516)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0231453516)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEPOOLNAME | MME POOL名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0231453516)

假设用户需要查询所有的MME POOL：

```
%%LST MMEPOOL:;%%
RETCODE = 0  操作成功

结果如下
--------
       MME POOL名称  =  mmepool1
       SGW POOL名称  =  NULL
指定备份MME功能开关  =  不使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0231453516)

| 输出项名称 | 输出项解释 |
| --- | --- |
| MME POOL名称 | 该参数用于指定MME POOL名。 |
| SGW POOL名称 | 该参数用于指定与该MME POOL绑定的SGW POOL名。 |
| 指定备份MME功能开关 | 配置是否开启指定备份MME的功能。 |
