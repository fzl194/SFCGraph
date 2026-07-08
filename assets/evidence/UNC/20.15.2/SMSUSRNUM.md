# 显示SMSF中注册的用户数（DSP SMSUSRNUM）

- [命令功能](#ZH-CN_MMLREF_0225120882__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0225120882__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0225120882__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0225120882__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0225120882__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0225120882)

**适用NF：SMSF**

该命令用于查询当前在SMSF系统中注册的用户数。

## [注意事项](#ZH-CN_MMLREF_0225120882)

无

#### [操作用户权限](#ZH-CN_MMLREF_0225120882)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0225120882)

无

## [使用实例](#ZH-CN_MMLREF_0225120882)

运营商想要查询系统中用户数，执行如下命令：

```
DSP SMSUSRNUM:;
%%DSP SMSUSRNUM:;%%
RETCODE = 0  操作成功

结果如下：
--------
注册用户数  PODID                     

0           sms-pod-7f777cfbff-tb2pl  
1           sms-pod-7f777cfbff-n8w6n  
0           sms-pod-7f777cfbff-nm652
1           total                     
(结果个数 = 4)
```

## [输出结果说明](#ZH-CN_MMLREF_0225120882)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 注册用户数 | 该参数用于表示注册用户数。 |
| PODID | 该参数用于表示SMSF所在的POD的ID。 |
