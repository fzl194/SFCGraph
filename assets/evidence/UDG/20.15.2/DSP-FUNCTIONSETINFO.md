# 显示网络功能集全局列表（DSP FUNCTIONSETINFO）

- [命令功能](#ZH-CN_MMLREF_0318818226__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0318818226__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0318818226__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0318818226__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0318818226__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0318818226)

该命令用于显示全量网络功能列表。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0318818226)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0318818226)

无

## [使用实例](#ZH-CN_MMLREF_0318818226)

DSP FUNCTIONSETINFO;

```
%%DSP FUNCTIONSETINFO:;%%
RETCODE =0 操作成功
结果如下
-------
网络功能集名称      Pod类型                               动态上下线开关
xxx-4G              vusn-pod:0,gtp-pod:0,vusnom-pod:0     是
xxx-pfcp            vsm-pod:0                             是
```

## [输出结果说明](#ZH-CN_MMLREF_0318818226)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网络功能集名称 | 网络功能集名称。 |
| pod类型 | pod类型。 |
| 动态上下线开关 | 动态上下线开关。<br>取值说明：<br>- TRUE(TRUE)<br>- FALSE(FALSE) |
