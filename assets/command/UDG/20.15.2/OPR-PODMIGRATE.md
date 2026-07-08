---
id: UDG@20.15.2@MMLCommand@OPR PODMIGRATE
type: MMLCommand
name: OPR PODMIGRATE（操作节点扩缩容与Pod迁移任务）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: PODMIGRATE
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 部署规格管理
status: active
---

# OPR PODMIGRATE（操作节点扩缩容与Pod迁移任务）

## 功能

该命令用于PBU-A等控制类服务所在节点扩缩容或OMU等运维类服务所在节点扩缩容，扩缩容过程中会进行Pod迁移。该命令主要用于现网需要从小规格部署形态向大规格部署形态变化的扩容场景。如果扩容时失败，把缩容回退作为逃生手段。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：扩容/缩容的节点类型。<br>数据来源：本端规划<br>取值范围：<br>- “Manager_Service（ManagerService）”：管理类服务所在节点如PBU-A扩缩容及相关pod迁移。<br>- “OM_Service（OMService）”：运维类服务所在节点如OMU的扩缩容及相关pod迁移。<br>默认值：无<br>配置原则：无 |
| SCALETYPE | 迁移类型 | 可选必选说明：必选参数<br>参数含义：节点迁移类型，如扩容/缩容。<br>数据来源：本端规划<br>取值范围：<br>- ScaleOut（扩容迁移）<br>- ScaleIn（缩容迁移）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PODMIGRATE]] · 操作节点扩缩容与Pod迁移任务（PODMIGRATE）

## 使用实例

- OM服务小规格向大规格扩容迁移。
  ```
  OPR PODMIGRATE: SERVICETYPE=OM_Service, SCALETYPE=ScaleOut;
  ```
- OM服务回退缩容迁移。
  ```
  OPR PODMIGRATE: SERVICETYPE=OM_Service, SCALETYPE=ScaleIn;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/OPR-PODMIGRATE.md`
