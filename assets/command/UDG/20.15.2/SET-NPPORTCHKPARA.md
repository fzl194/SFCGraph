---
id: UDG@20.15.2@MMLCommand@SET NPPORTCHKPARA
type: MMLCommand
name: SET NPPORTCHKPARA（设置NP端口检测的参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPPORTCHKPARA
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP端口检测参数
status: active
---

# SET NPPORTCHKPARA（设置NP端口检测的参数）

## 功能

该命令用来设置NP端口检测的参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
  | INTLBWALMRPTTHD | INTLBWALMRCYTHD | EXTLBWALMRPTTHD | EXTLBWALMRCYTHD | NP2NPRSTSW | NP2NPRSTTHR | TBPORTCHKSW | VLDDRTNTHD | UPDCHKPRDMULT |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | 95 | 90 | 90 | 80 | 使能 | 3 | 使能 | 2000 | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTLBWALMRPTTHD | 内联口带宽利用率告警上报阈值（%） | 可选必选说明：可选参数。<br>参数含义：NP内联端口带宽利用率的告警阈值，当NP内联端口带宽利用率超过该阈值时上报告警“ALM-89006 NP接口流量带宽利用率超过告警阈值”。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为70~100，单位是百分比。<br>默认值：无。<br>配置原则：必须大于“内联口带宽利用率告警恢复阈值”参数的配置值。 |
| INTLBWALMRCYTHD | 内联口带宽利用率告警恢复阈值（%） | 可选必选说明：可选参数。<br>参数含义：NP内联端口带宽利用率的告警恢复阈值，当NP内联端口带宽利用率小于该阈值时恢复告警“ALM-89006 NP接口流量带宽利用率超过告警阈值”。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为60~99，单位是百分比。<br>默认值：无。<br>配置原则：必须小于“内联口带宽利用率告警上报阈值”参数的配置值。 |
| EXTLBWALMRPTTHD | 外联口带宽利用率告警上报阈值（%） | 可选必选说明：可选参数。<br>参数含义：NP外联端口带宽利用率的告警阈值，当NP外联端口带宽利用率超过该阈值时上报告警“ALM-89006 NP接口流量带宽利用率超过告警阈值”。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为70~100，单位是百分比。<br>默认值：无。<br>配置原则：必须大于“外联口带宽利用率告警恢复阈值”参数的配置值。 |
| EXTLBWALMRCYTHD | 外联口带宽利用率告警恢复阈值（%） | 可选必选说明：可选参数。<br>参数含义：NP外联端口带宽利用率的告警恢复阈值，当NP外联端口带宽利用率小于该阈值时恢复告警“ALM-89006 NP接口流量带宽利用率超过告警阈值”。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为60~99，单位是百分比。<br>默认值：无。<br>配置原则：必须小于“外联口带宽利用率告警上报阈值”参数的配置值。 |
| NP2NPRSTSW | NP间端口故障自愈开关 | 可选必选说明：可选参数。<br>参数含义：单板内多个NP间端口链路故障自愈开关。<br>数据来源：本端规划。<br>取值范围：<br>- DISABLE(去使能)<br>- ENABLE(使能)<br>默认值：无。<br>配置原则：无。 |
| NP2NPRSTTHR | NP间端口故障时长阈值（秒） | 可选必选说明：条件可选参数。<br>前提条件：该参数在“NP2NPRSTSW”配置为“ENABLE”时为条件可选参数。<br>参数含义：NP间端口链路故障时长超过该配置值后，复位单板尝试自愈。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为3~60，单位是秒。<br>默认值：无。<br>配置原则：无。 |
| TBPORTCHKSW | TB出端口检测开关 | 可选必选说明：可选参数。<br>参数含义：该参数用于设置检测NP内POD TB出端口状态的开关。<br>数据来源：本端规划。<br>取值范围：<br>- DISABLE(去使能)<br>- ENABLE(使能)<br>默认值：无。<br>配置原则：无。 |
| VLDDRTNTHD | TB出端口无效的时长阈值（毫秒） | 可选必选说明：条件可选参数。<br>前提条件：该参数在“TBPORTCHKSW”配置为“ENABLE”时为条件可选参数。<br>参数含义：该参数用于设置NP内POD TB出端口无效时长阈值。如果无效状态持续时长超过该配置值，则上报告警。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为600~180000，单位是毫秒。<br>默认值：无。<br>配置原则：<br>- 该参数配置值要大于**[SET GLOBALFABRICOAM](../../../../系统调测/PAE 调测命令/配置/设置OAM全局配置（SET GLOBALFABRICOAM）_92520017.md)**命令中“OAMINTERVAL”参数配置值。建议小于“OAMINTERVAL”参数与“OAMMULTIPLIER”参数的乘积。<br>- 必须是200毫秒的倍数。 |
| UPDCHKPRDMULT | 检测TB出端口刷新的周期倍数 | 可选必选说明：条件可选参数。<br>前提条件：该参数在“TBPORTCHKSW”配置为“ENABLE”时为条件可选参数。<br>参数含义：该参数用于设置检测NP内POD TB出端口是否刷新的周期倍数。检测周期的时长是该参数配置值与<br>**[SET GLOBALFABRICOAM](../../../../系统调测/PAE 调测命令/配置/设置OAM全局配置（SET GLOBALFABRICOAM）_92520017.md)**<br>命令中的“OAMINTERVAL”参数的配置值的乘积。如果持续未刷新的时长超过检测周期的时长，则上报告警。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为5~100。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [NP端口检测的参数（NPPORTCHKPARA）](configobject/UDG/20.15.2/NPPORTCHKPARA.md)

## 使用实例

设置内联口带宽利用率告警上报阈值为85：

```
SET NPPORTCHKPARA: INTLBWALMRPTTHD=85;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置NP端口检测的参数（SET-NPPORTCHKPARA）_44275545.md`
