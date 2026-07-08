# 查询升级补丁定时器（LST UPGPATTIMER）

- [命令功能](#ZH-CN_MMLREF_0230310142__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0230310142__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0230310142__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0230310142__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0230310142__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0230310142)

该命令用于查询升级/补丁对应定时器的时长值。

> **说明**
> 无

#### [操作用户权限](#ZH-CN_MMLREF_0230310142)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0230310142)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 定时器名称参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指示定时器名称。UpgradeStackUpdateTimer：升级堆栈更新时长。PatchStackUpdateTimer：补丁堆栈更新时长。PodDeleteTimer：POD删除时长。OSPatchPushTimer：OS补丁推送时长。UpgradeCommonTimer1~10：升级通用定时配置1。PatchCommonTimer1~10：补丁通用定时配置1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0230310142)

查询堆栈更新定时器时长值。

```
%%LST UPGPATTIMER:NAME="UpgradeStackUpdateTimer";%%
RETCODE = 0  操作成功

结果如下
--------
  定时器名称参数  =  UpgradeStackUpdateTimer
定时器配置时长值  =  40
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0230310142)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 定时器名称参数 | 该参数用于指示定时器名称。UpgradeStackUpdateTimer：升级堆栈更新时长。PatchStackUpdateTimer：补丁堆栈更新时长。PodDeleteTimer：POD删除时长。OSPatchPushTimer：OS补丁推送时长。UpgradeCommonTimer1~10：升级通用定时配置1。PatchCommonTimer1~10：补丁通用定时配置1。 |
| 定时器配置时长值 | 该参数用于设置指定定时器的配置时长。 |
