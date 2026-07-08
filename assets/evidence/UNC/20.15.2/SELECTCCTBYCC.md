# 查询基于CC配置融合计费模板处理（LST SELECTCCTBYCC）

- [命令功能](#ZH-CN_MMLREF_0209653712__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653712__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653712__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653712__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653712__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653712)

**适用NF：PGW-C、SMF、SGW-C**

该命令用于查询基于CC配置融合计费模板处理。

## [注意事项](#ZH-CN_MMLREF_0209653712)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653712)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653712)

无

## [使用实例](#ZH-CN_MMLREF_0209653712)

查询基于CC配置的融合计费模板：

```
%%LST SELECTCCTBYCC:;%%
RETCODE = 0  操作成功

结果如下
--------
                         CC类型  =  未指定Charge Characteristic的值
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0xFFFF
    Charge Characteristic优先级  =  0
               融合计费模板名称  =  global
I-SMF/SGW使用的融合计费模板名称  =  servingcct
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653712)

| 输出项名称 | 输出项解释 |
| --- | --- |
| CC类型 | 该参数用于指定计费属性。 |
| Charge Characteristic值 | 该参数用于指定特殊的CC值。 |
| Charge Characteristic特定值掩码 | 该参数用于指定CC的掩码，通过配置掩码可以实现全匹配CC值，还是只匹配部分bit位。 |
| Charge Characteristic优先级 | 该参数用于设置优先级，配置mask时必须指定优先级，不允许指定相同的优先级。 |
| 融合计费模板名称 | 该命令用于指定融合计费模板（Converged Charging Template）名称。 |
| I-SMF/SGW使用的融合计费模板名称 | 该命令用于指定I-SMF/SGW使用的融合计费模板（Converged Charging Template）名称。 |
