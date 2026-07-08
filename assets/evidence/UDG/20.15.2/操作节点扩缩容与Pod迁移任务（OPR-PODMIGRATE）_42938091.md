# 操作节点扩缩容与Pod迁移任务（OPR PODMIGRATE）

- [命令功能](#ZH-CN_MMLREF_0242938091__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0242938091__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0242938091__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0242938091__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0242938091)

该命令用于PBU-A等控制类服务所在节点扩缩容或OMU等运维类服务所在节点扩缩容，扩缩容过程中会进行Pod迁移。该命令主要用于现网需要从小规格部署形态向大规格部署形态变化的扩容场景。如果扩容时失败，把缩容回退作为逃生手段。

> **说明**
> 该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0242938091)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0242938091)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：扩容/缩容的节点类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manager_Service（ManagerService）”：管理类服务所在节点如PBU-A扩缩容及相关pod迁移。<br>- “OM_Service（OMService）”：运维类服务所在节点如OMU的扩缩容及相关pod迁移。<br>默认值：无<br>配置原则：无 |
| SCALETYPE | 迁移类型 | 可选必选说明：必选参数<br>参数含义：节点迁移类型，如扩容/缩容。<br>数据来源：本端规划<br>取值范围：<br>- ScaleOut（扩容迁移）<br>- ScaleIn（缩容迁移）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0242938091)

- OM服务小规格向大规格扩容迁移。
  ```
  OPR PODMIGRATE: SERVICETYPE=OM_Service, SCALETYPE=ScaleOut;
  ```
- OM服务回退缩容迁移。
  ```
  OPR PODMIGRATE: SERVICETYPE=OM_Service, SCALETYPE=ScaleIn;
  ```
