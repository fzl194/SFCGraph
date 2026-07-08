---
id: UNC@20.15.2@MMLCommand@SET LOGCLEANPOLICY
type: MMLCommand
name: SET LOGCLEANPOLICY（设置日志老化策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LOGCLEANPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET LOGCLEANPOLICY（设置日志老化策略）

## 功能

本命令用于设置审计日志老化策略。

日志老化策略包括日志存留期和日志占用空间，用于设置系统对日志的最大存留时长和最大占用空间大小。当日志超过最大存留时长或者最大占用空间大小时，系统按照日志产生时间，删除最老的日志。

## 注意事项

- 该命令存在系统初始记录，参数CLEANPERIOD（日志存留期）初始值为365（天），参数CLEANTHRESHOLD（日志占用空间）初始值为400（MB）。
- 该命令设置的参数可在OM Portal页面“安全 > 日志审计 > 日志配置”中查看配置结果。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| CLEANPERIOD | 日志存留期（天） | 可选必选说明：必选参数。<br>参数含义：用于设置日志存留天数。<br>取值范围：7~365。<br>默认值：365。<br>配置原则：无。 |
| CLEANTHRESHOLD | 日志占用空间（MB） | 可选必选说明：必选参数。<br>参数含义：用于设置日志占用空间。<br>取值范围：120~1000。<br>默认值：400。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOGCLEANPOLICY]] · 日志老化策略（LOGCLEANPOLICY）

## 使用实例

设置日志老化策略：

```
%%SET LOGCLEANPOLICY: CLEANPERIOD=90, CLEANTHRESHOLD=120;%% 
RETCODE = 0  操作成功 
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LOGCLEANPOLICY.md`
