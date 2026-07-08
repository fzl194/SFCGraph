---
id: UNC@20.15.2@MMLCommand@SET DMOCCFG
type: MMLCommand
name: SET DMOCCFG（设置Diameter流控控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DMOCCFG
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Diameterl流控管理
status: active
---

# SET DMOCCFG（设置Diameter流控控制参数）

## 功能

**适用网元：SGSN、MME**

该命令用于设置Diameter流控控制参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SNTHD | Diameter流控Sequence Number有效变化门限值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置Diameter流控判断Overload Report中Sequence Number有效变化的门限值。<br>数据来源：本端规划<br>取值范围: 1~1000000<br>系统初始值：10000<br>配置原则：无<br>默认值：无 |
| ULRCAUSE | Diameter流控导致ULR拒绝原因值 | 可选必选说明：可选参数。<br>参数含义：该参数用于设置因S6a接口Diameter流控而导致ULR流程失败时，下发给UE的原因值。<br>数据来源：整网规划。<br>取值范围：整数取值范围0~111。<br>系统初始值：0。<br>默认值：无<br>配置原则：<br>- 参数取值为0，表示不使用特殊指定原因值，系统默认下发#22（Congestion）原因值。<br>- 原因值为1表示非协议定义原因值，不建议配置。<br>- 参数修改为非0值，可能会改变此参数所控制的场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |
| AIRCAUSE | Diameter流控导致AIR拒绝原因值 | 可选必选说明：可选参数。<br>参数含义：该参数用于设置因S6a接口Diameter流控而导致AIR流程失败时，下发给UE的原因值。<br>数据来源：整网规划。<br>取值范围：整数取值范围0~111。<br>默认值：无<br>系统初始值：0。<br>配置原则：<br>- 参数取值为0，表示不使用特殊指定原因值，系统默认下发#22（Congestion）原因值。<br>- 原因值为1表示非协议定义原因值，不建议配置。<br>- 参数修改为非0值，可能会改变此参数所控制的场景中下发给终端的拒绝原因值，从而导致相应拒绝类话统指标的变化。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMOCCFG]] · Diameter流控控制参数（DMOCCFG）

## 使用实例

Diameter流控导致ULR流程失败时，预期下发#15（No suitable cells in ta）：

SET DMOCCFG: ULRCAUSE=15;

Diameter流控导致AIR流程失败时，预期下发#17（Network failure）：

SET DMOCCFG: AIRCAUSE=17;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DMOCCFG.md`
