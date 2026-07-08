---
id: UNC@20.15.2@MMLCommand@SET GMMPTMSIREALLOC
type: MMLCommand
name: SET GMMPTMSIREALLOC（设置Gb模式PTMSI重分配控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GMMPTMSIREALLOC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- Gb模式PTMSI重分配控制参数
status: active
---

# SET GMMPTMSIREALLOC（设置Gb模式PTMSI重分配控制参数）

## 功能

**适用网元：SGSN**

在用户接入Gb模式时， UNC 可通过此命令可以设置Gb模式下的PTMSI重分配的控制参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WITHRAUPROC | 伴随RAU流程分配 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Intra RAU流程中P-TMSI的重分配。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“YES(是)”<br>。<br>说明：- “YES(是)”：Intra RAU流程中，为用户重新分配P-TMSI。<br>- “NO(否)”：Intra RAU流程中，不为用户重新分配P-TMSI。但当RAU request消息携带的TLLI（Temporary Logic Link Identity）不为Local TLLI时，则会为用户重分配P-TMSI。 |
| REALLOCTMR | P-TMSI重分配流程间隔时长（小时） | 可选必选说明：可选参数<br>参数含义：该参数用于设定P-TMSI重分配流程的间隔时间长。如果配置为<br>“0”<br>时，PTMSI重分配功能关闭；配置为其他取值时，PTMSI重分配功能开启。<br>数据来源：整网规划<br>取值范围：0～24<br>系统初始设置值：<br>“0”<br>。<br>说明：- 扩展PTMSI重分配功能，由P-TMSI重分配流程间隔时长和P-TMSI重分配流程发起条件进行控制。<br>- 如果“P-TMSI重分配流程间隔时长（小时）”取值为“0”，不进行PTMSI重分配，与P-TMSI重分配流程发起条件无关。<br>- 当系统取值不为“0”时:- 如果“P-TMSI重分配流程发起条件”为“IN_READY_STATE（处于Ready状态）”的情况下，计时过程中的隐式P-TMSI分配不会更新p-tmsi重分配计时时间戳。<br>- 如果P-TMSI重分配流程发起条件为“AFTER_PTMSI_ALLOC（PTMSI分配后）”的情况下，PTMSI重分配不受MS状态变更的影响。当“（当前系统时间－时间戳记录时间）> PTMSI重分配时长”时，发起PTMSI重分配流程，并更新时间戳。当“（当前系统时间－时间戳记录时间）> PTMSI重分配时长”时，如果用户处于Standby状态下，则P-TMSI重分配会触发一定数量的PAGING消息，并且系统负担增加。 |
| REALLOCCOND | P-TMSI重分配流程发起条件 | 可选必选说明：可选参数<br>参数含义：该参数用于表示P-TMSI重分配流程的发起条件。<br>数据来源：整网规划<br>取值范围：<br>- “IN_READY_STATE(处于Ready状态)”<br>- “AFTER_PTMSI_ALLOC(PTMSI分配后)”<br>系统初始设置值：<br>“IN_READY_STATE(处于Ready状态)”<br>。 |

## 操作的配置对象

- [Gb模式PTMSI重分配控制参数（GMMPTMSIREALLOC）](configobject/UNC/20.15.2/GMMPTMSIREALLOC.md)

## 使用实例

设置Gb模式PTMSI重分配控制参数，设置WITHRAUPROC（伴随RAU流程分配）为NO（否），REALLOCTMR（P-TMSI重分配流程间隔时长（小时））为1，REALLOCCOND（P-TMSI重分配流程发起条件）为IN_READY_STATE（处于Ready状态）：

SET GMMPTMSIREALLOC: WITHRAUPROC=NO, REALLOCTMR=1, REALLOCCOND=IN_READY_STATE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Gb模式PTMSI重分配控制参数（SET-GMMPTMSIREALLOC）_26145520.md`
