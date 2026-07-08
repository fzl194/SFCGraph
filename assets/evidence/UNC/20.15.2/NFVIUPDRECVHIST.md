# 查询分批升级历史（DSP NFVIUPDRECVHIST）

- [命令功能](#ZH-CN_MMLREF_0263673344__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0263673344__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0263673344__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0263673344__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0263673344__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0263673344)

该命令用于查询NFVI分批升级恢复历史记录。

## [注意事项](#ZH-CN_MMLREF_0263673344)

无

#### [操作用户权限](#ZH-CN_MMLREF_0263673344)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0263673344)

无

## [使用实例](#ZH-CN_MMLREF_0263673344)

查询NFVI分批升级历史记录。

```
%%DSP NFVIUPDRECVHIST:;%%
RETCODE = 0  操作成功

结果如下
------------------------
操作模式  =  Recovery
处理结果  =  Succeed
处理详情  =  NULL
(结果个数 = 1)
```

## [输出结果说明](#ZH-CN_MMLREF_0263673344)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 操作模式 | 操作模式类型。<br>取值说明：<br>- Recovery（升级正常结束恢复）<br>- ForceRecovery（系统异常强制恢复） |
| 处理结果 | NFVI分批升级恢复结果。<br>取值说明：<br>- Running（运行中）<br>- Succeed（成功）<br>- Failed（失败） |
| 处理详情 | NFVI分批升级恢复结果详细。 |
