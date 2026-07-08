---
id: UNC@20.15.2@MMLCommand@STR VLROFFLOADBYLAI
type: MMLCommand
name: STR VLROFFLOADBYLAI（启动IMSI分离4G用户任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: VLROFFLOADBYLAI
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- 基于LAI的IMSI分离业务
status: active
---

# STR VLROFFLOADBYLAI（启动IMSI分离4G用户任务）

## 功能

![](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.assets/notice_3.0-zh-cn_2.png)

- 执行前请确认LAI列表配置正确，避免非预期用户IMSI Detach。
- 执行前请确认MSC侧已开启相关流控功能，避免SGs接口以及对端MSC设备的负荷增加。

**适用网元：MME**

本命令用于对LAI列表中所有LAI对应的TAI下面联合附着的4G用户执行IMSI分离操作。执行操作前必须确保已通过 [**ADD VLROFFLOADLAILST**](../基于LAI的IMSI分离配置信息/增加位置区列表(ADD VLROFFLOADLAILST)_26305242.md) 命令将待处理的LAI添加到LAI列表。

## 注意事项

- 如果LAI列表为空，命令会执行失败。
- 启动扫描任务前必须确保已通过[**LST VLROFFLOADLAILST**](../基于LAI的IMSI分离配置信息/查询位置区列表(LST VLROFFLOADLAILST)_26145428.md)确认LAI列表配置正确，以避免非预期用户IMSI分离。
- 用户可以通过命令[**DSP VLROFFLOADBYLAI**](显示IMSI分离4G用户任务运行状态(DSP VLROFFLOADBYLAI)_26145426.md)查询扫描任务的运行状态和处理进度。扫描任务的运行状态为“正在运行”时，无法立即启动新的扫描任务。
- 任务处理速度由命令[**SET VLROFFLOADINF**](../VLR迁移配置信息/设置VLR迁移配置信息(SET VLROFFLOADINF)_72345023.md)中的VLROFFLODSPD参数设置，推荐使用系统初始设置值，避免任务处理速度设置不合理，导致系统CPU占有率上升。
- 此命令涉及CSFB被叫恢复特性（特性编号：WSFD-102503，license部件编码：LKV2CSCR01），执行命令前请使用[**DSP LICENSE**](../../../../../../平台服务管理/操作维护/License管理/显示License(DSP LICENSE)_00360098.md)命令确认对应特性license是否得到授权，执行[**LST LICENSESWITCH**](../../../../../../平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令确认特性开关状态为“打开”。
- UNC倒换场景下，用户迁移不可用。
- 执行前请确认LAI列表配置正确，避免非预期用户IMSI Detach。
- 执行前请确认MSC侧已开启相关流控功能，避免SGs接口以及对端MSC设备的负荷增加。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADBYLAI]] · IMSI分离4G用户任务（VLROFFLOADBYLAI）

## 使用实例

对 [**ADD VLROFFLOADLAILST**](../基于LAI的IMSI分离配置信息/增加位置区列表(ADD VLROFFLOADLAILST)_26305242.md) 配置的所有LAI对应的TAI下面联合附着的4G用户，执行IMSI分离操作：

STR VLROFFLOADBYLAI:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-VLROFFLOADBYLAI.md`
