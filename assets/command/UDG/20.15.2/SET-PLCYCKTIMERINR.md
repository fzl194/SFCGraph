---
id: UDG@20.15.2@MMLCommand@SET PLCYCKTIMERINR
type: MMLCommand
name: SET PLCYCKTIMERINR（设置策略类型和核查间隔）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PLCYCKTIMERINR
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# SET PLCYCKTIMERINR（设置策略类型和核查间隔）

## 功能

该命令用于设置策略类型和核查间隔。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | POLICYTYPE | INTERVAL |
> | --- | --- |
> | Inner | 1 |
> | Outer | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYTYPE | 策略类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略类型，Inner表示内部策略，Outer表示外部策略。<br>数据来源：本端规划<br>取值范围：<br>- Inner（内部策略）<br>- Outer（外部通信策略）<br>默认值：无。<br>配置原则：无 |
| INTERVAL | 策略核查时间间隔 (分钟) | 可选必选说明：必选参数<br>参数含义：该参数用于设置策略核查时间间隔，单位分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295，单位是分钟。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PLCYCKTIMERINR]] · 策略类型和核查间隔（PLCYCKTIMERINR）

## 使用实例

设置策略类型和核查间隔，内部策略用Inner，外部策略用Outer，核查间隔单位为分钟。

```
%%SET PLCYCKTIMERINR: POLICYTYPE=Inner, INTERVAL=1;%%
RETCODE = 0  操作成功

---    结束
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-PLCYCKTIMERINR.md`
