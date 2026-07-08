# 显示SMSF系统内处于UDM Bypass状态的用户数（DSP SMSFUDMBYPASSNUM）

- [命令功能](#ZH-CN_MMLREF_0000001404735165__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001404735165__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001404735165__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001404735165__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001404735165__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001404735165)

**适用NF：SMSF**

该命令用于显示SMSF系统内处于UDM Bypass状态的用户数。

## [注意事项](#ZH-CN_MMLREF_0000001404735165)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001404735165)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001404735165)

无

## [使用实例](#ZH-CN_MMLREF_0000001404735165)

当运营商希望查询SMSF系统内处于UDM Bypass状态的用户数，执行如下命令：

```
DSP SMSFUDMBYPASSNUM:;
```

## [输出结果说明](#ZH-CN_MMLREF_0000001404735165)

| 输出项名称 | 输出项解释 |
| --- | --- |
| SMSF UDM Bypass用户数 | 该参数用于表示SMSF系统特定POD内处于UDM Bypass状态的用户数。 |
| PODID | 该参数用于表示SMSF系统内处于UDM Bypass状态的用户数所在的POD的标识。 |
