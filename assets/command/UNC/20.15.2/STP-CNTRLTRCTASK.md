---
id: UNC@20.15.2@MMLCommand@STP CNTRLTRCTASK
type: MMLCommand
name: STP CNTRLTRCTASK（停止跨层统一联动跟踪任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: CNTRLTRCTASK
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- 工程调测
- 5G工程命令
status: active
---

# STP CNTRLTRCTASK（停止跨层统一联动跟踪任务）

## 功能

该命令用于停止跨层统一联动跟踪任务。

## 注意事项

- 该命令执行后立即生效。

- 该命令仅在虚机场景下支持，并且仅支持FusionSphere用户态EVS和用户态OVS组网。
- 该命令会触发PAE和FusionSphere跟踪任务停止，当PAE或FusionSphere的停止跟踪任务返回失败时，如PAE或FusionSphere跟踪任务已经异常停止，该命令会执行失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 任务ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示停止跨层统一联动跟踪任务的任务ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是14。<br>默认值：无<br>配置原则：<br>该参数可通过DSP CNTRLTRCTASK命令查询。 |

## 操作的配置对象

- [跨层统一联动跟踪任务（CNTRLTRCTASK）](configobject/UNC/20.15.2/CNTRLTRCTASK.md)

## 使用实例

停止跨层统一联动跟踪任务：

```
%%STP CNTRLTRCTASK: TASKID="20220301223015";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止跨层统一联动跟踪任务（STP-CNTRLTRCTASK）_73335361.md`
