---
id: UNC@20.15.2@MMLCommand@RST PCCTIMER
type: MMLCommand
name: RST PCCTIMER（复位PCC定时器）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: PCCTIMER
command_category: 动作类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 信令控制
- 复位PCC定时器
status: active
---

# RST PCCTIMER（复位PCC定时器）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于重启PCC定时器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERTYPE | PCC定时器 | 可选必选说明：必选参数<br>参数含义：该参数用于在supported-features动态协商功能使能时，手动重启定时器，并清除UNC本地缓存的所有PCRF的实际feature支持能力。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SUPFEA_NEGO_TMR：动态协商定时器。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCCTIMER]] · 复位PCC定时器（PCCTIMER）

## 使用实例

如果希望重启动态协商定时器，清除UNC本地缓存的所有PCRF的实际feature支持能力，则可以进行如下设置：

```
RST PCCTIMER: TIMERTYPE=SUPFEA_NEGO_TMR;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RST-PCCTIMER.md`
