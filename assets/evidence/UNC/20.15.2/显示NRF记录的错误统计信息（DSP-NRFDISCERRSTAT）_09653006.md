# 显示NRF记录的错误统计信息（DSP NRFDISCERRSTAT）

- [命令功能](#ZH-CN_MMLREF_0209653006__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209653006__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209653006__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209653006__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209653006__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209653006)

**适用NF：NRF**

该命令用于查询NF服务发现过程中NRF记录的错误统计信息，用于支撑定位问题。

## [注意事项](#ZH-CN_MMLREF_0209653006)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209653006)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209653006)

无

## [使用实例](#ZH-CN_MMLREF_0209653006)

查询NRF记录的错误统计信息：

```
 DSP NRFDISCERRSTAT:;
%% DSP NRFDISCERRSTAT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
CellServiceID  错误描述                                  错误统计次数  最后一次错误发生的时间

0              queryNfInstancesByTai_RecordNotFoundErr   11            2019-09-17 08:14:38.921196576 +0       
0              DiscDslFinal_DiscDslFinalErr              25            2019-09-17 08:10:36.156884259 +0   
(结果个数 = 2)
```

## [输出结果说明](#ZH-CN_MMLREF_0209653006)

| 输出项名称 | 输出项解释 |
| --- | --- |
| CellServiceID | 该参数用于表示Cell Service ID。 |
| 错误描述 | 该参数用于表示NRF在处理NF服务发现过程中对应Cell Service ID的特定错误描述。 |
| 错误统计次数 | 该参数用于表示当前Cell Service ID对应错误的错误统计次数。 |
| 最后一次错误发生的时间 | 该参数用于表示Cell Service ID发生错误时，对应的最后一次错误发生的时间。 |
