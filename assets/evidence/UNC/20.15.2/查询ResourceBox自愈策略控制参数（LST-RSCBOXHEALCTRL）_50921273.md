# 查询ResourceBox自愈策略控制参数（LST RSCBOXHEALCTRL）

- [命令功能](#ZH-CN_MMLREF_0000001450921273__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001450921273__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001450921273__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001450921273__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001450921273__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001450921273)

该命令用于查询ResourceBox自愈策略控制参数。

## [注意事项](#ZH-CN_MMLREF_0000001450921273)

该命令只适用于裸机容器云场景。

#### [操作用户权限](#ZH-CN_MMLREF_0000001450921273)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001450921273)

无

## [使用实例](#ZH-CN_MMLREF_0000001450921273)

查询ResourceBox自愈策略控制参数:

```
LST RSCBOXHEALCTRL:;
RETCODE = 0  操作成功

结果如下
--------
  ResourceBox全故障Node故障升级自愈控制 = 使能
  ResourceBox全故障Node正常升级自愈控制 = 使能
ResourceBox部分故障Node正常升级自愈控制 = 去使能
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001450921273)

| 输出项名称 | 输出项解释 |
| --- | --- |
| ResourceBox全故障Node故障升级自愈控制 | 该参数用于表示ResourceBox全部Pod故障、Node故障时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。 |
| ResourceBox全故障Node正常升级自愈控制 | 该参数用于表示ResourceBox全部Pod故障、Node正常时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。 |
| ResourceBox部分故障Node正常升级自愈控制 | 该参数用于表示ResourceBox中单个Pod或部分Pod故障、Node正常时，且进行Pod重建无法修复时，是否需要将自愈升级到ResourceBox进行复位、重建处理。 |
