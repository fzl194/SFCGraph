---
id: UNC@20.15.2@MMLCommand@RTR LOGAGENTSTC
type: MMLCommand
name: RTR LOGAGENTSTC（清除日志代理丢弃的日志信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: LOGAGENTSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 日志管理
status: active
---

# RTR LOGAGENTSTC（清除日志代理丢弃的日志信息）

## 功能

该命令用于清除日志代理丢弃的日志信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程ID | 可选必选说明：必选参数<br>参数含义：进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOGAGENTSTC]] · 日志代理丢弃的日志信息（LOGAGENTSTC）

## 使用实例

清除日志代理丢弃的告警日志统计信息，可通过执行如下命令：

```
RTR LOGAGENTSTC:PROCESSID=3
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-LOGAGENTSTC.md`
