---
id: UDG@20.15.2@MMLCommand@SET PROCFAULTALM
type: MMLCommand
name: SET PROCFAULTALM（设置进程故障告警上报模式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PROCFAULTALM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# SET PROCFAULTALM（设置进程故障告警上报模式）

## 功能

设置进程故障告警上报模式。进程故障告警快速上报使能位开启时，出现一次进程异常就立刻上报告警。进程故障告警快速上报使能位关闭时，在1分钟内出现3次进程故障才会上报告警。

## 注意事项

- 该命令执行后立即生效。
- 进程故障告警快速上报使能位开启时，出现一次进程异常就立刻上报告警。进程故障告警快速上报使能位关闭时，在1分钟内出现3次进程故障才会上报告警。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| ISTRGALMIMMDTLY |
| --- |
| Disable |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISTRGALMIMMDTLY | 告警快速上报使能位 | 可选必选说明：必选参数<br>参数含义：告警快速上报使能位。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Disable：去使能。<br>- Enable：使能。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PROCFAULTALM]] · 进程故障告警上报模式（PROCFAULTALM）

## 使用实例

设置进程故障告警上报模式：

```
SET PROCFAULTALM:ISTRGALMIMMDTLY=Enable
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PROCFAULTALM.md`
