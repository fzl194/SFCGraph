# 显示节点扩缩容任务进展（DSP PODMIGRATEHIST）

- [命令功能](#ZH-CN_MMLREF_0242938050__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0242938050__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0242938050__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0242938050__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0242938050__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0242938050)

查询最近一次下发命令 [**OPR PODMIGRATE**](操作节点扩缩容与Pod迁移任务（OPR PODMIGRATE）_42938091.md) 触发的节点扩容/缩容任务进度和状态。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0242938050)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0242938050)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：扩容/缩容的节点类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manager_Service（ManagerService）”：管理类服务所在节点如PBU-A扩缩容及相关pod迁移。<br>- “OM_Service（OMService）”：运维类服务所在节点如OMU的扩缩容及相关pod迁移。<br>默认值：无<br>配置原则：无 |
| SCALETYPE | 迁移类型 | 可选必选说明：必选参数<br>参数含义：节点迁移类型，如扩容/缩容。<br>数据来源：本端规划<br>取值范围：<br>- ScaleOut（扩容迁移）<br>- ScaleIn（缩容迁移）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0242938050)

查询Manager服务最近一次扩容迁移进度。

```
%%DSP PODMIGRATEHIST: SERVICETYPE=Manager_Service, SCALETYPE=ScaleOut;%%
RETCODE = 0  操作成功

结果如下
------------------------
迁移任务状态  =  迁移完成
    迁移进度  =  100%
    结果说明  =  NULL
        阶段  =  阶段二
(Number of results = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0242938050)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 迁移任务状态 | 最近一次下发的<br>[**OPR PODMIGRATE**](操作节点扩缩容与Pod迁移任务（OPR PODMIGRATE）_42938091.md)<br>命令触发的节点扩容/缩容迁移任务状态。<br>取值说明：<br>- Processing（迁移中）<br>- Finished（迁移完成）<br>- “Failed（迁移失败）”：如果是扩容时迁移失败，则需要执行OPR PODMIGRATE进行缩容回退；如果是缩容时迁移失败，则重新执行OPR PODMIGRATE进行缩容重试。<br>- “NoOpr（迁移任务未下发）”：扩容/缩容任务未成功下发，请重新执行OPR PODMIGRATE下发扩容/缩容迁移任务。 |
| 迁移进度 | 最近一次下发的<br>[**OPR PODMIGRATE**](操作节点扩缩容与Pod迁移任务（OPR PODMIGRATE）_42938091.md)<br>命令触发的节点扩容/缩容迁移任务进度。 |
| 结果说明 | 节点扩容/缩容任务进度的说明，若任务失败显示失败原因。 |
| 阶段 | 显示当前或当前迁移任务发生前的部署形态。<br>取值说明：<br>- “StageOne（阶段一）”：当前部署为小规格或处于小规格向大规格迁移过程中。<br>- “StageTwo（阶段二）”：当前部署为大规格或处于大规格向小规格迁移过程中。 |
