---
id: UNC@20.15.2@MMLCommand@DSP ONECLICKDEPLOYHIST
type: MMLCommand
name: DSP ONECLICKDEPLOYHIST（显示一键式部署操作历史）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ONECLICKDEPLOYHIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# DSP ONECLICKDEPLOYHIST（显示一键式部署操作历史）

## 功能

该命令用于显示一键式部署任务的操作记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [一键式部署操作历史（ONECLICKDEPLOYHIST）](configobject/UNC/20.15.2/ONECLICKDEPLOYHIST.md)

## 使用实例

假如运营商想要查询当前环境一键式部署任务的执行情况，调用以下命令可以查询已经结束的一键式部署任务及正在执行的一键式部署任务进度。

```
%%DSP ONECLICKDEPLOYHIST:;%%
RETCODE = 0  操作成功

结果如下
--------
操作类型           节点pod列表  操作信息  开始时间           结束时间           处理结果  结果说明             

ScaleOut           isu-pod:4    NULL      20231109-11:32:41  20231109-11:32:41  处理失败  task started failed  
ScaleOut_Rollback  isu-pod:4    NULL      20231109-11:33:07  20231109-11:33:07  处理成功  NULL                 
ScaleOut           isu-pod:4    NULL      20231109-11:42:05  20231109-11:42:05  处理失败  task started failed  
ScaleOut_Rollback  isu-pod:4    NULL      20231109-11:57:33  20231109-11:57:33  处理成功  NULL                 
ScaleOut           isu-pod:4    NULL      20231109-12:11:39  20231109-12:11:40  处理失败  task started failed  
ScaleOut_Rollback  isu-pod:4    NULL      20231109-12:31:27  20231109-12:31:27  处理成功  NULL                 
(结果个数 = 6)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示一键式部署操作历史（DSP-ONECLICKDEPLOYHIST）_93751500.md`
