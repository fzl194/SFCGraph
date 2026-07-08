---
id: UNC@20.15.2@MMLCommand@STP VLROFFLOADBYLAI
type: MMLCommand
name: STP VLROFFLOADBYLAI（停止IMSI分离4G用户任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: VLROFFLOADBYLAI
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
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

# STP VLROFFLOADBYLAI（停止IMSI分离4G用户任务）

## 功能

**适用网元：MME**

用户通过 [启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) [**STR VLROFFLOADBYLAI**](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 启动扫描任务后，如果发现系统负荷过载或者LAI列表配置错误，可以执行本命令停止扫描任务，终止对于4G用户的IMSI分离操作。

## 注意事项

- 此命令执行后立即生效。
- LAI列表配置可以通过命令[**LST VLROFFLOADLAILST**](../基于LAI的IMSI分离配置信息/查询位置区列表(LST VLROFFLOADLAILST)_26145428.md)查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLROFFLOADBYLAI]] · IMSI分离4G用户任务（VLROFFLOADBYLAI）

## 使用实例

停止由 [启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) [**STR VLROFFLOADBYLAI**](启动IMSI分离4G用户任务(STR VLROFFLOADBYLAI)_26305240.md) 启动的扫描任务，终止对于4G用户的IMSI分离操作：

STP VLROFFLOADBYLAI:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/STP-VLROFFLOADBYLAI.md`
