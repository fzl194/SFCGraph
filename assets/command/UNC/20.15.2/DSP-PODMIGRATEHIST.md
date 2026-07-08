---
id: UNC@20.15.2@MMLCommand@DSP PODMIGRATEHIST
type: MMLCommand
name: DSP PODMIGRATEHIST（显示节点扩缩容任务进展）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PODMIGRATEHIST
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# DSP PODMIGRATEHIST（显示节点扩缩容任务进展）

## 功能

查询最近一次下发命令 [**OPR PODMIGRATE**](操作节点扩缩容与Pod迁移任务（OPR PODMIGRATE）_42938091.md) 触发的节点扩容/缩容任务进度和状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：扩容/缩容的节点类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manager_Service（ManagerService）”：管理类服务所在节点如PBU-A扩缩容及相关pod迁移。<br>- “OM_Service（OMService）”：运维类服务所在节点如OMU的扩缩容及相关pod迁移。<br>默认值：无<br>配置原则：无 |
| SCALETYPE | 迁移类型 | 可选必选说明：必选参数<br>参数含义：节点迁移类型，如扩容/缩容。<br>数据来源：本端规划<br>取值范围：<br>- ScaleOut（扩容迁移）<br>- ScaleIn（缩容迁移）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PODMIGRATEHIST]] · 节点扩缩容任务进展（PODMIGRATEHIST）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示节点扩缩容任务进展（DSP-PODMIGRATEHIST）_42938050.md`
