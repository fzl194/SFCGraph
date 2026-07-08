---
id: UNC@20.15.2@MMLCommand@SET PMMPTMSIREALLOC
type: MMLCommand
name: SET PMMPTMSIREALLOC（设置Iu模式PTMSI重分配控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PMMPTMSIREALLOC
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
- Iu模式PTMSI重分配控制参数
status: active
---

# SET PMMPTMSIREALLOC（设置Iu模式PTMSI重分配控制参数）

## 功能

**适用网元：SGSN**

在用户接入Iu模式时， UNC 可通过此命令可以设置Iu模式下的PTMSI重分配的控制参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WITHRAUPROC | 伴随RAU流程分配 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Intra RAU流程中P-TMSI的重分配。<br>数据来源：整网规划<br>取值范围：<br>- “YES(是)”<br>- “NO(否)”<br>系统初始设置值：<br>“YES(是)”<br>。<br>说明：- “YES(是)”：Intra RAU流程中，为用户重新分配P-TMSI。<br>- “NO(否)”：Intra RAU流程中，不为用户重新分配P-TMSI。 |
| REALLOCTMR | P-TMSI重分配流程间隔时长（小时） | 可选必选说明：可选参数<br>参数含义：该参数用于设定P-TMSI重分配流程的间隔时间长。如果配置为<br>“0”<br>时，PTMSI重分配功能关闭；配置为其他取值时，PTMSI重分配功能开启。<br>数据来源：整网规划<br>取值范围：0～24<br>系统初始设置值：<br>“0”<br>。<br>说明：- 扩展PTMSI重分配功能，由“P-TMSI重分配流程间隔时长（小时）”和“P-TMSI重分配流程发起条件”进行控制。如果<br>“P-TMSI重分配流程间隔时长（小时）”<br>取值为<br>“0”<br>，不进行PTMSI重分配，与<br>“P-TMSI重分配流程发起条件”<br>无关。<br>- 当系统取值不为“0”时:- 不管“P-TMSI重分配流程发起条件”为“IN_PMM_CONNECTED_STATE（处于PMM-CONNECTED状态）”还是“AFTER_PTMSI_ALLOC（PTMSI分配后）”，RAB有效时都不会发起P-TMSI重分配流程，时间戳不重置，直到下一次满足分配条件时再发起P-TMSI重分配然后相应地重置重分配时间戳。 |
| REALLOCCOND | P-TMSI重分配流程发起条件 | 可选必选说明：可选参数<br>参数含义：该参数用于表示P-TMSI重分配流程的发起条件。<br>数据来源：整网规划<br>取值范围：<br>- “IN_PMM_CONNECTED_STATE(处于PMM-CONNECTED状态)”<br>- “AFTER_PTMSI_ALLOC(PTMSI分配后)”<br>系统初始设置值：<br>“IN_PMM_CONNECTED_STATE(处于PMM-CONNECTED状态)”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PMMPTMSIREALLOC]] · Iu模式PTMSI重分配控制参数（PMMPTMSIREALLOC）

## 使用实例

设置Iu模式PTMSI重分配控制参数，设置 “WITHRAUPROC（伴随RAU流程分配）” 为 “NO（否）” ， “REALLOCTMR（P-TMSI重分配流程间隔时长（小时））” 为 “1” ， “REALLOCCOND（P-TMSI重分配流程发起条件）” 为 “AFTER_PTMSI_ALLOC（PTMSI分配后）” ：

SET PMMPTMSIREALLOC: WITHRAUPROC=NO, REALLOCTMR=1, REALLOCCOND=AFTER_PTMSI_ALLOC;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置Iu模式PTMSI重分配控制参数(SET-PMMPTMSIREALLOC)_72345119.md`
