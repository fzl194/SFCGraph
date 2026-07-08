---
id: UDG@20.15.2@MMLCommand@LST UPGPATTIMER
type: MMLCommand
name: LST UPGPATTIMER（查询升级补丁定时器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPGPATTIMER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 升级补丁管理
- 升级补丁参数管理
status: active
---

# LST UPGPATTIMER（查询升级补丁定时器）

## 功能

该命令用于查询升级/补丁对应定时器的时长值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 定时器名称参数 | 可选必选说明：可选参数<br>参数含义：该参数用于指示定时器名称。UpgradeStackUpdateTimer：升级堆栈更新时长。PatchStackUpdateTimer：补丁堆栈更新时长。PodDeleteTimer：POD删除时长。OSPatchPushTimer：OS补丁推送时长。UpgradeCommonTimer1~10：升级通用定时配置1。PatchCommonTimer1~10：补丁通用定时配置1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPGPATTIMER]] · 升级补丁定时器（UPGPATTIMER）

## 使用实例

查询堆栈更新定时器时长值。

```
%%LST UPGPATTIMER:NAME="UpgradeStackUpdateTimer";%%
RETCODE = 0  操作成功

结果如下
--------
  定时器名称参数  =  UpgradeStackUpdateTimer
定时器配置时长值  =  40
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPGPATTIMER.md`
