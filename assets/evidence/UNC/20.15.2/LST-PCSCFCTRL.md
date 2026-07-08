# 查询P-CSCF控制配置（LST PCSCFCTRL）

- [命令功能](#ZH-CN_MMLREF_0209653780__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653780__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653780__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653780__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653780__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653780)

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询P-CSCF控制属性配置信息。

## [注意事项](#ZH-CN_MMLREF_0209653780)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653780)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653780)

无

## [使用实例](#ZH-CN_MMLREF_0209653780)

显示P-CSCF故障后是否主动向用户侧发送UpdateBearerRequest消息配置信息：

```
%%LST PCSCFCTRL:;%%
RETCODE = 0 操作成功

结果如下
------------
故障恢复 = 使能
(结果个数 = 1)

--- END
```

## [输出结果说明](#ZH-CN_MMLREF_0209653780)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 故障恢复 | 该参数用于设置检测到P-CSCF故障时，是否主动向用户侧发起UpdateBearerRequest消息更新P-CSCF地址。 |
