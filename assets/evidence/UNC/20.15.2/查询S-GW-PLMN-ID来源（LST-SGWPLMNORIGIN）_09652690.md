# 查询S-GW PLMN ID来源（LST SGWPLMNORIGIN）

- [命令功能](#ZH-CN_MMLREF_0209652690__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652690__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652690__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652690__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209652690__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209652690)

**适用NF：PGW-C、SGW-C**

该命令用于查询SGW-C和PGW-C合一形态时SGW-C PLMN的获取方式。

## [注意事项](#ZH-CN_MMLREF_0209652690)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209652690)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652690)

无

## [使用实例](#ZH-CN_MMLREF_0209652690)

查询S-GW和P-GW合一形态时S-GW PLMN的获取方式：

```
%%LST SGWPLMNORIGIN:;%%
RETCODE = 0  操作成功

结果如下
--------
S-GW PLMN ID来源  =  P-GW PLMN
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209652690)

| 输出项名称 | 输出项解释 |
| --- | --- |
| S-GW PLMN ID来源 | 用于控制SGW-C和PGW-C合一形态时SGW-C PLMN ID的获取方式。 |
