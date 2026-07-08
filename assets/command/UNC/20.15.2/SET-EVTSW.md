---
id: UNC@20.15.2@MMLCommand@SET EVTSW
type: MMLCommand
name: SET EVTSW（设置事件开关状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: EVTSW
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET EVTSW（设置事件开关状态）

## 功能

该命令用于设置指定服务指定事件的开关状态。当使用 [**SET EVTHEALCTRL**](设置事件全局开关（SET EVTHEALCTRL）_36101118.md) 命令开启整系统事件自愈功能时，可使用本命令设置指定事件的开关状态。当使用 [**SET EVTHEALCTRL**](设置事件全局开关（SET EVTHEALCTRL）_36101118.md) 命令关闭整系统事件自愈功能时，无法使用本命令开启指定事件的自愈功能。

## 注意事项

- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICE | 服务名称 | 可选必选说明：必选参数<br>参数含义：该参数表示事件绑定的服务名称。可以通过<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无。<br>配置原则：无 |
| EVENTID | 事件ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务名称下的事件ID，可以通过<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。<br>配置原则：<br>只支持配置<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取到的服务实例。 |
| SWITCH | 事件开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示事件的开关状态。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（打开）”：自愈使能<br>- “DISABLE（不使能）”：自愈不使能<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EVTSW]] · 事件开关状态（EVTSW）

## 使用实例

设置事件1自愈开关为开。

```
%%SET EVTSW: SERVICE="SDRS", EVENTID=1, SWITCH=ENABLE;%%
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-EVTSW.md`
