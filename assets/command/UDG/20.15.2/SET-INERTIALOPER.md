---
id: UDG@20.15.2@MMLCommand@SET INERTIALOPER
type: MMLCommand
name: SET INERTIALOPER（设置惯性运行功能）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: INERTIALOPER
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 业务惯性运行
status: active
---

# SET INERTIALOPER（设置惯性运行功能）

## 功能

**适用NF：UPF**

设置惯性运行功能。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IDLEUSRIGNORE | DELAYTIME | NON5GUSRIGNORE | MULPATHUSRONLIN |
| --- | --- | --- | --- | --- |
| 初始值 | ENABLE | 30 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDLEUSRIGNORE | 数据面非连接态用户是否忽略惯性运行功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制数据面非连接态用户是否忽略惯性运行功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：惯性运行功能不忽略数据面非连接态用户。<br>- ENABLE：惯性运行功能忽略数据面非连接态用户。<br>默认值：无<br>配置原则：该参数在“SET LICENSESWITCH”命令将惯性运行的license项配置为“ENABLE”时生效。 |
| DELAYTIME | PFCP路径断后延迟进入惯性运行状态时长（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个延迟时间，在路径断超过这个时间后，进入惯性运行状态。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～300，单位是秒。0到300之间的整数。<br>默认值：无<br>配置原则：无 |
| NON5GUSRIGNORE | 非5G用户是否忽略惯性运行功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制非5G用户是否忽略惯性运行功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：惯性运行功能不忽略非5G用户。<br>- ENABLE：惯性运行功能忽略非5G用户。<br>默认值：无<br>配置原则：该参数在“SET LICENSESWITCH”命令将惯性运行的license项配置为“ENABLE”时生效。 |
| MULPATHUSRONLIN | 多路径场景下路径异常时是否支持用户在线 | 可选必选说明：可选参数<br>参数含义：该参数用于控制多路径场景下路径异常时是否支持用户在线。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：无应用场景，无需配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/INERTIALOPER]] · 惯性运行功能配置（INERTIALOPER）

## 使用实例

设置惯性运行功能是否忽略数据面非连接态用户开关为关，PFCP路径断后30s进入惯性运行状态，非5G用户是否忽略惯性运行功能开关为开，多路径场景下路径异常时是否支持用户在线开关为开：

```
SET INERTIALOPER: IDLEUSRIGNORE=DISABLE, DELAYTIME=30, NON5GUSRIGNORE=ENABLE, MULPATHUSRONLIN=ENABLE;
RETCODE = 0  操作成功
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置惯性运行功能（SET-INERTIALOPER）_14588115.md`
