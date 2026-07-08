---
id: UNC@20.15.2@MMLCommand@SET LINKCONGCTRL
type: MMLCommand
name: SET LINKCONGCTRL（设置Diameter链路拥塞控制）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LINKCONGCTRL
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diameter链路拥塞控制
status: active
---

# SET LINKCONGCTRL（设置Diameter链路拥塞控制）

## 功能

**适用NF：PGW-C、SMF**

此命令用于设置Diameter链路拥塞触发告警和链路重建的相关参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- UNC以6小时为一个告警抑制周期。在告警抑制周期内，只有由参数AlmRptDtctPrd设置的检测周期中链路拥塞率（此链路由于链路拥塞丢弃的消息数与此链路传输的总消息数的比率）一直达到参数AlmCongRate设置值才会上报告警。非告警抑制周期内，链路拥塞率达到参数AlmCongRate设置值立即上报告警，进入告警抑制周期。
- UNC每5秒检测一次链路状态，在参数AlmClrDtcPrd设置的检查周期内，链路均未由于链路拥塞丢弃过消息，则恢复“ALM-81057 接口拥塞”告警。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | ALMSWITCH | ALMCONGRATE | ALMRPTDTCTPRD | ALMCLRDTCTPRD | REESTABLISHSW | REESTCONGRATE | REESTABLISHPRD |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | ENABLE | 20 | 12 | 12 | DISABLE | 80 | 255 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMSWITCH | 告警开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置链路拥塞是否触发上报告警。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| ALMCONGRATE | 触发告警上报的链路拥塞率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置链路触发“ALM-81057 接口拥塞”告警的链路拥塞率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～80。<br>默认值：无<br>配置原则：无 |
| ALMRPTDTCTPRD | 告警上报检测周期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数设置用于上报告警的链路拥塞状态检测周期。如果设置该参数为N，则链路拥塞状态检测周期为N*5秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～60。<br>默认值：无<br>配置原则：无 |
| ALMCLRDTCTPRD | 告警恢复检测周期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ALMSWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数设置用于恢复告警的链路拥塞状态检测周期。如果设置该参数为N，则链路拥塞状态检测周期为N*5秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～60。<br>默认值：无<br>配置原则：无 |
| REESTABLISHSW | 链路重建开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置链路拥塞是否触发链路重建的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：无 |
| REESTCONGRATE | 触发链路重建的链路拥塞率 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REESTABLISHSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置触发链路重建的链路拥塞率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为5～100。<br>默认值：无<br>配置原则：无 |
| REESTABLISHPRD | 链路重建的检测周期 | 可选必选说明：条件可选参数<br>前提条件：该参数在“REESTABLISHSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数设置用于主动拆链并重建链路的链路拥塞状态检测周期。如果设置该参数为N，则链路拥塞状态检测周期为N*5秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LINKCONGCTRL]] · Diameter链路拥塞控制（LINKCONGCTRL）

## 使用实例

配置链路拥塞触发告警功能开启：

```
SET LINKCONGCTRL: ALMSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LINKCONGCTRL.md`
