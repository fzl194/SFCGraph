---
id: UNC@20.15.2@MMLCommand@STP DCNOFFLOAD
type: MMLCommand
name: STP DCNOFFLOAD（停止DCN迁移任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: DCNOFFLOAD
command_category: 动作类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- DCN迁移控制
status: active
---

# STP DCNOFFLOAD（停止DCN迁移任务）

## 功能

**适用网元：MME**

该命令用于停止当前正在进行的DCN迁移任务。

## 注意事项

此命令对类型为“IMSI(IMSI)”的迁移任务不生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [DCN迁移任务（DCNOFFLOAD）](configobject/UNC/20.15.2/DCNOFFLOAD.md)

## 使用实例

1. 停止DCN迁移任务：STP DCNOFFLOAD:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止DCN迁移任务(STP-DCNOFFLOAD)_72345723.md`
