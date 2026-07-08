# 查询整机IPv6接口ID配置（LST GLBIPV6INFID）

- [命令功能](#ZH-CN_MMLREF_0296242150__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0296242150__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0296242150__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0296242150__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0296242150__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0296242150)

**适用NF：PGW-C、GGSN、SMF**

此命令用于查询IMSI作为用户的IPv6地址Interface ID功能开关配置信息。

## [注意事项](#ZH-CN_MMLREF_0296242150)

无

#### [操作用户权限](#ZH-CN_MMLREF_0296242150)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0296242150)

无

## [使用实例](#ZH-CN_MMLREF_0296242150)

查询IMSI作为用户的IPv6地址Interface ID功能配置：

```
%%LST GLBIPV6INFID:;%%
RETCODE = 0  操作成功

结果如下
--------
配置IMSI作为IPv6 Interface ID  =  不使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0296242150)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 配置IMSI作为IPv6 Interface ID | 该参数用于控制开启和关闭IMSI作为用户的IPv6地址Interface ID功能。 |
